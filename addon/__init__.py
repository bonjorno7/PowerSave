import bpy
from . import utils
from . import prefs
from . import timer


def register():
    bpy.utils.register_class(prefs.PowerSavePrefs)
    bpy.app.timers.register(timer.autosave_timer, persistent=True)


def unregister():
    bpy.app.timers.unregister(timer.autosave_timer)
    bpy.utils.unregister_class(prefs.PowerSavePrefs)
