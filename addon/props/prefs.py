import bpy
from .. import utils


class PowerSavePrefs(bpy.types.AddonPreferences):
    bl_idname = utils.common.module()

    base_folder: bpy.props.StringProperty(
        name='Base Folder',
        description='The directory where initial saves will be stored',
        default=utils.files.get_default_folder(),
        subtype='FILE_PATH',
    )

    use_autosave: bpy.props.BoolProperty(
        name='Use Autosave',
        description='Whether to periodically save the file',
        default=True,
    )

    autosave_interval: bpy.props.IntProperty(
        name='Autosave Interval',
        description='The amount of minutes between each autosave',
        default=2,
        min=1,
        max=60,
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

    high_contrast_icons: bpy.props.BoolProperty(
        name='High Contrast Icons',
        description='Whether to use the high contrast set of icons',
        default=False,
    )

    powersave_name: bpy.props.StringProperty(
        name='PowerSave Name',
        description='The name to use for PowerSave',
        default='',
    )


    def draw(self, context):
        layout = self.layout

        utils.ui.draw_prop(layout, 'Base Folder', self, 'base_folder')
        utils.ui.draw_prop(layout, 'Use Autosave', self, 'use_autosave')
        utils.ui.draw_prop(layout, 'Autosave Interval', self, 'autosave_interval')
        utils.ui.draw_bool(layout, 'Save On Startup', self, 'save_on_startup')
        utils.ui.draw_prop(layout, 'Date Time Format', self, 'date_time_format')
        utils.ui.draw_prop(layout, 'Increment Format', self, 'increment_format')
        utils.ui.draw_prop(layout, 'High Contrast Icons', self, 'high_contrast_icons')

        url = 'https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes'
        utils.ui.draw_op(layout, 'Date Time Documentation', 'wm.url_open', {'url': url})
