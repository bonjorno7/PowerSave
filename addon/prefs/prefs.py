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
            "Read the datetime documentation for details",
        ),
        default="%Y-%m-%d__%H-%M-%S__01.blend",
    )

    def draw(self, context):
        layout = self.layout
        utils.ui.draw_prop(layout, "Base Folder", self, "base_folder")
        utils.ui.draw_prop(layout, "Autosave Interval", self, "autosave_interval")
        utils.ui.draw_bool(layout, "Save On Startup", self, "save_on_startup")
        utils.ui.draw_prop(layout, "Datetime Format", self, "datetime_format")

        url = "https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes"
        utils.ui.draw_op(layout, "Datetime Documentation", "wm.url_open", {"url": url})
