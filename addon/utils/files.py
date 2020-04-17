import bpy
import pathlib
import sys
import subprocess


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
        bpy.ops.wm.url_open(url=pathlib.Path(bpy.data.filepath).parent.as_uri())
    except:
        return ({'ERROR'}, 'Failed to open project folder', {'CANCELLED'})

    return ({'INFO'}, 'Opened project folder', {'FINISHED'})
