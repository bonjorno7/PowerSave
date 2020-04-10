import bpy
from . import utils


def autosave_timer():
    prefs = utils.get_prefs()
    randint = utils.randint()
    prefs.autosave_interval = randint
    return 1.0
