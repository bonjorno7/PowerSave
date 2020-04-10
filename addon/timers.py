import bpy
from . import utils


def autosave_timer():
    prefs = utils.get_prefs()

    if bpy.data.is_saved and bpy.data.is_dirty:
        bpy.ops.wm.save_mainfile(check_existing=False)

    return prefs.autosave_interval * 60


def register():
    if not bpy.app.timers.is_registered(autosave_timer):
        interval = utils.get_prefs().autosave_interval * 60
        bpy.app.timers.register(autosave_timer, first_interval=interval, persistent=True)


def unregister():
    if bpy.app.timers.is_registered(autosave_timer):
        bpy.app.timers.unregister(autosave_timer)
