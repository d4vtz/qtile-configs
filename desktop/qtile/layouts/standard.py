from libqtile import layout
from libqtile.config import Match

from desktop.appearance import BORDER_WIDTH, COLORS, GAP

layout_theme = {
    "border_width": BORDER_WIDTH,
    "margin": GAP,
    "border_focus": COLORS["purple"],
    "border_normal": COLORS["current_line"],
}

layouts = [
    layout.MonadTall(
        **layout_theme,
        ratio=0.58,
        min_ratio=0.25,
        max_ratio=0.75,
        change_ratio=0.05,
        change_size=20,
        single_border_width=0,
        single_margin=GAP,
    ),
    layout.Columns(
        **layout_theme,
        border_on_single=False,
        fair=True,
        insert_position=1,
        num_columns=2,
    ),
    layout.Max(),
]

floating_layout = layout.Floating(
    border_width=BORDER_WIDTH,
    border_focus=COLORS["pink"],
    border_normal=COLORS["current_line"],
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="blueman-manager"),
    ],
)
