# PyModule Entrypoint Calling Convention

## How `entrypoint_dispatch` returns

Pyromaniac's `entrypoint_dispatch` has **two distinct return paths** depending on whether the
Python method returns `True` (claimed) or a falsy value (not claimed):

```python
# Simplified from pymodules.py
def entrypoint_dispatch(self, name, regs):
    ...
    handled = entrypoint(regs)
    if not handled:
        regs.pc = regs.lr          # return via LR (normal subroutine return)
    else:
        regs.pc = memory[regs.sp]  # pop PC from stack top
        regs.sp += 4
```

This mirrors the RISC OS convention for OS vectors, where:

- The vector dispatcher pushes the caller's return address onto the stack before branching.
- An **unclaiming** handler returns via `MOV pc, lr`.
- A **claiming** handler returns by popping the previously pushed return address from the stack.

## Entry points as OS vectors

When used with `OS_Claim`, the OS itself pushes the return address before dispatching, so the
stack is in the correct state automatically.

```python
def initialise(self, arguments, pwp):
    self.ro.kernel.api.os_claim(vectors.ByteV,
                                self.module.entrypoints['my_handler'].address,
                                self.pwp.address)
```

The module's private word address is registered as R12. On call: R12 = private word address.

## Entry points as custom function descriptors

Some RISC OS APIs accept a `(workspace, function)` descriptor pair where the API calls:

```
R12 = descriptor[0]   (workspace pointer)
PC  = descriptor[1]   (function address)
```

When an entrypoint is used this way (not through `OS_Claim`), the **caller** is responsible for
pushing the return address onto the stack before branching to the entry point. If the Python
handler returns `True`, Pyromaniac pops PC from SP — so whatever is on top of the stack when
the entrypoint is entered must be the correct return address.

### Setting up the descriptor

In `swi_end` or equivalent, store the entry point address in the descriptor and point
`descriptor[0]` at whatever R12 should hold on call:

```python
entry_addr = self.module.entrypoints['my_fn'].address
self._mem(descriptor_ptr    ).word = workspace_ptr  # passed as R12
self._mem(descriptor_ptr + 4).word = entry_addr
```

### RISC OS-side calling shim (BBC BASIC)

If you need to call such a descriptor from BBC BASIC using `USR`, write a three-instruction
shim that pushes LR onto the stack and then loads R12 and PC from the descriptor:

```bbcbasic
DIM MC% 16
P%=MC%
[OPT 2
 STR r14,[r13,#-4]!   ; push return address (LR from BASIC's USR call)
 LDR r12,[r1]         ; load workspace pointer from descriptor[0]
 LDR pc,[r1,#4]       ; jump to function (descriptor[1])
]
```

Usage:

```bbcbasic
A%=colour    : REM R0 = input
B%=desc_ptr  : REM R1 = descriptor address
result%=USR(MC%)
```

When the Python handler returns `True`, Pyromaniac pops the PC from the stack (the LR we
pushed), returning correctly to BASIC's `USR` cleanup.

**Why NOT to use a four-instruction STMFD/MOV/LDMIA/LDMFD pattern:**

A naive shim that does `STMFD r13!,{r12,r14}` pushes R12 first (at the lower stack address),
so R12 — not LR — is at SP when the entrypoint is entered. `entrypoint_dispatch` would then
pop R12 as the return PC, jumping to garbage.

### R12 and module instance lookup

`entrypoint_dispatch` searches module instances for one whose `privateword_pointer.address`
matches R12. If none matches (because R12 holds a workspace pointer, not a private word), it
falls back to the **preferred instance** (the most recently initialised instance of the
module). This means calling an entrypoint with a non-private-word R12 is safe provided there
is exactly one instance of the module loaded — the preferred instance is used.

If a module may have multiple instances and entrypoints are used as function descriptors, store
`self.pwp.address` in `descriptor[0]` instead, and look up the workspace from the private word
inside the Python handler:

```python
def my_fn(self, regs):
    # regs[12] == self.pwp.address (private word), not the workspace
    workspace = self._mem(self.pwp.address).word
    ...
```
