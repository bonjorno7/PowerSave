import bpy
import datetime


module_name = __name__.partition('.')[0]


def get_prefs():
    return bpy.context.preferences.addons[module_name].preferences


def description(*args):
    return ".\n".join(args)


def get_datetime(string):
    return datetime.datetime.now().strftime(string)
