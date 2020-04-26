import bpy
import pathlib
from .. import utils


def autosave_timer():
    prefs = utils.common.prefs()

    if prefs.use_autosave and bpy.data.is_saved and bpy.data.is_dirty:
        path = pathlib.Path(bpy.data.filepath)

        if prefs.autosave_to_copy:
            path = path.with_suffix('.autosave')

        bpy.ops.wm.save_as_mainfile(filepath=str(path), check_existing=False, copy=True)

    return prefs.autosave_interval * 60
