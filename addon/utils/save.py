import bpy
import pathlib
import string
import re
from .. import utils


def increment_until_unique(path: pathlib.Path):
    while path.is_file():
        numbers = re.findall(r"\d+", str(path.stem))

        if numbers:
            path = str(path)
            last = numbers[-1]

            index = path.rfind(last)
            length = len(last)
            number = str(int(last) + 1)

            start = index + max(length - len(number), 0)
            end = index + length

            path = f"{path[:start]}{number}{path[end:]}"
            path = pathlib.Path(path)

        else:
            name = f"{path.stem}{utils.common.get_increment()}.blend"
            path = path.parent.joinpath(name)

    return path


def sanitize_path(path: pathlib.Path):
    valid = f"-_.() {string.ascii_letters}{string.digits}"
    name = "".join(c if c in valid else "_" for c in path.name)
    return path.parent.resolve().joinpath(name)


def powersave():
    prefs = utils.common.get_prefs()

    if bpy.data.filepath:
        path = bpy.data.filepath
    else:
        path = prefs.base_folder

    if prefs.powersave_name:
        name = prefs.powersave_name
    else:
        name = utils.common.get_datetime_increment()

    if path:
        name = f'{name.replace(".blend", "")}.blend'
        path = pathlib.Path(path).joinpath(name)
        path = increment_until_unique(path)
        path = sanitize_path(path)

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            bpy.ops.wm.save_mainfile(filepath=str(path))
            utils.files.add_to_recent_files()

        except:
            return ({'ERROR'}, f'Failed to save "{path.name}"', {'CANCELLED'})

        return ({'INFO'}, f'Saved "{path.name}"', {'FINISHED'})

    return ({'WARNING'}, "No base folder set", {'CANCELLED'})
