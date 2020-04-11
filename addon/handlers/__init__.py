import bpy
from . import load_handler


def register():
    if load_handler.load_handler not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(load_handler.load_handler)


def unregister():
    if load_handler.load_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(load_handler.load_handler)
