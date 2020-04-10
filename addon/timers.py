import bpy
from . import utils


def autosave_timer():
    prefs = utils.get_prefs()

    print("AUTO SAVING")

    return prefs.autosave_interval * 60
