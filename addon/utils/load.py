import bpy
import pathlib
import typing
from .. import utils


def should_load_autosave() -> typing.Union[bool, None]:
    current_path = utils.files.as_path(bpy.data.filepath)
    autosave_path = utils.files.as_autosave(current_path)

    if current_path == autosave_path:
        return False

    if current_path.is_file() and autosave_path.is_file():
        current_time = current_path.stat().st_mtime_ns
        autosave_time = autosave_path.stat().st_mtime_ns
        return autosave_time > current_time


def load_autosave() -> typing.Tuple[set, str, set]:
    current_path = utils.files.as_path(bpy.data.filepath)
    autosave_path = utils.files.as_autosave(current_path)

    try:
        bpy.ops.wm.open_mainfile(filepath=str(autosave_path))
    except:
        return ({'ERROR'}, f'Failed to load "{autosave_path.name}"', {'CANCELLED'})

    new_path = utils.save.increment_until_unique(current_path)

    try:
        bpy.ops.wm.save_as_mainfile(filepath=str(new_path))
        utils.files.add_to_recent_files()
    except:
        return ({'ERROR'}, f'Failed to save "{new_path.name}"', {'CANCELLED'})

    return ({'INFO'}, f'Loaded "{autosave_path.name}" as "{new_path.name}"', {'FINISHED'})


def verify_version(direction) -> typing.Union[pathlib.Path, bool]:
    path = utils.files.as_path(bpy.data.filepath)

    if path.is_file():
        path = utils.files.change_version(path, direction)

        if path.is_file():
            return path

    return False


def load_version(direction) -> typing.Tuple[set, str, set]:
    path = verify_version(direction)

    if not path:
        return ({'ERROR'}, f'File version does not exist', {'CANCELLED'})

    if bpy.data.is_saved and bpy.data.is_dirty:
        try:
            bpy.ops.wm.save_mainfile(filepath=bpy.data.filepath)
        except:
            return ({'ERROR'}, f'Failed to save "{bpy.data.filepath}"', {'CANCELLED'})

    try:
        bpy.ops.wm.open_mainfile(filepath=str(path))
    except:
        return ({'ERROR'}, f'Failed to load "{path.name}"', {'CANCELLED'})

    return ({'INFO'}, f'Loaded "{path.name}"', {'FINISHED'})
