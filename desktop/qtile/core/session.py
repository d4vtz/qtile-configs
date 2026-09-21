"""Desktop session services managed by systemd --user.

Qtile only imports the graphical-session environment and starts the target.
Individual daemons belong in unit files so reloads never duplicate them.
"""

SESSION_TARGET = "qtile-session.target"

# Environment variables that need to reach D-Bus/systemd activated services.
SESSION_ENVIRONMENT = (
    "WAYLAND_DISPLAY",
    "DISPLAY",
    "XDG_CURRENT_DESKTOP",
    "XDG_SESSION_TYPE",
    "QT_QPA_PLATFORM",
    "XCURSOR_THEME",
    "XCURSOR_SIZE",
)

IMPORT_ENVIRONMENT = (
    "dbus-update-activation-environment --systemd "
    + " ".join(SESSION_ENVIRONMENT)
)
START_SESSION = f"systemctl --user start {SESSION_TARGET}"
STOP_SESSION = f"systemctl --user stop {SESSION_TARGET}"
