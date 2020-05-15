import bpy
from .. import utils


@bpy.app.handlers.persistent
def load_handler(_):
    prefs = utils.common.prefs()

    utils.common.update_powersave_name()

    if prefs.save_on_startup and not bpy.data.is_saved:
        result = utils.save.powersave()
        print(result[1])
