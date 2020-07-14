import bpy
from .. import utils


class PurgeOrphans(bpy.types.Operator):
    bl_idname = 'powersave.purge_orphans'
    bl_label = 'Purge Orphans'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = 'Purge orphan data in a loop until none is left'


    def execute(self, context):
        result = utils.misc.purge_orphans()
        self.report(result[0], result[1])
        return result[2]
