# PyModule Memory And I/O

## Memory access

Pyromaniac provides convenient methods for reading from RISC OS memory via `self.ro.memory[address]`.

### Reading strings

```python
filename_ptr = regs[1]
filename = self.ro.memory[filename_ptr].string
```

If the original C interface compares a string parameter by pointer identity, preserve the raw register value as well as the decoded string. `self.ro.memory[regs[0]].string` gives you the text, but not the original pointer for identity comparisons.

### Reading quins

```python
time_ptr = regs[5]
quin = self.ro.memory[time_ptr].quin
```

### Reading words

```python
ptr = regs[2]
words = self.ro.memory[ptr].read_words(count)
word = self.ro.memory[ptr].word
signed_word = self.ro.memory[ptr].signedword
self.ro.memory[ptr].word = word
```

### Reading double words

```python
ptr = regs[2]
dword = self.ro.memory[ptr].dword
signed_dword = self.ro.memory[ptr].signeddword
self.ro.memory[ptr].dword = dword
```

### Bytes

```python
ptr = regs[3]
data = self.ro.memory[ptr].read_bytes(length)
self.ro.memory[ptr].write_bytes(data)
byte = self.ro.memory[ptr].byte
self.ro.memory[ptr].byte = byte
```

## Time conversion

```python
from riscos.rotime import quin_to_datetime

quin = self.ro.memory[time_ptr].quin
dt = quin_to_datetime(quin)
timestamp = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
```

## File I/O

Never use Python's built-in `open()` for RISC OS files. It accesses the host filesystem, not the emulated RISC OS filesystem.

```python
self.file = self.ro.kernel.api.open(self.filename, 'w')
self.file.write('example\n')
self.file.flush()
self.file.close()
```

Supported modes:

- `'w'` - Write (create/truncate)
- `'r'` - Read
- `'a'` - Append
- `'w+'` - Read/write (create/truncate)
- `'r+'` - Read/write (existing file)

## Calling SWIs

SWIs can be called through `self.ro.kernel.api`. Output to the screen using `OS_Write*` SWIs is usually best done through:

- `self.ro.kernel.write(str)`
- `self.ro.kernel.writeln(str)`

When calling `self.ro.kernel.api.swi(swi_number, args)`, the `args` parameter must be an iterable:

- Correct: `self.ro.kernel.api.swi(swis.Hourglass_On, (r1,))`
- Incorrect: `self.ro.kernel.api.swi(swis.Hourglass_On, r1)`
