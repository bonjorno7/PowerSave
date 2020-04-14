import bpy
from .. import utils


@bpy.app.handlers.persistent
def load_handler(dummy):
    prefs = utils.common.get_prefs()

    if prefs.save_on_startup:
        result = utils.save.save_datetime()
        print(result[1])
