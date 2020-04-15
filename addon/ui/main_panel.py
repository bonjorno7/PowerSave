import bpy
from .. import utils


class PowerSavePanel(bpy.types.Panel):
    bl_idname = "POWERSAVE_PT_PowerSavePanel"
    bl_category = "PowerSave"
    bl_label = f"PowerSave {utils.common.get_version()}"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        prefs = utils.common.get_prefs()

        layout = self.layout

        if self.is_popover:
            layout.ui_units_x = 8

        col = layout.column()

        col.label(text="Preferences")
        box = col.box().column()

        box.prop(prefs, "autosave_interval")
        box.prop(prefs, "save_on_startup")

        col.separator()

        col.label(text="Operators")
        box = col.box().column()

        box.operator("powersave.save_datetime")
        box.operator("powersave.save_incremental")
        box.operator("powersave.open_project_folder")


def popover(self, context):
    layout = self.layout
    panel = PowerSavePanel.bl_idname
    icon = utils.ui.get_icon()
    layout.popover(panel, text="", icon_value=icon)
