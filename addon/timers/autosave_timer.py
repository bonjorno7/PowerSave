import bpy
from .. import utils


def autosave_timer() -> float:
    prefs = utils.common.prefs()

    if prefs.use_autosave and bpy.data.is_saved and bpy.data.is_dirty:
        scene = bpy.context.scene
        if 'bc' in scene and scene.bc.running:
            return 1

        current_path = utils.files.as_path(bpy.data.filepath)
        autosave_path = utils.files.as_autosave(current_path, mkdir=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(autosave_path), check_existing=False, copy=True)

    return prefs.autosave_interval * 60
