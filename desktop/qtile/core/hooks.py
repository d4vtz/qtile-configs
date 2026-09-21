"""Qtile lifecycle hooks.

Long-running desktop services will be systemd --user units. Hooks are kept
small and compositor-specific.
"""

from libqtile import hook


@hook.subscribe.startup_once
def first_start() -> None:
    # Reserved for actions that truly need Qtile's first-start lifecycle.
    pass
