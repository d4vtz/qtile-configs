from libqtile import hook

from groups import groups
from keys import keys
from layouts import floating_layout, layouts
from mouse import mouse
from screens import screens
from settings import (
    auto_fullscreen,
    bring_front_click,
    cursor_warp,
    dgroups_app_rules,
    dgroups_key_binder,
    focus_on_window_activation,
    follow_mouse_focus,
    reconfigure_screens,
    wmname,
)

__all__ = [
    "keys",
    "groups",
    "layouts",
    "floating_layout",
    "screens",
    "mouse",
    "dgroups_key_binder",
    "dgroups_app_rules",
    "follow_mouse_focus",
    "bring_front_click",
    "cursor_warp",
    "floating_layout",
    "auto_fullscreen",
    "focus_on_window_activation",
    "reconfigure_screens",
    "wmname",
]


@hook.subscribe.startup_once
def _startup_once() -> None:
    """Reserved for session services that should start once per login.

    Keep this intentionally empty for the minimal base. Later we can move
    session services to systemd user units instead of spawning them here.
    """
    pass
