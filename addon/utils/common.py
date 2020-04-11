import bpy
import datetime
from .. import icons


module_name = __name__.partition('.')[0]


def get_prefs():
    return bpy.context.preferences.addons[module_name].preferences


def get_datetime(string: str="%Y-%m-%d__%H-%M-%S"):
    return datetime.datetime.now().strftime(string)


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
