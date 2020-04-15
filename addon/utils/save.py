import bpy
import pathlib
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


def save_datetime():
    if not bpy.data.is_saved:
        prefs = utils.common.get_prefs()

        if prefs.base_folder:
            name = f"{utils.common.get_datetime_increment()}.blend"
            path = pathlib.Path(prefs.base_folder).joinpath(name)
            path = increment_until_unique(path.resolve())

            try:
                path.parent.mkdir(parents=True, exist_ok=True)
                bpy.ops.wm.save_mainfile(filepath=str(path))
                utils.files.add_to_recent_files()

            except:
                return ({'ERROR'}, f'Failed to save "{path.name}"', {'CANCELLED'})

            return ({'INFO'}, f'Saved "{path.name}"', {'FINISHED'})

        return ({'WARNING'}, "No base folder set", {'CANCELLED'})

    return ({'WARNING'}, "File is already saved", {'CANCELLED'})


def save_incremental():
    if bpy.data.is_saved:
        path = pathlib.Path(bpy.data.filepath)
        path = increment_until_unique(path.resolve())

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            bpy.ops.wm.save_mainfile(filepath=str(path))
            utils.files.add_to_recent_files()

        except:
            return ({'ERROR'}, f'Failed to save "{path.name}"', {'CANCELLED'})

        return ({'INFO'}, f'Saved "{path.name}"', {'FINISHED'})

    return ({'WARNING'}, "Unsaved file", {'CANCELLED'})
