import bpy
from .. import utils


class PowerSave(bpy.types.Operator):
    bl_idname = 'powersave.powersave'
    bl_label = 'PowerSave'
    bl_options = {'REGISTER', 'INTERNAL'}
    bl_description = utils.common.description(
        'Save this blend file with the name in the text field below',
        'If no name is provided, generate one based on the date and time',
        'If this blend has never been saved, put it in the PowerSave folder',
    )


    def execute(self, context):
        result = utils.save.powersave()
        self.report(result[0], result[1])
        return result[2]
