import bpy
from . import utils
from . import prefs
from . import handlers
from . import timers


def register():
    prefs.register()
    handlers.register()
    timers.register()


def unregister():
    timers.unregister()
    handlers.unregister()
    prefs.unregister()
