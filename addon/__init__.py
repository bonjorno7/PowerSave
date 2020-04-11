from . import icons
from . import prefs
from . import handlers
from . import timers
from . import ui


def register():
    icons.register()
    prefs.register()
    handlers.register()
    timers.register()
    ui.register()


def unregister():
    ui.unregister()
    timers.unregister()
    handlers.unregister()
    prefs.unregister()
    icons.unregister()
