from libqtile.config import DropDown, Group, ScratchPad

WORKSPACE_NAMES = tuple(str(i) for i in range(1, 8))

groups = [Group(name, label=name) for name in WORKSPACE_NAMES]

# Hidden utility workspace. More dropdowns can be added without consuming a
# normal workspace.
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "terminal",
                "kitty --class qtile-scratchpad",
                x=0.10,
                y=0.08,
                width=0.80,
                height=0.80,
                opacity=0.98,
                on_focus_lost_hide=False,
            )
        ],
    )
)
