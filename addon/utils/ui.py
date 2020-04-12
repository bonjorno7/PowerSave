import bpy
from .. import icons


def get_icon():
    if bpy.data.is_saved:
        if bpy.data.is_dirty:
            icon = "gray"
        else:
            icon = "green"
    else:
        icon = "red"

    return icons.id(icon)


def tag_redraw():
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()
