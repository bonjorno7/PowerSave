import bpy
import os
import pathlib
from .. import utils
from .. import timers


@bpy.app.handlers.persistent
def load_handler(dummy):
    prefs = utils.common.get_prefs()

    if prefs.save_on_startup and prefs.base_folder and not bpy.data.is_saved:
        name = utils.common.get_datetime(prefs.datetime_format)
        path = pathlib.Path(prefs.base_folder).joinpath(name).resolve()

        try:
            os.makedirs(str(path.parent), exist_ok=True)
            bpy.ops.wm.save_mainfile(filepath=str(path))

        except:
            print(f"Failed to save to {path}")
