"""
Stub module implementation.

A stub PyModule which can be used as the basis for other modules.
"""

from pyromaniac.config import Configuration

from riscos.modules.pymodules import PyModule

import riscos.constants.services as services


class StubConfig(Configuration):
    _types = {
            'flag': 'bool',
        }
    _help = {
            'flag': """
Controls whether something will happen or not.
""",
        }
    _safe = {
        }
    flag = True


class Stub(PyModule):
    version = '0.01'
    date = '18 May 2026'

    # SWI definitions - remove if not needed
    swi_base = 0xc76c0
    swi_prefix = "Stub"
    swi_names = [
            "Trigger",
        ]

    # Commands - remove if not needed
    commands = [
            ('Stub', 'Example command help text.', 0x00000000),
            ('StubTwo', 'Example command which takes two parameters.', 0x00020001),
        ]

    def __init__(self, ro, module):
        super(Stub, self).__init__(ro, module)

        # SWI dispatch table for functions
        self.swi_dispatch = {
                0: self.swi_trigger,
            }

        self.debug_stub = False
        self.ro.debug_register_ivar('stub', self)

    def initialise(self, arguments, pwp):
        super(Stub, self).initialise(arguments, pwp)
        if self.debug_stub:
            print("Module Stub initialised")

    def finalise(self, pwp):
        if self.debug_netstatus:
            print("Module Stub dying")

    def service(self, service, regs):
        # Service handler; remove the function if not needed.
        if service == services.Service_ExternalBell:
            self.ro.kernel.writeln("Bell!")
            return True  # We claimed it

    # SWI dispatch function - remove if not needed
    def swi(self, offset, regs):
        func = self.swi_dispatch.get(offset, None)
        if func:
            return func(regs)

        return False

    def swi_trigger(self, regs):
        """
        SWI was triggered.
        """
        if self.debug_stub:
            print("SWI triggered")
        # We just increment R0.
        regs[0] = regs[0] + 1
        return True

    def cmd_stub(self, args):
        """
        Syntax: *Stub
        """
        self.ro.kernel.writeln("You ran stub")

    def cmd_stubtwo(self, args):
        """
        Syntax: *StubTwo <one> <two>
        """
        self.ro.kernel.writeln("You ran stub with " + args)
