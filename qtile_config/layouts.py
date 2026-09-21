from libqtile import layout
from libqtile.config import Match

from .theme import BORDER_WIDTH, DRACULA, GAP

layout_theme = {
    "border_width": BORDER_WIDTH,
    "margin": GAP,
    "border_focus": DRACULA["purple"],
    "border_normal": DRACULA["current_line"],
}

layouts = [layout.MonadTall(**layout_theme), layout.Columns(**layout_theme), layout.Max()]

floating_layout = layout.Floating(
    border_width=BORDER_WIDTH,
    border_focus=DRACULA["pink"],
    border_normal=DRACULA["current_line"],
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"), Match(wm_class="makebranch"),
        Match(wm_class="maketag"), Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"), Match(title="pinentry"),
    ],
)
