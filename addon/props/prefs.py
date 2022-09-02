import bpy
import typing
from .. import icons
from .. import utils


def panel_tab_items(self, context) -> typing.List[typing.Tuple[str, str, str, bpy.types.ImagePreview, int]]:
    powersave = ('POWERSAVE', 'PowerSave', '', icons.id('powersave'), 0)
    powerlink = ('POWERLINK', 'PowerLink', '', icons.id('powerlink'), 1)
    powerbackup = ('POWERBACKUP', 'PowerBackup', '', icons.id('powerbackup'), 2)
    powermanage = ('POWERMANAGE', 'PowerManage', '', icons.id('powermanage'), 3)
    return [powersave, powerlink, powerbackup, powermanage]


class PowerSavePrefs(bpy.types.AddonPreferences):
    bl_idname = utils.common.module()

    base_folder: bpy.props.StringProperty(
        name='Base Folder',
        description='The directory where initial saves will be stored',
        default=utils.files.get_default_folder(),
        subtype='DIR_PATH',
    )

    use_autosave: bpy.props.BoolProperty(
        name='Use Autosave',
        description='Whether to periodically save the file',
        default=False,
    )

    autosave_interval: bpy.props.IntProperty(
        name='Autosave Interval',
        description='The amount of minutes between each autosave',
        default=2,
        min=1,
        max=60,
    )

    autosave_format: bpy.props.EnumProperty(
        name='Autosave Format',
        items=[
            ('OVERWRITE', 'Autosave Overwrite', 'Autosave over the original file'),
            ('EXTENSION', 'Autosave Extension', 'Autosave with the ".blend.autosave" extension'),
            ('SUFFIX', 'Autosave Suffix', 'Autosave with the "_autosave" suffix'),
            ('FOLDER', 'Autosave Folder', 'Autosave in the "autosave" subfolder'),
            ('CUSTOM', 'Autosave Custom', 'Autosave with a custom folder and file name'),
        ],
        default='OVERWRITE',
    )

    autosave_folder: bpy.props.StringProperty(
        name='Autosave Folder',
        description='Supports relative paths starting with two forward slashes',
        default='//',
        subtype='DIR_PATH',
        update=utils.files.sanitize_autosave_folder,
    )

    autosave_name: bpy.props.StringProperty(
        name='Autosave Name',
        description='{name} is replaced with the file name without extension',
        default='{name}.blend',
        update=utils.files.sanitize_autosave_name,
    )

    autosave_external_text: bpy.props.BoolProperty(
        name='Autosave External Text',
        description='Autosave external text files you have open in Blender',
        default=False,
    )

    save_on_startup: bpy.props.BoolProperty(
        name='Save on Startup',
        description='Whether to save new projects in your base folder automatically',
        default=False,
    )

    date_time_format: bpy.props.StringProperty(
        name='Date Time Format',
        description=utils.common.description(
            'The formatting string used to create file names',
            'Read the datetime documentation for details',
        ),
        default='%A_%d-%B-%Y_%H.%M',
    )

    increment_format: bpy.props.StringProperty(
        name='Increment Format',
        description='What characters to put before the increment number and how many zeroes to pad it with',
        default='_01',
    )

    increment_strict: bpy.props.BoolProperty(
        name='Increment Strict',
        description='Only recognize version numbers prefixed the same way as your Increment Format',
        default=False,
    )

    icon_preset: bpy.props.EnumProperty(
        name='Icon Preset',
        description='Which set of icons to use for the 3D view button',
        items=[
            ('DEFAULT', 'Default', 'Green - Gray - Red'),
            ('TRAFFIC', 'Traffic Light', 'Green - Yellow - Red'),
            ('CONTRAST', 'High Contrast', 'White - Mixed - Black'),
        ],
    )

    powersave_name: bpy.props.StringProperty(
        name='PowerSave Name',
        description='The name to use for PowerSave',
        default='',
        options={'SKIP_SAVE'},
    )

    panel_tab: bpy.props.EnumProperty(
        name='Panel Tab',
        description='Which tab is currently active in the popover',
        items=panel_tab_items,
        options={'SKIP_SAVE'},
    )

    popover_width: bpy.props.FloatProperty(
        name='Popover Width',
        description='How wide the popover panel should be, in blender UI units',
        default=10,
        min=1,
        max=20,
    )

    panel_category: bpy.props.StringProperty(
        name='Panel Category',
        description='What category to show the PowerSave panel in, leave empty to hide it entirely',
        default='PowerSave',
        update=utils.common.update_panel_category,
    )

    def draw(self, context):
        layout = self.layout

        utils.ui.draw_prop(layout, 'Base Folder', self, 'base_folder')
        utils.ui.draw_bool(layout, 'Use Autosave', self, 'use_autosave')

        col = layout.column()
        col.enabled = self.use_autosave
        utils.ui.draw_prop(col, 'Autosave Interval', self, 'autosave_interval')

        col = layout.column()
        col.enabled = self.use_autosave
        utils.ui.draw_prop(col, 'Autosave Format', self, 'autosave_format')

        col = layout.column()
        col.enabled = self.use_autosave and self.autosave_format == 'CUSTOM'
        utils.ui.draw_prop(col, 'Autosave Folder', self, 'autosave_folder')

        col = layout.column()
        col.enabled = self.use_autosave and self.autosave_format == 'CUSTOM'
        utils.ui.draw_prop(col, 'Autosave Name', self, 'autosave_name')

        col = layout.column()
        col.enabled = self.use_autosave
        utils.ui.draw_bool(col, 'Autosave External Text', self, 'autosave_external_text')

        utils.ui.draw_bool(layout, 'Save On Startup', self, 'save_on_startup')
        utils.ui.draw_prop(layout, 'Date Time Format', self, 'date_time_format')
        utils.ui.draw_prop(layout, 'Increment Format', self, 'increment_format')
        utils.ui.draw_bool(layout, 'Increment Strict', self, 'increment_strict')
        utils.ui.draw_prop(layout, 'Icon Preset', self, 'icon_preset')
        utils.ui.draw_prop(layout, 'Popover Width', self, 'popover_width')
        utils.ui.draw_prop(layout, 'Panel Category', self, 'panel_category')

        url = 'https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes'
        utils.ui.draw_op(layout, 'Date Time Documentation', 'wm.url_open', {'url': url})
