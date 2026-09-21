from libqtile.config import Key
from libqtile.lazy import lazy

from .groups import GROUP_NAMES

MOD = "mod4"
TERMINAL = "kitty"
LAUNCHER = "rofi -show drun"

keys = [
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Open terminal"),
    Key([MOD], "space", lazy.spawn(LAUNCHER), desc="Open application launcher"),
    Key([MOD], "Tab", lazy.next_layout(), desc="Next layout"),
    Key([MOD, "shift"], "q", lazy.window.kill(), desc="Close focused window"),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload Qtile config"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Quit Qtile"),
    Key([MOD], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([MOD], "v", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([MOD], "Left", lazy.layout.left(), desc="Focus left"),
    Key([MOD], "Right", lazy.layout.right(), desc="Focus right"),
    Key([MOD], "Up", lazy.layout.up(), desc="Focus up"),
    Key([MOD], "Down", lazy.layout.down(), desc="Focus down"),
    Key([MOD, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([MOD, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([MOD, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "control"], "Left", lazy.layout.grow_left(), desc="Grow left"),
    Key([MOD, "control"], "Right", lazy.layout.grow_right(), desc="Grow right"),
    Key([MOD, "control"], "Up", lazy.layout.grow_up(), desc="Grow up"),
    Key([MOD, "control"], "Down", lazy.layout.grow_down(), desc="Grow down"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Normalize layout"),
]

for name in GROUP_NAMES:
    keys.extend([
        Key([MOD], name, lazy.group[name].toscreen(), desc=f"Go to group {name}"),
        Key([MOD, "shift"], name, lazy.window.togroup(name, switch_group=True), desc=f"Move window to group {name}"),
    ])
