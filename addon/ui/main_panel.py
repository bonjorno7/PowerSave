import bpy
from .. import utils


class PowerSavePanel(bpy.types.Panel):
    bl_idname = 'POWERSAVE_PT_PowerSavePanel'
    bl_category = 'PowerSave'
    bl_label = f'PowerSave'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    def draw(self, context):
        prefs = utils.common.prefs()

        layout = self.layout

        if self.is_popover:
            layout.ui_units_x = 8

        col = layout.column()

        box = col.box().column()

        if hops():
            try:
                box.operator('hops.powersave', text='PowerSave (hops)')
            except:
                box.operator('powersave.powersave')
        else:
            box.operator('powersave.powersave')

        box.prop(prefs, 'powersave_name', text='')

        col.separator()

        box = col.box().column()
        flow = box.grid_flow(align=True)
        flow.operator('powersave.load_previous', text='', icon='REW')
        flow.operator('powersave.load_next', text='', icon='FF')
        box.operator('powersave.open_project_folder')

        col.separator()

        box = col.box().column()
        box.prop(prefs, 'use_autosave')
        box.prop(prefs, 'autosave_interval')
        box.prop(prefs, 'autosave_to_copy')
        box.prop(prefs, 'save_on_startup')


def popover(self, context):
    layout = self.layout
    panel = PowerSavePanel.bl_idname
    icon = utils.ui.get_icon()
    layout.popover(panel, text='', icon_value=icon)


def hops():
    wm = bpy.context.window_manager

    if hasattr(wm, 'Hard_Ops_folder_name'):
        return bpy.context.preferences.addons[wm.Hard_Ops_folder_name].preferences

    return False
