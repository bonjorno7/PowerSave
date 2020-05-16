import bpy
from .. import utils


@bpy.app.handlers.persistent
def load_handler(_):
    utils.common.update_powersave_name()
    prefs = utils.common.prefs()

    if prefs.save_on_startup and not bpy.data.is_saved:
        bpy.ops.powersave.powersave()

    if prefs.autosave_to_copy and bpy.data.is_saved:
        if utils.save.should_load_autosave():
            bpy.ops.powersave.load_autosave('INVOKE_DEFAULT')
