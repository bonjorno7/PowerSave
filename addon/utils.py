import bpy
import datetime
from . import icons


addon_name = __name__.partition('.')[0]


def get_prefs():
    return bpy.context.preferences.addons[addon_name].preferences


def get_datetime(string: str="%Y-%m-%d__%H-%M-%S"):
    return datetime.datetime.now().strftime(string)


def get_icon():
    if bpy.data.is_saved:
        if bpy.data.is_dirty:
            icon = "blue"
        else:
            icon = "green"
    else:
        icon = "red"

    return icons.id(icon)
