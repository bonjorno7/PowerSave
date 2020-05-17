import bpy
import pathlib
from .. import utils


def sanitize_path(path: pathlib.Path):
    drive = pathlib.Path(path.drive)
    path = str(path)[len(path.drive):]
    path = utils.common.sanitize(path)
    return drive.joinpath(path).resolve()


def increment_until_unique(path: pathlib.Path):
    while path.is_file():
        path = utils.files.change_version(path, 1)

    return path


def powersave():
    prefs = utils.common.prefs()

    if bpy.data.is_saved:
        path = pathlib.Path(bpy.data.filepath).parent
    else:
        path = pathlib.Path(prefs.base_folder)

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
