import bpy
from . import prefs


def register():
    bpy.utils.register_class(prefs.PowerSavePrefs)


def unregister():
    bpy.utils.unregister_class(prefs.PowerSavePrefs)
