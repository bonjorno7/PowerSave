import bpy


@bpy.app.handlers.persistent
def load_handler(dummy):
    print('FILE LOADED')
