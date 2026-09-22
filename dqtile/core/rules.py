from libqtile.config import Match

FLOAT_RULES = [
    Match(wm_class="pavucontrol"), Match(wm_class="blueman-manager"),
    Match(wm_class="nm-connection-editor"),
    Match(wm_class="org.kde.polkit-kde-authentication-agent-1"),
    Match(wm_class="pinentry"), Match(title="pinentry"),
    Match(title="Picture-in-Picture"), Match(title="Picture in picture"),
]
