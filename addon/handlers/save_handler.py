import bpy
from .. utils import common
from .. import timers


@bpy.app.handlers.persistent
def save_handler(dummy):
    common.tag_redraw()
    timers.unregister()
    timers.register()
