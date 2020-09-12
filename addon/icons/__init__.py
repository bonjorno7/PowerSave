import bpy
import bpy.utils.previews
import pathlib


pcoll = None


def id(identifier):
    global pcoll
    return pcoll[identifier].icon_id


def register():
    global pcoll
    pcoll = bpy.utils.previews.new()

    directory = pathlib.Path(__file__).parent

    for filepath in directory.glob('*.png'):
        pcoll.load(filepath.stem, str(filepath), 'IMAGE')


def unregister():
    global pcoll
    bpy.utils.previews.remove(pcoll)
