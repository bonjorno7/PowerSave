import bpy
import datetime
import re


module_name = __name__.partition('.')[0]


def get_prefs():
    return bpy.context.preferences.addons[module_name].preferences


def description(*args):
    return ".\n".join(args)


def get_datetime():
    string = get_prefs().datetime_format
    return datetime.datetime.now().strftime(string)


def get_increment():
    string = get_prefs().increment_format
    numbers = re.findall(r"\d+", string)
    return string if numbers else f"{string}1"


def get_filename():
    return f"{get_datetime()}{get_increment()}"
