import subprocess
from libqtile import hook
@hook.subscribe.startup_once
def start_session()->None:
    subprocess.Popen(["dbus-update-activation-environment","--systemd","WAYLAND_DISPLAY","DISPLAY","XDG_CURRENT_DESKTOP","XDG_SESSION_TYPE"])
    subprocess.Popen(["systemctl","--user","start","qtile-session.target"])
@hook.subscribe.shutdown
def stop_session()->None:
    subprocess.Popen(["systemctl","--user","stop","qtile-session.target"])
