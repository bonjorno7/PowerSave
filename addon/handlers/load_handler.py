import bpy
from .. import utils


@bpy.app.handlers.persistent
def load_handler(_):
    utils.common.update_powersave_name()
    prefs = utils.common.prefs()

    if bpy.data.is_saved:
        if utils.load.should_load_autosave():
            bpy.ops.powersave.load_autosave('INVOKE_DEFAULT')

    else:
        if prefs.save_on_startup:
            bpy.ops.powersave.powersave()
