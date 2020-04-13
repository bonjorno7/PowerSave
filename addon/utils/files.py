import bpy
import pathlib


def get_default_folder():
    temporary_directory = bpy.context.preferences.filepaths.temporary_directory
    return str(pathlib.Path(temporary_directory).joinpath("PowerSave"))
