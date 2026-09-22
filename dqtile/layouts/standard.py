from libqtile import layout
from libqtile.config import Match
from dqtile.theme.theme import BORDER_WIDTH, COLORS, GAP
from dqtile.core.rules import FLOAT_RULES
from .center_master import CenterMaster

layout_theme = dict(border_width=BORDER_WIDTH, margin=GAP, border_focus=COLORS["purple"], border_normal=COLORS["current_line"])
layouts = [
    CenterMaster(**layout_theme),
    layout.MonadTall(**layout_theme, ratio=.58, min_ratio=.25, max_ratio=.75, change_ratio=.05, change_size=20, single_border_width=0, single_margin=GAP),
    layout.Columns(**layout_theme, border_on_single=False, fair=True, insert_position=1, num_columns=2),
    layout.Max(),
]
floating_layout = layout.Floating(
    border_width=BORDER_WIDTH, border_focus=COLORS["pink"], border_normal=COLORS["current_line"],
    float_rules=[*layout.Floating.default_float_rules, Match(wm_class="confirmreset"), Match(wm_class="makebranch"), Match(wm_class="maketag"), Match(wm_class="ssh-askpass"), Match(title="branchdialog"), Match(title="pinentry"), *FLOAT_RULES],
)
