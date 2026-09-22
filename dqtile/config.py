"""Compose the complete dqtile configuration."""

from collections.abc import Callable
from libqtile.config import Output, Screen
from .core.groups import groups
from .core.input import wl_input_rules, wl_xcursor_size, wl_xcursor_theme
from .core.keys import keys
from .core.mouse import mouse
from .core.settings import auto_fullscreen, auto_minimize, bring_front_click, cursor_warp, dgroups_app_rules, dgroups_key_binder, focus_on_window_activation, follow_mouse_focus, reconfigure_screens, screen_change_debounce_timeout, wmname
from .layouts import floating_layout, layouts
from .ui.screens import extension_defaults, screens, widget_defaults
from .core import hooks as _hooks

fake_screens: list[Screen] | None = None
generate_screens: Callable[[list[Output]], list[Screen]] | None = None

__all__ = ["keys", "groups", "layouts", "floating_layout", "screens", "mouse", "widget_defaults", "extension_defaults", "fake_screens", "generate_screens", "wl_input_rules", "wl_xcursor_theme", "wl_xcursor_size", "dgroups_key_binder", "dgroups_app_rules", "follow_mouse_focus", "bring_front_click", "cursor_warp", "auto_fullscreen", "auto_minimize", "focus_on_window_activation", "reconfigure_screens", "screen_change_debounce_timeout", "wmname"]
