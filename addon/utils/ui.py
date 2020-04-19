import bpy
from .. import utils
from .. import icons


def get_icon():
    if utils.common.prefs().high_contrast_icons:
        if bpy.data.is_saved:
            if bpy.data.is_dirty:
                icon = 'mixed'
            else:
                icon = 'white'
        else:
            icon = 'black'

    else:
        if bpy.data.is_saved:
            if bpy.data.is_dirty:
                icon = 'gray'
            else:
                icon = 'green'
        else:
            icon = 'red'

    return icons.id(icon)


def tag_redraw():
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()


def draw_prop(layout, text, data, prop):
    row = layout.row()
    row.label(text=text)
    row.prop(data, prop, text='')


def draw_bool(layout, text, data, prop):
    row = layout.row()
    row.label(text=text)
    col = row.column()
    col.alignment = 'RIGHT'
    col.prop(data, prop, text='')


def draw_op(layout, text, operator, options):
    op = layout.operator(operator, text=text)
    for key, value in options.items():
        op[key] = value
