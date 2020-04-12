import bpy
import pathlib
from .. import utils
from .. import timers


@bpy.app.handlers.persistent
def load_handler(dummy):
    prefs = utils.common.get_prefs()

    if prefs.save_on_startup and prefs.base_folder and not bpy.data.is_saved:
        name = f"{utils.common.get_datetime(prefs.datetime_format)}.blend"
        path = pathlib.Path(prefs.base_folder).joinpath(name).resolve()

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            bpy.ops.wm.save_mainfile(filepath=str(path))

        except:
            print(f"Failed to save to {path}")
