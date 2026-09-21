"""Behaviour that applies to the compositor as a whole."""

dgroups_key_binder = None
dgroups_app_rules = []

follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = False

auto_fullscreen = True
auto_minimize = False
focus_on_window_activation = "smart"
reconfigure_screens = True
screen_change_debounce_timeout = 1

# Java toolkits still inspect this value.
wmname = "LG3D"
