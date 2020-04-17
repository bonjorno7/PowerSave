import bpy
from . import addon
from . import prefs


def register():
    bpy.utils.register_class(addon.PowerSaveProps)
    bpy.utils.register_class(prefs.PowerSavePrefs)

    bpy.types.WindowManager.powersave = bpy.props.PointerProperty(type=addon.PowerSaveProps)


def unregister():
    del bpy.types.WindowManager.powersave

    bpy.utils.unregister_class(prefs.PowerSavePrefs)
    bpy.utils.register_class(addon.PowerSaveProps)
