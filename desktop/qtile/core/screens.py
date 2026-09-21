"""Temporary Qtile UI.

The final desktop bar belongs to Quickshell. This bar intentionally stays
small so Qtile remains usable while the shell is being built.
"""

from libqtile import bar, widget
from libqtile.config import Screen

from desktop.appearance import BAR_SIZE, COLORS, FONT, FONT_SIZE

widget_defaults = {
    "font": FONT,
    "fontsize": FONT_SIZE,
    "padding": 6,
    "foreground": COLORS["foreground"],
}
extension_defaults = widget_defaults.copy()


def make_bar() -> bar.Bar:
    return bar.Bar(
        [
            widget.GroupBox(
                active=COLORS["foreground"],
                inactive=COLORS["comment"],
                highlight_method="line",
                this_current_screen_border=COLORS["purple"],
                urgent_border=COLORS["red"],
                disable_drag=True,
            ),
            widget.CurrentLayout(),
            widget.Spacer(),
            widget.WindowName(max_chars=70),
            widget.Spacer(),
            widget.CPU(format="CPU {load_percent}%"),
            widget.Memory(format="RAM {MemPercent}%"),
            widget.Volume(fmt="VOL {}"),
            widget.Battery(format="BAT {percent:2.0%}"),
            widget.Clock(format="%a %d %b  %H:%M"),
            widget.StatusNotifier(),
        ],
        BAR_SIZE,
        background=COLORS["background"],
        border_color=COLORS["current_line"],
        border_width=[0, 0, 1, 0],
    )


screens = [Screen(top=make_bar())]
