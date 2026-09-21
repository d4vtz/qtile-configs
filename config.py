"""Qtile entry point for the desktop environment.

Qtile requires these names at module scope. Implementation lives under the
desktop.qtile package so this file stays a thin adapter.
"""

from desktop.qtile.core.groups import groups
from desktop.qtile.core.input import wl_input_rules, wl_xcursor_size, wl_xcursor_theme
from desktop.qtile.core.keys import keys
from desktop.qtile.core.mouse import mouse
from desktop.qtile.core.screens import extension_defaults, screens, widget_defaults
from desktop.qtile.core.settings import (
    auto_fullscreen,
    auto_minimize,
    bring_front_click,
    cursor_warp,
    dgroups_app_rules,
    dgroups_key_binder,
    focus_on_window_activation,
    follow_mouse_focus,
    reconfigure_screens,
    screen_change_debounce_timeout,
    wmname,
)
from desktop.qtile.layouts import floating_layout, layouts
from desktop.qtile.core import hooks as _hooks

__all__ = [
    "keys", "groups", "layouts", "floating_layout", "screens", "mouse",
    "widget_defaults", "extension_defaults", "wl_input_rules",
    "wl_xcursor_theme", "wl_xcursor_size", "dgroups_key_binder",
    "dgroups_app_rules", "follow_mouse_focus", "bring_front_click",
    "cursor_warp", "auto_fullscreen", "auto_minimize",
    "focus_on_window_activation", "reconfigure_screens",
    "screen_change_debounce_timeout", "wmname",
]
