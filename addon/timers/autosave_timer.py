import bpy
import pathlib
from .. import utils


def autosave_timer():
    prefs = utils.common.prefs()

    if prefs.use_autosave and bpy.data.is_saved and bpy.data.is_dirty:
        path = utils.files.as_path(bpy.data.filepath)

        if prefs.autosave_to_copy:
            path = utils.files.with_autosave(path)

        bpy.ops.wm.save_as_mainfile(filepath=str(path), check_existing=False, copy=True)

    return prefs.autosave_interval * 60
