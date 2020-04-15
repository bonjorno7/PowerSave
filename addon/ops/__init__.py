import bpy
from . import powersave
from . import save_datetime
from . import save_incremental
from . import open_project_folder


def register():
    bpy.utils.register_class(powersave.PowerSave)
    bpy.utils.register_class(save_datetime.SaveDatetime)
    bpy.utils.register_class(save_incremental.SaveIncremental)
    bpy.utils.register_class(open_project_folder.OpenProjectFolder)


def unregister():
    bpy.utils.unregister_class(open_project_folder.OpenProjectFolder)
    bpy.utils.unregister_class(save_incremental.SaveIncremental)
    bpy.utils.unregister_class(save_datetime.SaveDatetime)
    bpy.utils.unregister_class(powersave.PowerSave)
