import bpy
import pathlib
import re
import traceback
import typing
from .. import utils


def get_default_folder() -> str:
    return str(utils.common.documents().joinpath('PowerSave'))


def add_to_recent_files():
    try:
        with open(bpy.utils.user_resource('CONFIG', path='recent-files.txt'), 'r+') as recent_files:
            lines = [bpy.data.filepath]

            for line in recent_files:
                line = line.rstrip('\r\n')

                if line != bpy.data.filepath:
                    lines.append(line)

            recent_files.seek(0, 0)
            recent_files.writelines(lines)

    except:
        traceback.print_exc()
        print('Failed to add to recent files')


def open_project_folder() -> typing.Tuple[set, str, set]:
    if not bpy.data.is_saved:
        return ({'WARNING'}, 'Unsaved file', {'CANCELLED'})

    try:
        bpy.ops.wm.path_open(filepath=str(pathlib.Path(bpy.data.filepath).parent))
    except:
        traceback.print_exc()
        return ({'ERROR'}, 'Failed to open project folder', {'CANCELLED'})

    return ({'INFO'}, 'Opened project folder', {'FINISHED'})


def as_path(path: str) -> pathlib.Path:
    return pathlib.Path(path).resolve()


def verify_folder(folder: pathlib.Path, mkdir: bool = False) -> bool:
    if mkdir:
        try:
            folder.mkdir(parents=True, exist_ok=True)
        except:
            traceback.print_exc()
            print(f'Unable to create autosave folder "{folder}"')

    return folder.is_dir()


def as_autosave(path: pathlib.Path, mkdir: bool = False) -> pathlib.Path:
    prefs = utils.common.prefs()

    if prefs.autosave_format == 'OVERWRITE':
        return path

    elif prefs.autosave_format == 'EXTENSION':
        return path.with_suffix('.blend.autosave')

    elif prefs.autosave_format == 'SUFFIX':
        return path.with_stem(f'{path.stem}_autosave')

    elif prefs.autosave_format == 'FOLDER':
        folder = path.parent.joinpath('autosave')

        if verify_folder(folder, mkdir):
            return folder.joinpath(path.name)
        else:
            return path

    elif prefs.autosave_format == 'CUSTOM':
        folder = as_path(bpy.path.abspath(prefs.autosave_folder))

        if verify_folder(folder, mkdir):
            return folder.joinpath(prefs.autosave_name.replace('{name}', path.stem))
        else:
            return path


def sanitize_autosave_folder(self, context: bpy.types.Context):
    if not self.autosave_folder:
        self['autosave_folder'] = '//'

    elif not self.autosave_folder.startswith('//'):
        autosave_folder = as_path(self.autosave_folder)

        if autosave_folder.is_absolute():
            self['autosave_folder'] = str(autosave_folder)
        else:
            self['autosave_folder'] = f'//{autosave_folder}'


def sanitize_autosave_name(self, context: bpy.types.Context):
    if not self.autosave_name:
        self['autosave_name'] = '{name}.blend'

    elif '/' in self.autosave_name or '\\' in self.autosave_name:
        index = max(self.autosave_name.rfind('/'), self.autosave_name.rfind('\\'))

        if index != -1:
            self['autosave_name'] = self.autosave_name[index + 1:]


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
