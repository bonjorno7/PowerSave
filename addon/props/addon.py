import bpy
from .. import utils


name = __name__.partition('.')[0]


class PowerSaveProps(bpy.types.PropertyGroup):
    addon: bpy.props.StringProperty(
        name='Addon',
        description='The PowerSave module',
        default=name,
    )

    def prefs(self):
        return utils.common.prefs()
