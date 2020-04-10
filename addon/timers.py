import bpy
from . import utils


def autosave_timer():
    prefs = utils.get_prefs()

    print("AUTO SAVING")

    return prefs.autosave_interval * 60


def register():
    unregister()

    interval = utils.get_prefs().autosave_interval * 60
    bpy.app.timers.register(autosave_timer, first_interval=interval, persistent=True)


def unregister():
    if bpy.app.timers.is_registered(autosave_timer):
        bpy.app.timers.unregister(autosave_timer)
