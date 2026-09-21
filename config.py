"""Qtile entry point.

Keep this file intentionally small. The actual configuration lives in the
qtile_config package so components can evolve independently.
"""
from libqtile import hook

from qtile_config.groups import groups
from qtile_config.input import wl_input_rules
from qtile_config.keys import keys
from qtile_config.layouts import floating_layout, layouts
from qtile_config.mouse import mouse
from qtile_config.screens import extension_defaults, screens, widget_defaults
from qtile_config.settings import (
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
    "keys", "groups", "layouts", "floating_layout", "screens", "mouse",
    "widget_defaults", "extension_defaults", "wl_input_rules",
    "dgroups_key_binder", "dgroups_app_rules", "follow_mouse_focus",
    "bring_front_click", "cursor_warp", "auto_fullscreen",
    "focus_on_window_activation", "reconfigure_screens", "wmname",
]


@hook.subscribe.startup_once
def _startup_once() -> None:
    """Session services will later be managed by systemd --user."""
    pass
