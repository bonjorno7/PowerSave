import bpy
from .. import utils


def autosave_timer() -> float:
    prefs = utils.common.prefs()

    if prefs.use_autosave and bpy.data.is_saved and bpy.data.is_dirty:
        scene = bpy.context.scene
        if hasattr(scene, 'bc') and scene.bc.running:
            return 1

        current_path = utils.files.as_path(bpy.data.filepath)
        autosave_path = utils.files.as_autosave(current_path, mkdir=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(autosave_path), check_existing=False, copy=True)

    if prefs.autosave_external_text:
        for text in bpy.data.texts.values():
            if not text.is_in_memory and text.is_dirty:
                utils.common.override(bpy.context, {'edit_text': text}, bpy.ops.text.save)

    return prefs.autosave_interval * 60
