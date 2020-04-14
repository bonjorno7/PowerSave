import bpy
from .. import utils


class SaveIncremental(bpy.types.Operator):
    bl_idname = "powersave.save_incremental"
    bl_label = "Save Incremental"

    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved

    def execute(self, context):
        result = utils.save.save_incremental()
        self.report(result[0], result[1])
        return result[2]
