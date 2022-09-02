import bpy
import datetime
import re
import pathlib
import platform
import typing
from .. import props
from .. import ui


def module() -> str:
    return props.addon.name


def prefs() -> bpy.types.AddonPreferences:
    return bpy.context.preferences.addons[module()].preferences


def description(*args) -> str:
    return '.\n'.join(args)


def sanitize(text: str) -> str:
    return ''.join('_' if c in ':*?"<>|' else c for c in text)


def date_time() -> str:
    form = prefs().date_time_format
    form = datetime.datetime.now().strftime(form)
    return sanitize(form)


def increment() -> str:
    form = sanitize(prefs().increment_format)
    match = re.search(r'\d+$', form)

    if match:
        number = '1'.zfill(len(match.group()))
        return re.sub(r'\d+$', number, form)
    else:
        return f'{form}1'


def date_time_increment() -> str:
    return f'{date_time()}{increment()}'


def update_powersave_name():
    name = pathlib.Path(bpy.data.filepath).stem
    prefs().powersave_name = name


def update_panel_category(self, context):
    category = prefs().panel_category
    ui.main_panel.PowerSavePanel.bl_category = category
    ui.main_panel.PowerSavePanel.bl_region_type = 'UI' if category else 'HEADER'
    bpy.utils.unregister_class(ui.main_panel.PowerSavePanel)
    bpy.utils.register_class(ui.main_panel.PowerSavePanel)


def context_override(
    context: bpy.types.Context,
    override: dict,
    operator: typing.Callable,
    arguments: dict = None,
    execution: str = 'EXEC_DEFAULT',
) -> typing.Set[str]:
    override = dict(context.copy(), **override)

    if arguments is None:
        arguments = {}

    if hasattr(context, 'temp_override'):
        with context.temp_override(**override):
            return operator(execution, **arguments)

    return operator(override, execution, **arguments)


def documents() -> pathlib.Path:
    if platform.system() == 'Windows':
        import ctypes.wintypes
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 1, buf)
        return pathlib.Path(buf.value)
    else:
        return pathlib.Path.home()
