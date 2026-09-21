"""Window matching and workspace routing rules."""

from libqtile.config import Match

# Application classes/app_ids are intentionally kept in one place. Wayland
# clients generally expose app_id while XWayland clients still expose wm_class.
WORKSPACE_RULES = {
    "1": [
        Match(wm_class="google-chrome"),
        Match(wm_class="google-chrome-stable"),
        Match(wm_class="chromium"),
        Match(wm_class="firefox"),
    ],
    "2": [
        Match(wm_class="code"),
        Match(wm_class="Code"),
        Match(wm_class="nvim"),
    ],
    "3": [
        Match(wm_class="org.kde.dolphin"),
        Match(wm_class="dolphin"),
    ],
}

FLOAT_RULES = [
    Match(wm_class="pavucontrol"),
    Match(wm_class="blueman-manager"),
    Match(wm_class="nm-connection-editor"),
    Match(wm_class="org.kde.polkit-kde-authentication-agent-1"),
    Match(wm_class="pinentry"),
    Match(title="pinentry"),
    Match(title="Picture-in-Picture"),
    Match(title="Picture in picture"),
]
