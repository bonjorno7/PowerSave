import bpy
from . import utils
from . import prefs
from . import timers


def register():
    bpy.utils.register_class(prefs.PowerSavePrefs)
    bpy.app.timers.register(timers.autosave_timer, persistent=True)


def unregister():
    bpy.app.timers.unregister(timers.autosave_timer)
    bpy.utils.unregister_class(prefs.PowerSavePrefs)
