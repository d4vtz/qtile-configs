from libqtile.config import Key
from libqtile.lazy import lazy

from .apps import (
    BRIGHTNESS_DOWN, BRIGHTNESS_UP, FILE_MANAGER, LAUNCHER, MIC_MUTE,
    TERMINAL, VOLUME_DOWN, VOLUME_MUTE, VOLUME_UP,
)
from .groups import WORKSPACE_NAMES

MOD = "mod4"


@lazy.function
def cycle_occupied_groups(qtile, step: int) -> None:
    """Cycle through normal workspaces that currently contain windows."""
    occupied = [
        group
        for group in qtile.groups
        if group.name in WORKSPACE_NAMES and group.windows
    ]

    if not occupied:
        return

    current = qtile.current_group
    if current not in occupied:
        target = occupied[0] if step > 0 else occupied[-1]
    else:
        index = occupied.index(current)
        target = occupied[(index + step) % len(occupied)]

    target.toscreen()


keys = [
    # Applications
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Terminal"),
    Key([MOD], "space", lazy.spawn(LAUNCHER), desc="Launcher"),
    Key([MOD], "e", lazy.spawn(FILE_MANAGER), desc="File manager"),

    # Focus
    Key([MOD], "Left", lazy.layout.left(), desc="Focus left"),
    Key([MOD], "Right", lazy.layout.right(), desc="Focus right"),
    Key([MOD], "Up", lazy.layout.up(), desc="Focus up"),
    Key([MOD], "Down", lazy.layout.down(), desc="Focus down"),
    Key([MOD], "Tab", lazy.next_layout(), desc="Next layout"),

    # Cycle only through occupied workspaces
    Key([MOD], "bracketright", cycle_occupied_groups(1), desc="Next occupied workspace"),
    Key([MOD], "bracketleft", cycle_occupied_groups(-1), desc="Previous occupied workspace"),

    # Move windows
    Key([MOD, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move left"),
    Key([MOD, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move right"),
    Key([MOD, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move up"),
    Key([MOD, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move down"),

    # Resize
    Key([MOD, "control"], "Left", lazy.layout.grow_left(), desc="Grow left"),
    Key([MOD, "control"], "Right", lazy.layout.grow_right(), desc="Grow right"),
    Key([MOD, "control"], "Up", lazy.layout.grow_up(), desc="Grow up"),
    Key([MOD, "control"], "Down", lazy.layout.grow_down(), desc="Grow down"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Normalize"),

    # Window state
    Key([MOD], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen"),
    Key([MOD], "v", lazy.window.toggle_floating(), desc="Floating"),
    Key([MOD, "shift"], "q", lazy.window.kill(), desc="Close window"),
    Key([MOD], "grave", lazy.group["scratchpad"].dropdown_toggle("terminal"), desc="Scratchpad"),

    # Qtile lifecycle
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload config"),
    Key([MOD, "control", "shift"], "q", lazy.shutdown(), desc="Exit Qtile"),

    # Media keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn(VOLUME_UP), desc="Volume up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(VOLUME_DOWN), desc="Volume down"),
    Key([], "XF86AudioMute", lazy.spawn(VOLUME_MUTE), desc="Mute audio"),
    Key([], "XF86AudioMicMute", lazy.spawn(MIC_MUTE), desc="Mute microphone"),
    Key([], "XF86MonBrightnessUp", lazy.spawn(BRIGHTNESS_UP), desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(BRIGHTNESS_DOWN), desc="Brightness down"),
]

for name in WORKSPACE_NAMES:
    keys.extend([
        Key([MOD], name, lazy.group[name].toscreen(), desc=f"Workspace {name}"),
        Key([MOD, "shift"], name, lazy.window.togroup(name, switch_group=True), desc=f"Move to workspace {name}"),
    ])
