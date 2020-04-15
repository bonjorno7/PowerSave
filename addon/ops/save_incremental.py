import bpy
from .. import utils


class SaveIncremental(bpy.types.Operator):
    bl_idname = "powersave.save_incremental"
    bl_label = "Save Incremental"
    bl_description = utils.common.description(
        "Save this file with the last number incremented one",
        "If the file name doesn't contain a number, one is added at the end",
    )

    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved

    def execute(self, context):
        result = utils.save.save_incremental()
        self.report(result[0], result[1])
        return result[2]
