import bpy
import random


addon_name = __name__.partition('.')[0]


def get_prefs():
    return bpy.context.preferences.addons[addon_name].preferences


def randint():
    return random.randint(1, 10)
