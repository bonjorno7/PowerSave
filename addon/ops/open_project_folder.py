import bpy
from .. import utils


class OpenProjectFolder(bpy.types.Operator):
    bl_idname = "powersave.open_project_folder"
    bl_label = "Open Project Folder"

    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved

    def execute(self, context):
        result = utils.files.open_project_folder()
        self.report(result[0], result[1])
        return result[2]