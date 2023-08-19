# Tsukihime, the Qtile configuration to rule them all
# Made by @tsukki9696

#-----------
# Imports
#-----------
import os
import subprocess
import colors

from typing import List
from libqtile import qtile, layout, bar, hook, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile.lazy import lazy
from qtile_extras import widget

#-----------
# User Settings
#-----------

# Colorscheme, referenced by an external colors.py file
# Affects bar, window decorations and widgets inside the said bar
# Available colorschemes: oxocarbon, janleigh, rosepine, radium
colors, backgroundColor, foregroundColor, workspaceColor, chordColor = colors.oxocarbon()

# Modkey for keybinds, "mod4" refers to the Super or Windows keys
mod = "mod4"
# mod = "mod1" # Alt as super

# Define your apps here to use later in keybinds
# Same thing for music controls
class Apps:
    terminal = "wezterm"
    launcher = "rofi -show drun"
    browser = "firefox"
    filemanager = "pcmanfm"
    chatapp = "armcord"
    screenshotter = "flameshot gui"
    lockscreen = "betterlockscreen -l"

class Music:
    next = "mpc --host localhost --port 8800 next"
    prev = "mpc --host localhost --port 8800 prev"
    toggle = "mpc --host localhost --port 8800 toggle"
    volup = "pulsemixer --change-volume +10"
    voldown = "pulsemixer --change-volume -10"
    mute = "pulsemixer --toggle-mute"

# Function for resizing floating windows
@lazy.function
def resize_floating_window(qtile, width: int = 0, height: int = 0):
    w = qtile.current_window
    w.cmd_set_size_floating(w.width + width, w.height + height)

#-----------
# Keybindings
#-----------

keys = [
# Open terminal
    Key([mod], "Return", lazy.spawn(Apps.terminal)),

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

# Resize floating windows with Arrow keys
    Key([mod], "Right", resize_floating_window(width=10), desc='increase width by 10'),
    Key([mod], "Left", resize_floating_window(width=-10), desc='decrease width by 10'),
    Key([mod], "Up", resize_floating_window(height=10), desc='increase height by 10'),
    Key([mod], "Down", resize_floating_window(height=-10), desc='decrease height by 10'),

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
    Key([mod, "shift"], "i", lazy.to_screen(0)), 
    Key([mod, "shift"], "o", lazy.to_screen(1)),

# Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

# Apps
    Key([mod], "w", lazy.spawn(Apps.browser)),
    Key([mod], "e", lazy.spawn(Apps.filemanager)),
    Key([mod], "q", lazy.spawn(Apps.screenshotter)),

    Key([mod, "shift"], "q", lazy.spawn(Apps.lockscreen)),
    Key([mod, "shift"], "return", lazy.spawn(Apps.launcher)),

# Music control
    Key([mod], "o", lazy.spawn(Music.next)),
    Key([mod], "u", lazy.spawn(Music.prev)),
    Key([mod], "i", lazy.spawn(Music.toggle)),

# Volume control, scuffed but it is what works for me
    Key([mod], "t", lazy.spawn(Music.volup)),
    Key([mod], "r", lazy.spawn(Music.voldown)),
    Key([mod], "y", lazy.spawn(Music.mute)),
]

#-----------
# Groups/Workspaces
#-----------

# Our groups and which apps go on specific groups
# If you want to find out the wm_class of a specific app, use 'xprop | grep WM_CLASS' 
groups = [
        Group("1", layout="monadtall", matches=[Match(wm_class=Apps.browser)]),
        Group("2", layout="monadtall", matches=[Match(wm_class=Apps.chatapp)]),
        Group("3", layout="monadtall", matches=[Match(wm_class=Apps.filemanager)]),
        Group("4", layout="monadtall"),
        Group("5", layout="monadtall"),
        Group("6", layout="max", matches=[Match(wm_class="pcsx2-qt" "prismlauncher")]),
        ]

# This makes our group labels change dynamically,
# Qtile cannot make shapes like in Awesome, so we settle
# for an unicode symbol repeated over for our current group
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
# Refer to your terminal emulator's way to classify sessions,
# wezterm uses 'wezterm start --class' and kitty uses 'kitty --class' for example
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

#-----------
# Layouts
#-----------

# Define layouts and layout themes
# It's easier to refer to a color in the colors array that we imported from colors.py
# than to type every single individual hex code, this also allows for possible
# dynamic theme switching
layout_theme = {
    "margin":8,
    "border_width": 3,
    "border_focus": colors[5],
    "border_normal": colors[1]
}

# Consult the Qtile standard configuration to see other layout options
layouts = [ layout.MonadTall(**layout_theme), layout.Max(**layout_theme) ]

#-----------
# Bar
#-----------

# Bar configuration
# Here we reference our colors.py file for using our chosen colorscheme,
# remember to tweak values accordingly, I can't promise everything will look
# perfectly out of the box, select the accent colors of your choosing,
# refer to colors.py to see what each color is.

# Our default parameters for the widgets in our bar
# Append parameters here so you can spare yourself from repetition
widget_defaults = dict(
    font="JetBrains Mono Bold",
    fontsize=14,
    background=colors[0],
    foreground=colors[1],
)

extension_defaults = widget_defaults.copy()

# Our widgets
# Refer the qtile wiki for other widget options both in the builtin widgets and in the qtile-extras repo
# Tweak colors according to your selected colorscheme, cant promise everything looks perfect with no tweaks
def get_widgets():
    widgets = [
        widget.Spacer(length=5),
        widget.GroupBox(
            highlight_method='text',
            inactive=colors[1],
            active=colors[7],
            this_current_screen_border=colors[5],
            urgent_border=colors[0],
            ),
        widget.CurrentLayoutIcon(
            use_mask=True,
            scale=0.5,
            padding=10, # Don't delete this or the bar will go transparent, for some reason
        ),
        widget.Spacer(),
        widget.Clock(format="%I:%M %p"),
        widget.Spacer(length=10),
            ]

    return widgets

# Define our screens, I occasionally use two monitors so there's why we have two screens here
# you're free to remove and add as needed
screens = [
    Screen(
        top=bar.Bar(
            get_widgets(),
            30,
            margin=8,
       ),
    ),
    Screen(
        top=bar.Bar(
            get_widgets(),
            30,
            margin=8,
       ),
    ),
]

#-----------
# Mouse
#-----------

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#-----------
# Misc
#-----------

# Which screens spawn as floating by default
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='qview'), 
    Match(wm_class='feh'),
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='flameshot'),
    Match(wm_class='galculator'),
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], fullscreen_border_width = 0, border_width = 0)

# Autostart script, for starting important apps, refer to autostart.sh
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.run([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wmname = "Qtile"
