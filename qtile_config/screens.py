from libqtile import bar, widget
from libqtile.config import Screen

from .theme import BAR_SIZE, DRACULA, FONT, FONT_SIZE

widget_defaults = dict(font=FONT, fontsize=FONT_SIZE, padding=6, foreground=DRACULA["foreground"])
extension_defaults = widget_defaults.copy()


def make_bar() -> bar.Bar:
    return bar.Bar([
        widget.GroupBox(
            active=DRACULA["foreground"], inactive=DRACULA["comment"],
            highlight_method="line", this_current_screen_border=DRACULA["purple"],
            urgent_border=DRACULA["red"], disable_drag=True,
        ),
        widget.CurrentLayout(), widget.Spacer(), widget.WindowName(max_chars=60), widget.Spacer(),
        widget.CPU(format="CPU {load_percent}%"),
        widget.Memory(format="RAM {MemPercent}%"),
        widget.Volume(fmt="VOL {}"),
        widget.Battery(format="BAT {percent:2.0%}", charge_char="+", discharge_char="-", full_char="=", unknown_char="?"),
        widget.Clock(format="%a %d %b  %H:%M"),
        # Systray is X11-only. StatusNotifier is the native Wayland tray.
        widget.StatusNotifier(),
    ], BAR_SIZE, background=DRACULA["background"], border_color=DRACULA["current_line"], border_width=[0, 0, 1, 0])

screens = [Screen(top=make_bar())]
