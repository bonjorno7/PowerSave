import bpy
from .. utils import common


def autosave_timer():
    prefs = common.get_prefs()

    if bpy.data.is_saved and bpy.data.is_dirty:
        bpy.ops.wm.save_mainfile(check_existing=False)
        common.tag_redraw()

    return prefs.autosave_interval * 60
