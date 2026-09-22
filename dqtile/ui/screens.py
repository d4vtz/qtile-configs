from libqtile import bar,widget
from libqtile.config import Screen
from dqtile.theme.theme import BAR_SIZE,COLORS,FONT,FONT_SIZE
widget_defaults={"font":FONT,"fontsize":FONT_SIZE,"padding":6,"foreground":COLORS["foreground"]}
extension_defaults=widget_defaults.copy()
def make_bar():
    return bar.Bar([
        widget.GroupBox(active=COLORS["foreground"],inactive=COLORS["comment"],highlight_method="line",this_current_screen_border=COLORS["purple"],urgent_border=COLORS["red"],disable_drag=True),
        widget.CurrentLayout(fmt=" {} "),widget.Spacer(length=12),widget.WindowName(max_chars=70),widget.Spacer(),
        widget.CheckUpdates(distro="Arch_checkupdates",display_format="UPD {updates}",no_update_string="",colour_have_updates=COLORS["orange"],execute="kitty -e bash -lc 'paru; exec bash'"),
        widget.CPU(format="CPU {load_percent}%"),widget.Memory(format="RAM {MemPercent}%"),widget.Volume(fmt="VOL {}"),widget.Battery(format="BAT {percent:2.0%}",low_percentage=.20,low_foreground=COLORS["red"]),widget.Clock(format="%a %d %b  %H:%M")
    ],BAR_SIZE,background=COLORS["background"],border_color=COLORS["current_line"],border_width=[0,0,1,0])
screens=[Screen(top=make_bar())]
