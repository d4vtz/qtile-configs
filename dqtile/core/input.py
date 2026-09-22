from libqtile.backend.wayland import InputConfig

wl_input_rules = {
    "type:touchpad": InputConfig(tap=True, drag=True, dwt=True, natural_scroll=False, scroll_method="two_finger", click_method="clickfinger"),
    "type:keyboard": InputConfig(kb_layout="latam", kb_options="terminate:ctrl_alt_bksp"),
}
wl_xcursor_theme = "Papirus-Dark"
wl_xcursor_size = 24
