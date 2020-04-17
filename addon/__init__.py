from . import props
from . import icons
from . import ops
from . import timers
from . import handlers
from . import ui


def register():
    props.register()
    icons.register()
    ops.register()
    timers.register()
    handlers.register()
    ui.register()


def unregister():
    ui.unregister()
    handlers.unregister()
    timers.unregister()
    ops.unregister()
    icons.unregister()
    props.unregister()
