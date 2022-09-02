import bpy
from .. import utils
from .. import icons


icon_presets = {
    'DEFAULT': {'saved': 'green', 'dirty': 'gray', 'unsaved': 'red'},
    'TRAFFIC': {'saved': 'green', 'dirty': 'yellow', 'unsaved': 'red'},
    'CONTRAST': {'saved': 'white', 'dirty': 'mixed', 'unsaved': 'black'},
}


def get_icon() -> bpy.types.ImagePreview:
    icon_dict = icon_presets[utils.common.prefs().icon_preset]

    if bpy.data.is_saved:
        if bpy.data.is_dirty:
            icon = icon_dict['dirty']
        else:
            icon = icon_dict['saved']
    else:
        icon = icon_dict['unsaved']

    return icons.id(icon)


def tag_redraw():
    for window in bpy.context.window_manager.windows.values():
        for area in window.screen.areas.values():
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
