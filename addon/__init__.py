from . import icons
from . import prefs
from . import handlers
from . import timers


def register():
    icons.register()
    prefs.register()
    handlers.register()
    timers.register()


def unregister():
    timers.unregister()
    handlers.unregister()
    prefs.unregister()
    icons.unregister()
