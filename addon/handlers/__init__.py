import bpy
from . import load_handler
from . import save_handler


def register():
    if load_handler.load_handler not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(load_handler.load_handler)

    if save_handler.save_handler not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(save_handler.save_handler)


def unregister():
    if load_handler.load_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(load_handler.load_handler)

    if save_handler.save_handler not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(save_handler.save_handler)
