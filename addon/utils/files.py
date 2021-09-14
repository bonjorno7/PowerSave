import bpy
import pathlib
import re
import typing
from .. import utils


def get_default_folder() -> str:
    return str(utils.common.documents().joinpath('PowerSave'))


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


def open_project_folder() -> typing.Tuple[set, str, set]:
    if not bpy.data.is_saved:
        return ({'WARNING'}, 'Unsaved file', {'CANCELLED'})

    try:
        bpy.ops.wm.path_open(filepath=str(pathlib.Path(bpy.data.filepath).parent))
    except:
        return ({'ERROR'}, 'Failed to open project folder', {'CANCELLED'})

    return ({'INFO'}, 'Opened project folder', {'FINISHED'})


def as_path(path: str) -> pathlib.Path:
    return pathlib.Path(path).resolve()


def as_autosave(path: pathlib.Path, mkdir: bool = False) -> pathlib.Path:
    prefs = utils.common.prefs()
    folder = as_path(bpy.path.abspath(prefs.autosave_folder))

    if mkdir:
        try:
            folder.mkdir(parents=True, exist_ok=True)
        except:
            print(f'Unable to create autosave folder "{folder}"')
            return path

    return folder.joinpath(path.name)


def sanitize_autosave_folder(self, context):
    if not self.autosave_folder:
        self['autosave_folder'] = '//'

    elif not self.autosave_folder.startswith('//'):
        autosave_folder = as_path(self.autosave_folder)

        if autosave_folder.is_absolute():
            self['autosave_folder'] = str(autosave_folder)
        else:
            self['autosave_folder'] = f'//{autosave_folder}'

 
def change_version(path: pathlib.Path, direction: int) -> pathlib.Path:
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
