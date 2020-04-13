import bpy
from . import main_panel


def register():
    bpy.utils.register_class(main_panel.PowerSavePanel)
    bpy.types.VIEW3D_MT_editor_menus.append(main_panel.popover)


def unregister():
    bpy.types.VIEW3D_MT_editor_menus.remove(main_panel.popover)
    bpy.utils.unregister_class(main_panel.PowerSavePanel)
