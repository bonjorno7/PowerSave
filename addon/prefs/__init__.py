import bpy
from . import prefs


def register():
    try:
        bpy.utils.register_class(prefs.PowerSavePrefs)
    except:
        pass


def unregister():
    try:
        bpy.utils.unregister_class(prefs.PowerSavePrefs)
    except:
        pass
