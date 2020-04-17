import bpy
from .. import utils


class PowerSavePanel(bpy.types.Panel):
    bl_idname = 'POWERSAVE_PT_PowerSavePanel'
    bl_category = 'PowerSave'
    bl_label = f'PowerSave {utils.common.version()}'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    def draw(self, context):
        prefs = utils.common.prefs()

        layout = self.layout

        if self.is_popover:
            layout.ui_units_x = 8

        col = layout.column()

        box = col.box().column()
        box.operator('powersave.powersave')
        box.prop(prefs, 'powersave_name', text='')

        col.separator()

        box = col.box().column()
        box.operator('powersave.open_project_folder')

        col.separator()

        box = col.box().column()
        box.prop(prefs, 'use_autosave')
        box.prop(prefs, 'autosave_interval')
        box.prop(prefs, 'save_on_startup')


def popover(self, context):
    layout = self.layout
    panel = PowerSavePanel.bl_idname
    icon = utils.ui.get_icon()
    layout.popover(panel, text='', icon_value=icon)
