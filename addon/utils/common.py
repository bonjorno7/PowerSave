import bpy
import datetime
import re
from ... import bl_info


module_name = __name__.partition('.')[0]


def get_prefs():
    return bpy.context.preferences.addons[module_name].preferences


def get_version():
    return "".join(str(n) for n in bl_info["version"])


def description(*args):
    return ".\n".join(args)


def get_datetime():
    form = get_prefs().datetime_format
    return datetime.datetime.now().strftime(form)


def get_increment():
    form = get_prefs().increment_format
    numbers = re.findall(r"\d+", form)
    return form if numbers else f"{form}1"


def get_datetime_increment():
    return f"{get_datetime()}{get_increment()}"
