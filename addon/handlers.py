import bpy
import os
import pathlib
from . import utils
from . import timers


@bpy.app.handlers.persistent
def load_handler(dummy):
    prefs = utils.get_prefs()

    if prefs.save_on_startup and not bpy.data.is_saved:
        name = utils.get_datetime("%Y-%m-%d/%Y-%m-%d__%H-%M-%S__01.blend")
        path = pathlib.Path(prefs.base_folder).joinpath(name)

        folder = str(path.parent)
        if not os.path.isdir(folder):
            os.mkdir(folder)

        bpy.ops.wm.save_mainfile(filepath=str(path))

    timers.unregister()
    timers.register()


def register():
    if load_handler not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(load_handler)


def unregister():
    if load_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(load_handler)
