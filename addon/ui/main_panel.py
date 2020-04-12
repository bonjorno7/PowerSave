import bpy
from .. import utils


class PowerSavePanel(bpy.types.Panel):
    bl_idname = "POWERSAVE_PT_PowerSavePanel"
    bl_category = "PowerSave"
    bl_label = "PowerSave"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        if self.is_popover:
            layout.ui_units_x = 8

        prefs = utils.common.get_prefs()

        layout.prop(prefs, "autosave_interval")
        layout.prop(prefs, "save_on_startup")


def popover(self, context):
    layout = self.layout
    panel = PowerSavePanel.bl_idname
    icon = utils.ui.get_icon()
    layout.popover(panel, text="", icon_value=icon)
