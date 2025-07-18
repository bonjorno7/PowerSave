import bpy
import typing
from .. import utils
from ..ui.main_panel import powersave_draw

name = __name__.partition('.')[0]


class PowerSaveProps(bpy.types.PropertyGroup):
    addon: bpy.props.StringProperty(
        name='Addon',
        description='The PowerSave module',
        default=name,
    )

    @property
    def prefs(self) -> bpy.types.AddonPreferences:
        return utils.common.prefs()

    @staticmethod
    def draw(self, column):
        powersave_draw(self, column)

    def powersave(self) -> typing.Tuple[set, str, set]:
        return utils.save.powersave()
