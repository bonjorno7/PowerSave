import bpy
from .. import utils


class LoadAutosave(bpy.types.Operator):
    bl_idname = 'powersave.load_autosave'
    bl_label = 'Load Autosave'
    bl_options = {'INTERNAL'}
    bl_description = 'Load the autosave file for this blend'

    def draw(self, context):
        col = self.layout.column()
        col.label(text='The autosave file is newer.')
        col.label(text='Would you like to load it?')

    def execute(self, context):
        result = utils.load.load_autosave()
        self.report(result[0], result[1])
        return result[2]

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
