import bpy
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
    def prefs(self):
        return utils.common.prefs()

    @staticmethod
    def draw(self, column):
        powersave_draw(self, column)

    def powersave(self):
        return utils.save.powersave()
