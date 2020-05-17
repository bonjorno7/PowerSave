import bpy
from . import powersave
from . import load_autosave
from . import load_previous
from . import load_next
from . import open_project_folder


def register():
    bpy.utils.register_class(powersave.PowerSave)
    bpy.utils.register_class(load_autosave.LoadAutosave)
    bpy.utils.register_class(load_previous.LoadPrevious)
    bpy.utils.register_class(load_next.LoadNext)
    bpy.utils.register_class(open_project_folder.OpenProjectFolder)


def unregister():
    bpy.utils.unregister_class(open_project_folder.OpenProjectFolder)
    bpy.utils.unregister_class(load_next.LoadNext)
    bpy.utils.unregister_class(load_previous.LoadPrevious)
    bpy.utils.unregister_class(load_autosave.LoadAutosave)
    bpy.utils.unregister_class(powersave.PowerSave)
