import bpy
import os
import pathlib
from .. utils import common
from .. import timers


@bpy.app.handlers.persistent
def load_handler(dummy):
    prefs = common.get_prefs()

    if prefs.save_on_startup and not bpy.data.is_saved:
        name = common.get_datetime(prefs.datetime_format)
        path = pathlib.Path(prefs.base_folder).joinpath(name)
        os.makedirs(str(path.parent), exist_ok=True)
        bpy.ops.wm.save_mainfile(filepath=str(path))

    timers.unregister()
    timers.register()
