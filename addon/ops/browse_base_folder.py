import bpy
import bpy_extras
from .. import utils


class BrowseBaseFolder(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    bl_idname = 'powersave.browse_base_folder'
    bl_label = 'Browse to PowerSave folder'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}
    bl_description = 'Browse to the PowerSave base folder'

    filter_glob: bpy.props.StringProperty(
        default='',
        options={'HIDDEN'},
    )


    def invoke(self, context, event):
        prefs = utils.common.prefs()
        self.filepath = prefs.base_folder
        return super().invoke(context, event)
 

    def execute(self, context):
        prefs = utils.common.prefs()
        folder = utils.files.as_path(self.filepath)

        while folder.name.lower() == folder.parent.name.lower():
            folder = folder.parent

        prefs.base_folder = str(folder)
        return {'FINISHED'}
