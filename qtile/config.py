# Imports
import os
import subprocess
import colors

from typing import List
from libqtile import qtile, layout, bar, hook, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile.lazy import lazy
from qtile_extras import widget

# Colors from the colors.py file
colors, backgroundColor, foregroundColor, workspaceColor, chordColor = colors.oxocarbon()

mod = "mod4"
terminal = "wezterm"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.run([home])

# Define your apps here to use later in keybinds
class Apps:
    launcher = "rofi -show drun"
    browser = "firefox"
    filemanager = "pcmanfm"
    chatapp = "discord"
    screenshotter = "flameshot gui"
    lockscreen = "betterlockscreen -l"

# Same thing but for music controls
class Music:
    next = "mpc --host localhost --port 8800 next"
    prev = "mpc --host localhost --port 8800 prev"
    toggle = "mpc --host localhost --port 8800 toggle"

keys = [
# Open terminal
    Key([mod], "Return", lazy.spawn(terminal)),

# Qtile System Actions
    # Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "r", lazy.reload_config()),

# Active Window Actions
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "Shift" ], "c", lazy.window.kill()),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete()
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add()
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster()
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster()
        ),

# Window Focus (Vim keys)
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# Qtile Layout Actions
    Key([mod], "r", lazy.layout.reset()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "f", lazy.layout.flip()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

# Move windows around MonadTall/MonadWide Layouts
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),

# Switch focus to specific monitor
    Key([mod], "i", lazy.to_screen(0)), 
    Key([mod], "o", lazy.to_screen(1)),

# Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

# Apps
    Key([mod], "w", lazy.spawn(Apps.browser)),
    Key([mod], "e", lazy.spawn(Apps.filemanager)),
    Key([mod], "q", lazy.spawn(Apps.screenshotter)),

    Key([mod, "shift"], "q", lazy.spawn(Apps.lockscreen)),
    Key([mod, "shift"], "return", lazy.spawn(Apps.launcher)),

    Key([mod, "shift"], "p", lazy.spawn(Music.next)),
    Key([mod, "shift"], "o", lazy.spawn(Music.prev)),
    Key([mod, "shift"], "i", lazy.spawn(Music.toggle)),
]

# Our groups and which apps go on specific groups
groups = [
        Group("1", layout="monadtall", matches=[Match(wm_class=Apps.browser)]),
        Group("2", layout="monadtall", matches=[Match(wm_class=Apps.chatapp)]),
        Group("3", layout="monadtall", matches=[Match(wm_class=Apps.filemanager)]),
        Group("4", layout="monadtall"),
        Group("5", layout="monadtall"),
        Group("6", layout="max", matches=[Match(wm_class="pcsx2-qt" "prismlauncher")]),
        ]

# This makes our group labels change dynamically
@hook.subscribe.setgroup
def setgroup():
    for i in range(len(groups)-1):
        qtile.groups[i].label = "󰹞"
        qtile.current_group.label = "󰹞󰹞󰹞"

# Add group specific keybindings
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Mod + number to move to that group."),
        Key(["mod1"], "Tab", lazy.screen.next_group(), desc="Move to next group."),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group(), desc="Move to previous group."),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="Move focused window to new group."),
    ])

# Define scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", "wezterm start --class scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("term2", "wezterm start --class scratch2", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("ranger", "wezterm start --class ranger -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("volume", "wezterm start --class volume -e alsamixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("mus", "wezterm start --class mus -e ncmpcpp", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
]))

# Scratchpad keybindings
keys.extend([
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod, "shift"], "m", lazy.group['scratchpad'].dropdown_toggle('term2')),
    Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('mus')),
])

# Define layouts and layout themes
layout_theme = {
    "margin":8,
    "border_width": 3,
    "border_focus": colors[5],
    "border_normal": colors[1]
}

layouts = [ layout.MonadTall(**layout_theme), layout.Max(**layout_theme) ]

widget_defaults = dict(
    font="JetBrains Mono Bold",
    fontsize=14,
    background=colors[0],
    foreground=colors[1],
)

extension_defaults = widget_defaults.copy()

def get_widgets():
    widgets = [
        widget.Spacer(length=5),
        widget.GroupBox(
            highlight_method='text',
            active=colors[5],
            this_current_screen_border=colors[7],
            urgent_border=colors[0],
            ),
        widget.WindowName(),
        widget.Spacer(),
        widget.CurrentLayout(),
        widget.Clock(format="%I:%M %p"),
        widget.Spacer(length=10),
            ]
    return widgets

screens = [
    Screen(
        top=bar.Bar(
            get_widgets(),
            30,
            margin=8,
       ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='qview'),  # qview
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='flameshot'),
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], fullscreen_border_width = 0, border_width = 0)

auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wmname = "Qtile"
