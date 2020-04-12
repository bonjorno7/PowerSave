import bpy
from .. import utils


class PowerSavePrefs(bpy.types.AddonPreferences):
    bl_idname = utils.common.module_name

    base_folder: bpy.props.StringProperty(
        name="Base Folder",
        description="The directory where initial saves will be stored",
        default=utils.common.get_default_folder(),
        subtype='FILE_PATH',
    )

    autosave_interval: bpy.props.IntProperty(
        name="Autosave Interval",
        description="The amount of minutes between each autosave",
        default=2,
        min=1,
        max=60,
    )

    save_on_startup: bpy.props.BoolProperty(
        name="Save on Startup",
        description="Whether to save new projects in your base folder automatically",
        default=True,
    )

    datetime_format: bpy.props.StringProperty(
        name="Datetime Format",
        description=utils.common.description(
            "The formatting string used to create file names",
            "%Y = year    %m = month    %d = day",
            "%H = hour    %M = minute    %S = second",
        ),
        default="%Y-%m-%d__%H-%M-%S__01.blend",
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Test", icon_value=utils.ui.get_icon())
        layout.prop(self, "base_folder")
        layout.prop(self, "autosave_interval")
        layout.prop(self, "save_on_startup")
        layout.prop(self, "datetime_format")
