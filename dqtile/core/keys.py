from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy
from .apps import BRIGHTNESS_DOWN,BRIGHTNESS_UP,BROWSER,FILE_MANAGER,LAUNCHER,LOCK,MIC_MUTE,SCREENSHOT,TERMINAL,VOLUME_DOWN,VOLUME_MUTE,VOLUME_UP
from .groups import WORKSPACE_NAMES
MOD="mod4"
@lazy.function
def cycle_occupied_groups(qtile,step:int)->None:
    occupied=[g for g in qtile.groups if g.name in WORKSPACE_NAMES and g.windows]
    if not occupied:return
    current=qtile.current_group
    target=(occupied[0] if step>0 else occupied[-1]) if current not in occupied else occupied[(occupied.index(current)+step)%len(occupied)]
    target.toscreen()
keys=[
Key([MOD],"Return",lazy.spawn(TERMINAL),desc="Terminal"),Key([MOD],"space",lazy.spawn(LAUNCHER),desc="Launcher"),Key([MOD],"e",lazy.spawn(FILE_MANAGER),desc="Files"),Key([MOD],"b",lazy.spawn(BROWSER),desc="Browser"),
Key([MOD],"Left",lazy.layout.left()),Key([MOD],"Right",lazy.layout.right()),Key([MOD],"Up",lazy.layout.up()),Key([MOD],"Down",lazy.layout.down()),
Key([MOD,"shift"],"Left",lazy.layout.shuffle_left()),Key([MOD,"shift"],"Right",lazy.layout.shuffle_right()),Key([MOD,"shift"],"Up",lazy.layout.shuffle_up()),Key([MOD,"shift"],"Down",lazy.layout.shuffle_down()),Key([MOD,"shift"],"Return",lazy.layout.swap_main()),
Key([MOD,"control"],"Left",lazy.layout.grow_left()),Key([MOD,"control"],"Right",lazy.layout.grow_right()),Key([MOD,"control"],"Up",lazy.layout.grow_up()),Key([MOD,"control"],"Down",lazy.layout.grow_down()),Key([MOD],"n",lazy.layout.normalize()),
Key([MOD],"Tab",lazy.next_layout()),Key([MOD],"f",lazy.window.toggle_fullscreen()),Key([MOD],"v",lazy.window.toggle_floating()),Key([MOD],"q",lazy.window.kill()),
Key([MOD],"Page_Down",cycle_occupied_groups(1)),Key([MOD],"Page_Up",cycle_occupied_groups(-1)),Key([MOD],"grave",lazy.group["scratchpad"].dropdown_toggle("terminal")),
Key([MOD,"shift"],"s",lazy.spawn(SCREENSHOT)),Key([MOD,"control"],"l",lazy.spawn(LOCK)),Key([MOD,"control"],"r",lazy.reload_config()),Key([MOD,"control","shift"],"q",lazy.shutdown()),
Key([],"XF86AudioRaiseVolume",lazy.spawn(VOLUME_UP)),Key([],"XF86AudioLowerVolume",lazy.spawn(VOLUME_DOWN)),Key([],"XF86AudioMute",lazy.spawn(VOLUME_MUTE)),Key([],"XF86AudioMicMute",lazy.spawn(MIC_MUTE)),Key([],"XF86MonBrightnessUp",lazy.spawn(BRIGHTNESS_UP)),Key([],"XF86MonBrightnessDown",lazy.spawn(BRIGHTNESS_DOWN))]
for name in WORKSPACE_NAMES: keys.extend([Key([MOD],name,lazy.group[name].toscreen()),Key([MOD,"shift"],name,lazy.window.togroup(name,switch_group=True))])
for vt in range(1,8): keys.append(Key(["control","mod1"],f"f{vt}",lazy.core.change_vt(vt).when(func=lambda:qtile.core.name=="wayland")))
