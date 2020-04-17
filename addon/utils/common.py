import bpy
import string
import datetime
import re
import pathlib
from .. import props
from ... import bl_info


def module():
    return props.addon.name


def prefs():
    return bpy.context.preferences.addons[module()].preferences


def version():
    return ''.join(str(n) for n in bl_info['version'])


def description(*args):
    return '.\n'.join(args)


def sanitize(text: str):
    valid = f'-_.()/\\ {string.ascii_letters}{string.digits}'
    return ''.join(c if c in valid else '_' for c in text)


def date_time():
    form = prefs().date_time_format
    form = datetime.datetime.now().strftime(form)
    return sanitize(form)


def increment():
    form = sanitize(prefs().increment_format)
    numbers = re.findall(r'\d+', form)
    return form if numbers else f'{form}1'


def date_time_increment():
    return f'{date_time()}{increment()}'


def update_powersave_name():
    name = pathlib.Path(bpy.data.filepath).stem
    prefs().powersave_name = name
