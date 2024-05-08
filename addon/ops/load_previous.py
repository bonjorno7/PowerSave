import bpy
from .. import utils


class LoadPrevious(bpy.types.Operator):
    bl_idname = 'powersave.load_previous'
    bl_label = 'Load Previous'
    bl_options = {'INTERNAL'}
    bl_description = 'Load the previous iteration of this file'


    def draw(self, context):
        col = self.layout.column()
        col.label(text='This file has unsaved changes.')
        col.label(text='Are you sure you want to switch?')


    @classmethod
    def poll(cls, context):
        return utils.load.verify_version(-1)


    def execute(self, context):
        result = utils.load.load_version(-1)
        self.report(result[0], result[1])
        return result[2]


    def invoke(self, context, event):
        if bpy.data.is_saved and bpy.data.is_dirty:
            return context.window_manager.invoke_props_dialog(self)
        else:
            return self.execute(context)
