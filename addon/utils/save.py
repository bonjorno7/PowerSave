import bpy
import pathlib
import datetime
import typing
from .. import utils


def sanitize_path(path: pathlib.Path) -> pathlib.Path:
    drive = pathlib.Path(path.drive)
    path = str(path)[len(path.drive):]
    path = utils.common.sanitize(path)
    return drive.joinpath(path).resolve()


def increment_until_unique(path: pathlib.Path) -> pathlib.Path:
    while path.is_file():
        path = utils.files.increment_version(path)

    return path


def powersave() -> typing.Tuple[set, str, set]:
    prefs = utils.common.prefs()

    if bpy.data.is_saved:
        path = pathlib.Path(bpy.data.filepath).parent
    else:
        path = pathlib.Path(prefs.base_folder)
        if prefs.use_subfolder:
            path = path.joinpath(datetime.datetime.now().strftime(prefs.subfolder_format))

    if bpy.data.is_saved and not prefs.powersave_name:
        utils.common.update_powersave_name()

    if prefs.powersave_name:
        name = prefs.powersave_name
    else:
        name = utils.common.date_time_increment()

    if path:
        name = f'{name.replace(".blend", "")}.blend'
        path = path.joinpath(name)
        path = sanitize_path(path)
        path = increment_until_unique(path)

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            bpy.ops.wm.save_as_mainfile(filepath=str(path))
            utils.files.add_to_recent_files()

        except:
            return ({'ERROR'}, f'Failed to PowerSave "{path.name}"', {'CANCELLED'})

        return ({'INFO'}, f'PowerSaved "{path.name}"', {'FINISHED'})

    return ({'WARNING'}, 'No PowerSave folder set', {'CANCELLED'})
