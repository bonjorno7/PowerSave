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
            recent_files.write('\n'.join(lines))

        bpy.ops.wm.read_history()

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
        return path.with_name(f'{path.stem}_autosave.blend')

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


def increment_version(path: pathlib.Path) -> pathlib.Path:
    stem = path.stem
    increment = utils.common.increment()

    if utils.common.prefs().increment_strict:
        separator = re.sub(r'\d+$', '', increment)
        match = re.search(fr'(?<={separator})\d+$', stem)
    else:
        match = re.search(r'\d+$', stem)

    if match:
        stem = stem[:match.start()]
        number = str(int(match.group()) + 1)
        digits = len(match.group())
        increment = number.zfill(digits)

    return path.with_name(f'{stem}{increment}.blend')


def find_version(path: pathlib.Path, direction: int) -> typing.Union[pathlib.Path, None]:
    stem = path.stem
    match = re.search(r'\d+$', stem)

    if match:
        stem = stem[:match.start()]
        number = str(int(match.group()) + direction)
        digits = len(match.group())

        for zeros in range(max(1, digits - 1), digits + 2):
            increment = number.zfill(zeros)
            path = path.with_name(f'{stem}{increment}.blend')

            if path.is_file():
                return path

    return None
