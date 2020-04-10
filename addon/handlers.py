import bpy
from . import utils
from . import timers


@bpy.app.handlers.persistent
def load_handler(dummy):
    prefs = utils.get_prefs()

    if prefs.save_on_startup and not bpy.data.is_saved:
        path = "C:/Users/Jorijn/Documents/Blender/PowerSave/test01.blend"
        bpy.ops.wm.save_mainfile(filepath=path, check_existing=False)

    timers.unregister()
    timers.register()


def register():
    if load_handler not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(load_handler)


def unregister():
    if load_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(load_handler)
