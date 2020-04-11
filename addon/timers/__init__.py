import bpy
from .. utils import common
from . import autosave_timer


def register():
    if not bpy.app.timers.is_registered(autosave_timer.autosave_timer):
        interval = common.get_prefs().autosave_interval * 60
        bpy.app.timers.register(autosave_timer.autosave_timer, first_interval=interval, persistent=True)


def unregister():
    if bpy.app.timers.is_registered(autosave_timer.autosave_timer):
        bpy.app.timers.unregister(autosave_timer.autosave_timer)
