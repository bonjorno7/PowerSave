import bpy
import pathlib
import re
from .. import utils


def sanitize_path(path: pathlib.Path):
    drive = pathlib.Path(path.drive)
    path = str(path)[len(path.drive):]
    path = utils.common.sanitize(path)
    return drive.joinpath(path).resolve()


def increment_until_unique(path: pathlib.Path):
    while path.is_file():
        stem = path.stem
        numbers = re.findall(r'\d+', stem)

        if numbers:
            last = numbers[-1]
            length = len(last)
            number = str(int(last) + 1)

            index = stem.rfind(last)
            start = index + max(length - len(number), 0)
            end = index + length

            name = f'{stem[:start]}{number}{stem[end:]}.blend'
            path = path.with_name(name)

        else:
            name = f'{stem}{utils.common.increment()}.blend'
            path = path.with_name(name)

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


def should_load_autosave():
    current_path = utils.files.as_path(bpy.data.filepath)
    autosave_path = utils.files.with_autosave(current_path)

    current_exists = current_path.is_file()
    autosave_exists = autosave_path.is_file()
    is_autosave = current_path.stem.endswith('_autosave')

    if current_exists and autosave_exists and not is_autosave:
        current_time = current_path.stat().st_mtime_ns
        autosave_time = autosave_path.stat().st_mtime_ns
        return autosave_time > current_time


def load_autosave():
    current_path = utils.files.as_path(bpy.data.filepath)
    autosave_path = utils.files.with_autosave(current_path)

    try:
        bpy.ops.wm.open_mainfile(filepath=str(autosave_path))
    except:
        return ({'ERROR'}, f'Failed to load "{autosave_path.name}"', {'CANCELLED'})

    new_path = increment_until_unique(current_path)

    try:
        bpy.ops.wm.save_as_mainfile(filepath=str(new_path))
        utils.files.add_to_recent_files()
    except:
        return ({'ERROR'}, f'Failed to save "{new_path.name}"', {'CANCELLED'})

    return ({'INFO'}, f'Loaded "{autosave_path.name}" as "{new_path.name}"', {'FINISHED'})
