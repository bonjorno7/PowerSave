import bpy
from . import utils
from . import prefs
from . import handlers
from . import timers


def register():
    bpy.utils.register_class(prefs.PowerSavePrefs)
    bpy.app.handlers.load_post.append(handlers.load_handler)
    bpy.app.timers.register(timers.autosave_timer, persistent=True)


def unregister():
    bpy.app.timers.unregister(timers.autosave_timer)
    bpy.app.handlers.load_post.remove(handlers.load_handler)
    bpy.utils.unregister_class(prefs.PowerSavePrefs)
