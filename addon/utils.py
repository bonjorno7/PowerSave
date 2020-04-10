import bpy
import datetime


addon_name = __name__.partition('.')[0]


def get_prefs():
    return bpy.context.preferences.addons[addon_name].preferences


def get_datetime(string: str="%Y-%m-%d__%H-%M-%S"):
    return datetime.datetime.now().strftime(string)
