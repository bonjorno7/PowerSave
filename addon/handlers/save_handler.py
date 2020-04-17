import bpy
from .. import utils
from .. import timers


@bpy.app.handlers.persistent
def save_handler(_):
    utils.common.update_powersave_name()

    utils.ui.tag_redraw()

    timers.unregister()
    timers.register()
