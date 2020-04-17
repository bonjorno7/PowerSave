import bpy
import string
import datetime
import re
import pathlib
from .. import props
from ... import bl_info


def get_module():
    return props.addon.name


def get_prefs():
    return bpy.context.preferences.addons[get_module()].preferences


def get_version():
    return "".join(str(n) for n in bl_info["version"])


def description(*args):
    return ".\n".join(args)


def sanitize(text: str):
    valid = f"-_.()/\\ {string.ascii_letters}{string.digits}"
    return "".join(c if c in valid else "_" for c in text)


def get_datetime():
    form = sanitize(get_prefs().datetime_format)
    return datetime.datetime.now().strftime(form)


def get_increment():
    form = sanitize(get_prefs().increment_format)
    numbers = re.findall(r"\d+", form)
    return form if numbers else f"{form}1"


def get_datetime_increment():
    return f"{get_datetime()}{get_increment()}"


def update_powersave_name():
    name = pathlib.Path(bpy.data.filepath).stem
    get_prefs().powersave_name = name
