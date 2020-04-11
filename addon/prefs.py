import bpy
from . import utils


class PowerSavePrefs(bpy.types.AddonPreferences):
    bl_idname = utils.addon_name

    base_folder: bpy.props.StringProperty(
        name="Base Folder",
        subtype='FILE_PATH',
    )

    autosave_interval: bpy.props.IntProperty(
        name="Autosave Interval",
        default=5,
        min=1,
        max=60,
    )

    save_on_startup: bpy.props.BoolProperty(
        name="Save on Startup",
        default=True,
    )

    datetime_format: bpy.props.StringProperty(
        name="Datetime Format",
        default="%Y-%m/%m-%d__%H-%M__01.blend",
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "base_folder")
        layout.prop(self, "autosave_interval")
        layout.prop(self, "save_on_startup")
        layout.prop(self, "datetime_format")


def register():
    try:
        bpy.utils.register_class(PowerSavePrefs)
    except:
        pass


def unregister():
    try:
        bpy.utils.unregister_class(PowerSavePrefs)
    except:
        pass
