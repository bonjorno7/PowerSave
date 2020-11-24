import bpy
import pathlib
import sys
import subprocess
import re
from .. import utils


def get_default_folder():
    return str(pathlib.Path.home().joinpath('PowerSave'))


def add_to_recent_files():
    try:
        with open(bpy.utils.user_resource('CONFIG', 'recent-files.txt'), 'r+') as recent_files:
            lines = [bpy.data.filepath]

            for line in recent_files:
                line = line.rstrip('\r\n')

                if line != bpy.data.filepath:
                    lines.append(line)

            content = '\n'.join(lines)

            recent_files.seek(0, 0)
            recent_files.write(content)

    except:
        print('Failed to add to recent files')


def open_project_folder():
    if not bpy.data.is_saved:
        return ({'WARNING'}, 'Unsaved file', {'CANCELLED'})

    try:
        bpy.ops.wm.path_open(filepath=str(pathlib.Path(bpy.data.filepath).parent))
    except:
        return ({'ERROR'}, 'Failed to open project folder', {'CANCELLED'})

    return ({'INFO'}, 'Opened project folder', {'FINISHED'})


def as_path(path: str):
    return pathlib.Path(path).resolve()


def with_autosave(path: pathlib.Path):
    stem = f'{path.stem}_autosave'
    return path.with_name(f'{stem}{path.suffix}')


def change_version(path: pathlib.Path, direction: int):
    stem = path.stem
    numbers = re.findall(r'\d+', stem)

    if numbers:
        last = numbers[-1]
        length = len(last)
        number = str(int(last) + direction)

        index = stem.rfind(last)
        start = index + max(length - len(number), 0)
        end = index + length

        name = f'{stem[:start]}{number}{stem[end:]}.blend'
        path = path.with_name(name)

    else:
        name = f'{stem}{utils.common.increment()}.blend'
        path = path.with_name(name)

    return path
