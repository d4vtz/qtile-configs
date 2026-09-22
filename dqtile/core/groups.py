from libqtile.config import DropDown, Group, ScratchPad
WORKSPACE_NAMES=tuple(str(i) for i in range(1,8))
groups=[Group(i,label=i) for i in WORKSPACE_NAMES]
groups.append(ScratchPad("scratchpad",[DropDown("terminal","kitty --class qtile-scratchpad",x=.10,y=.08,width=.80,height=.80,opacity=.98,on_focus_lost_hide=False)]))
