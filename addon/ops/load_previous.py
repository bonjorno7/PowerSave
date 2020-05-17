import bpy
from .. import utils


class LoadPrevious(bpy.types.Operator):
    bl_idname = 'powersave.load_previous'
    bl_label = 'Load Previous'
    bl_description = 'Load the previous iteration of this file'
    bl_options = {'INTERNAL'}


    @classmethod
    def poll(cls, context):
        return utils.load.verify_version(-1)


    def execute(self, context):
        result = utils.load.load_version(-1)
        self.report(result[0], result[1])
        return result[2]
