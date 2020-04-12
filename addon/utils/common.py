import bpy
import pathlib
import datetime


module_name = __name__.partition('.')[0]


def get_prefs():
    return bpy.context.preferences.addons[module_name].preferences


def description(*args):
    return ".\n".join(args)


def get_default_folder():
    temporary_directory = bpy.context.preferences.filepaths.temporary_directory
    return str(pathlib.Path(temporary_directory).joinpath("PowerSave"))


def get_datetime(string: str="%Y %m %d %H %M %S"):
    return datetime.datetime.now().strftime(string)
