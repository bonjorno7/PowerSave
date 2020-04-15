import bpy
from .. import utils


class PowerSave(bpy.types.Operator):
    bl_idname = "powersave.powersave"
    bl_label = "PowerSave"
    bl_description = "Save this blend file in your PowerSave folder with the chosen name"

    @classmethod
    def poll(cls, context):
        return utils.common.get_prefs().powersave_name

    def execute(self, context):
        result = utils.save.powersave()
        self.report(result[0], result[1])
        return result[2]
