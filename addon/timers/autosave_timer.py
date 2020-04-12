import bpy
from .. import utils


def autosave_timer():
    prefs = utils.common.get_prefs()

    if bpy.data.is_saved and bpy.data.is_dirty:
        bpy.ops.wm.save_mainfile(check_existing=False)

    return prefs.autosave_interval * 60
