from . import icons
from . import prefs
from . import ops
from . import timers
from . import handlers
from . import ui


def register():
    icons.register()
    prefs.register()
    ops.register()
    timers.register()
    handlers.register()
    ui.register()


def unregister():
    ui.unregister()
    handlers.unregister()
    timers.unregister()
    ops.unregister()
    prefs.unregister()
    icons.unregister()
