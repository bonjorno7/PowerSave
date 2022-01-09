import bpy
from .. import utils


class PowerSavePanel(bpy.types.Panel):
    bl_idname = 'POWERSAVE_PT_PowerSavePanel'
    bl_category = 'PowerSave'
    bl_label = 'PowerSave'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    def draw(self, context):
        prefs = utils.common.prefs()

        layout = self.layout
        column = layout.column()

        if self.is_popover:
            layout.ui_units_x = prefs.popover_width

            panel_dict = {
                'POWERSAVE': 'PowerSave',
                'POWERLINK': 'PowerLink',
                'POWERBACKUP': 'PowerBackup',
                'POWERMANAGE': 'PowerManage',
            }

            row = column.row()
            row.label(text=panel_dict.get(prefs.panel_tab, 'Unknown'))
            row.prop(prefs, 'panel_tab', expand=True, icon_only=True)
            column.separator()

        if prefs.panel_tab == 'POWERSAVE' or not self.is_popover:
            powersave_draw(self, column)

        elif prefs.panel_tab == 'POWERLINK':
            powerlink_draw(self, column)

        elif prefs.panel_tab == 'POWERBACKUP':
            powerbackup_draw(self, column)

        elif prefs.panel_tab == 'POWERMANAGE':
            powermanage_draw(column)


def popover(self, context):
    layout = self.layout.row(align=False)
    panel = PowerSavePanel.bl_idname
    icon = utils.ui.get_icon()
    layout.popover(panel, text='', icon_value=icon)


def powersave_draw(self, column):
    prefs = utils.common.prefs()
    filepaths = bpy.context.preferences.filepaths

    box = column.box().column()
    if hasattr(bpy.types, 'HOPS_OT_powersave'):
        box.operator('hops.powersave', text='PowerSave (hops)')
    else:
        box.operator('powersave.powersave')
    box.prop(prefs, 'powersave_name', text='')

    column.separator()

    box = column.box().column()
    flow = box.grid_flow(align=True)
    flow.operator('powersave.load_previous', text='', icon='REW')
    flow.operator('powersave.load_next', text='', icon='FF')
    box.operator('powersave.open_project_folder')

    column.separator()

    box = column.box().column()
    box.prop(prefs, 'use_autosave')
    col = box.column()
    col.enabled = prefs.use_autosave
    col.prop(prefs, 'autosave_interval')
    row = col.row(align=True)
    row.prop(prefs, 'autosave_format', text='')
    if prefs.autosave_format == 'CUSTOM':
        op = row.operator('preferences.addon_show', icon='PREFERENCES', text='')
        op.module = utils.common.module()

    column.separator()

    box = column.box().column()
    icon = 'CHECKBOX_HLT' if bpy.data.use_autopack else 'CHECKBOX_DEHLT'
    box.operator('file.autopack_toggle', text='Toggle Autopack', icon=icon)
    box.operator('powersave.purge_orphans', text='Purge Orphans')

    column.separator()
    box = column.box().column()
    box.prop(filepaths, 'use_auto_save_temporary_files')
    col = box.column()
    col.enabled = filepaths.use_auto_save_temporary_files
    col.prop(filepaths, 'auto_save_time')
    box.prop(filepaths, 'save_version')


def powerlink_draw(self, column):
    wm = bpy.context.window_manager
    if hasattr(wm, 'powerlink'):
        wm.powerlink.draw(self, column)

    else:
        box = column.box().column()
        box.label(text='Check out PowerLink!')

        url = 'https://gumroad.com/l/powerlink'
        utils.ui.draw_op(box, 'Gumroad', 'wm.url_open', {'url': url})

        url = 'https://blendermarket.com/products/powerlink'
        utils.ui.draw_op(box, 'BlenderMarket', 'wm.url_open', {'url': url})


def powerbackup_draw(self, column):
    wm = bpy.context.window_manager
    if hasattr(wm, 'powerbackup'):
        wm.powerbackup.draw(self, column)

    else:
        box = column.box().column()
        box.label(text='Check out PowerBackup!')

        url = 'https://gumroad.com/l/powerbackup'
        utils.ui.draw_op(box, 'Gumroad', 'wm.url_open', {'url': url})

        url = 'https://blendermarket.com/products/powerbackup'
        utils.ui.draw_op(box, 'BlenderMarket', 'wm.url_open', {'url': url})


def powermanage_draw(column):
    wm = bpy.context.window_manager
    if hasattr(wm, 'powermanage'):
        wm.powermanage.draw_panel(column)

    else:
        box = column.box().column()
        box.label(text='Check out PowerManage!')

        url = 'https://gumroad.com/l/powermanage'
        utils.ui.draw_op(box, 'Gumroad', 'wm.url_open', {'url': url})

        url = 'https://blendermarket.com/products/powermanage'
        utils.ui.draw_op(box, 'BlenderMarket', 'wm.url_open', {'url': url})
