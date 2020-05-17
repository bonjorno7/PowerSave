import bpy
from .. import utils


class LoadNext(bpy.types.Operator):
    bl_idname = 'powersave.load_next'
    bl_label = 'Load Next'
    bl_description = 'Load the next iteration of this file'
    bl_options = {'INTERNAL'}


    @classmethod
    def poll(cls, context):
        return utils.load.verify_version(1)


    def execute(self, context):
        result = utils.load.load_version(1)
        self.report(result[0], result[1])
        return result[2]
