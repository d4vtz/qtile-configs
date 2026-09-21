"""Wayland input configuration."""
from libqtile.backend.wayland import InputConfig

# Apply touchpad-friendly defaults to every touchpad. Qtile chooses a more
# specific device rule first if we add one later.
wl_input_rules = {
    "type:touchpad": InputConfig(
        tap=True,
        drag=True,
        dwt=True,
        natural_scroll=True,
        scroll_method="two_finger",
        click_method="clickfinger",
    ),
}
