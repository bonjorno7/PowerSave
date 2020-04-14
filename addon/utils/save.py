import bpy
import pathlib
from .. import utils


def save_datetime():
    if not bpy.data.is_saved:
        prefs = utils.common.get_prefs()

        if prefs.base_folder:
            name = f"{utils.common.get_datetime(prefs.datetime_format)}.blend"
            path = pathlib.Path(prefs.base_folder).joinpath(name).resolve()

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
        prefs = utils.common.get_prefs()

        path = pathlib.Path(bpy.data.filepath).resolve()
        path = path.parent.joinpath(path.stem + "_01.blend")

        try:
            bpy.ops.wm.save_mainfile(filepath=str(path))
            utils.files.add_to_recent_files()
        
        except:
            return ({'ERROR'}, f'Failed to save "{path.name}"', {'CANCELLED'})

        return ({'INFO'}, f'Saved "{path.name}"', {'FINISHED'})

    return ({'WARNING'}, "Unsaved file", {'CANCELLED'})
