# PyModule Service Announcements

PyModules can both receive service calls through `service(self, service, regs)` and issue them through the Pyromaniac services dispatcher.

## Receiving services

If `service()` returns `True`, Pyromaniac marks the service as claimed by setting `R1` to `Service_Serviced`.

## Issuing services immediately

To announce a service call from a PyModule, use `self.ro.services.dispatch()`:

```python
import riscos.constants.services as services

def initialise(self, arguments, pwp):
    super(MyModule, self).initialise(arguments, pwp)
    self.ro.services.dispatch(services.Service_MyModuleStarted, preserve=True)
```

Use `preserve=True` unless you intentionally want the service dispatch to leave modified register state behind. If the module may run in an environment where the dispatcher is not present, guard it with `hasattr(self.ro, 'services')`.

## Startup announcements via callback

If a module's startup service must be deferred until control returns to user mode, do not issue it directly in `initialise()`. Instead, create an entry point, schedule it with `OS_AddCallBack`, and clear any pending callback with `OS_RemoveCallBack` during finalisation if it has not yet fired.

This mirrors the common C module pattern where startup is announced from a callback rather than directly from initialisation.

```python
import riscos.constants.services as services

class MyModule(PyModule):
    entrypoint_names = ['callback_announce']

    def __init__(self, ro, module):
        super(MyModule, self).__init__(ro, module)
        self.callback_pending = False

    def initialise(self, arguments, pwp):
        super(MyModule, self).initialise(arguments, pwp)
        func = self.module.entrypoints['callback_announce'].address
        self.ro.kernel.api.os_addcallback(func, self.pwp)
        self.callback_pending = True

    def finalise(self, pwp):
        if self.callback_pending:
            self.callback_pending = False
            func = self.module.entrypoints['callback_announce'].address
            self.ro.kernel.api.os_removecallback(func, self.pwp)

    def callback_announce(self, regs):
        self.callback_pending = False
        self.ro.services.dispatch(services.Service_MyModuleStarted, preserve=True)
```

Useful examples in the Pyromaniac tree include modules such as `sharefs`, `internet`, and `cdfsdriver`.
