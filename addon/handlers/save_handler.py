import bpy
from .. import utils
from .. import timers


@bpy.app.handlers.persistent
def save_handler(dummy):
    utils.ui.tag_redraw()
    timers.unregister()
    timers.register()
