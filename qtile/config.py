# Tsukihime
# Simple-ish configuration for qtile, focused on functionality and elegance
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
# Available colorschemes: oxocarbon, janleigh, rosepine, radium (more will be added)
colors, backgroundColor, foregroundColor, workspaceColor, chordColor = colors.oxocarbon()

# Modkey for keybinds, "mod4" refers to the Super or Windows keys
mod = "mod4"
# mod = "mod1" # Alt as super

# Define your apps here to use later in keybinds
class Apps:
    terminal = "st"
    term_cmd = "st -c "
    launcher = "rofi -show drun"
    browser  = "firefox"
    files    = "thunar"
    chatapp  = "discord"
    editor   = "nvim"
    photos   = "photopea"

# Define music related commands, mpd and audio related stuff,
# you could map it to X86Volume keys but they dont work with my keyboard
# so I just stick to pulsemixer
class Music:
    next     = "mpc -h localhost -p 8800 next"
    prev     = "mpc -h localhost -p 8800 prev"
    toggle   = "mpc -h localhost -p 8800 toggle"
    volup    = "pulsemixer --change-volume +10"
    voldown  = "pulsemixer --change-volume -10"
    mute     = "pulsemixer --toggle-mute"

#-----------
# Resizing Floating Windows
#-----------

# We have to define this up here because python is stupid
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

# Resize floating windows with Arrow keys, function down further
    Key([mod], "Right", resize_floating_window(width=20), desc='increase width by 20'),
    Key([mod], "Left", resize_floating_window(width=-20), desc='decrease width by 20'),
    Key([mod], "Down", resize_floating_window(height=20), desc='increase height by 20'),
    Key([mod], "Up", resize_floating_window(height=-20), desc='decrease height by 20'),

# Window Focus (Vim keys)
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# Qtile Layout Actions
    Key([mod], "r", lazy.layout.reset()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),
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
    Key([mod], "e", lazy.spawn(Apps.files)),
    Key([mod], "d", lazy.spawn(Apps.chatapp)),
    Key([mod, "shift"], "return", lazy.spawn(Apps.launcher)),

# Music control
    Key([mod], "o", lazy.spawn(Music.next)),
    Key([mod], "u", lazy.spawn(Music.prev)),
    Key([mod], "i", lazy.spawn(Music.toggle)),

# Volume control
# scuffed but it is what works for me
    Key([mod], "t", lazy.spawn(Music.volup)),
    Key([mod], "r", lazy.spawn(Music.voldown)),
    Key([mod], "y", lazy.spawn(Music.mute)),

# Screenshot
# requires 'maim', 'slop', 'xclip-git'
# because flameshot takes a whole year to boot ffs
    Key([mod], "q", lazy.spawn("maim -m 5 | xclip -selection clipboard -t image/png", shell=True)), # screenshot whole screen
    Key([mod, "shift"], "q", lazy.spawn("maim -m 5 -s | xclip -selection clipboard -t image/png", shell=True)), # screenshot specific window

# Reload Eww
    Key([mod, "shift"], "t", lazy.spawn("eww open controlcenter", shell=True)), # screenshot specific window
]

#-----------
# Groups/Workspaces
#-----------

# Our groups and which apps go on specific groups
# If you want to find out the wm_class of a specific app, run 'xprop | grep WM_CLASS'
groups = [
        Group("1", layout="monadtall", matches=[Match(wm_class=Apps.browser)]),   # browser
        Group("2", layout="monadtall", matches=[Match(wm_class=Apps.chatapp)]),   # discord
        Group("3", layout="monadtall"),
        Group("4", layout="monadtall"),
        Group("5", layout="monadtall"),
        Group("6", layout="monadtall"),
    ]
# This makes our group labels change dynamically,
# Qtile cannot make shapes like in Awesome, so we settle
# for an unicode symbol repeated over for our current group
@hook.subscribe.setgroup
def setgroup():
    # Omega scuffed hack to make the hook go through the length
    # of all of our groups, then subtract one from it, so the scratchpads
    # wont show up in the bar, then it applies our unicode magic
    num_groups = len(qtile.groups)
    for index, group in enumerate(qtile.groups):
        if index == num_groups - 1:
            continue  # Skip the last group
        if group is qtile.current_group:
            group.label = "󰹞󰹞󰹞󰹞󰹞󰹞󰹞󰹞󰹞"  # Currently focused group
        else:
            if group.windows:
                group.label = "󰹞󰹞󰹞󰹞"  # Unfocused group with windows
            else:
                group.label = "󰹞󰹞󰹞󰹞"  # Unfocused empty group

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
    DropDown("term", Apps.term_cmd+"scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("term2", Apps.term_cmd+"scratch2", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("ranger", Apps.term_cmd+"ranger -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("volume", Apps.term_cmd+"volume -e alsamixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("song", Apps.term_cmd+"song -e ncmpcpp", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
]))

# Scratchpad keybindings
keys.extend([
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod, "shift"], "m", lazy.group['scratchpad'].dropdown_toggle('term2')),
    Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('song')),
])

#-----------
# Layouts
#-----------

# Define layouts and layout themes
# It's easier to refer to a color in the colors array that we imported from colors.py
# than to type every single individual hex code, this also allows for possible
# dynamic theme switching
layout_theme = {
    "margin": 8,
    "border_width": 16,
    # --------------
    # Triple Borders
    # --------------
    # Qtile is stupid as shit and doesnt let us regulate the width of each individual border
    # if we have more than one, so the solution is to spam as much as we need to achieve a
    # certain thickness. It also does not let us reference colors from colors.py
    "border_focus": ["161616", "161616", "161616", "161616", "393939", "161616", "161616", "161616", "161616", "161616"],
    "border_normal": ["161616", "161616", "161616", "161616", "262626", "161616", "161616", "161616", "161616", "161616"],
    # "border_focus": colors[5], # normal borders for normal people
    # "border_normal": colors[3],
}

# Consult the Qtile standard configuration to see other layout options
# these are what work for me, a simple master and stack and a max layout for games
layouts = [ layout.MonadTall(**layout_theme), layout.MonadWide(**layout_theme), layout.Max(**layout_theme) ]

#-----------
# Bar
#-----------

# Functions
def startmenu():
    qtile.cmd_spawn("rofi -show drun")

def controlcenter():
    qtile.cmd_spawn("eww open controlcenter")

# Parsing : remove all text.
def txt_remove(text):
    return ""

# Here we reference our colors.py file for using our chosen colorscheme,
# remember to tweak values accordingly, I can't promise everything will look
# perfectly out of the box, select the accent colors of your choosing,
# refer to colors.py to see what each color is.

# Our default parameters for the widgets in our bar
# Append parameters here so you can spare yourself from repetition
widget_defaults = dict(
    font="Jetbrains Mono Bold",
    fontsize=14,
    background=colors[0],
    foreground=colors[2],
)

extension_defaults = widget_defaults.copy()

# The bar
# i am so sorry for everyone coming into this mess
def get_widgets():
    widgets = [
        widget.Spacer(length=3),
        widget.TextBox(
            text='󰋜',
            foreground=colors[7],
            background=colors[3],
            mouse_callbacks={"Button1": startmenu},
            ),
        widget.Spacer(length=5, background="#262626", mouse_callbacks={"Button1": startmenu}),
        widget.Spacer(length=5),
        widget.GroupBox(
            highlight_method='text', # makes the highlights just change the group name color
            inactive=colors[1],
            active=colors[11],
            background=colors[3],
            this_current_screen_border=colors[5],
            other_current_screen_border=colors[7],
            spacing=0,
            padding=1,
            urgent_border=colors[0], # make it the same as the background for no ugly borders
            ),
        widget.Spacer(length=5, background="#262626"),
        widget.Spacer(),
        widget.WidgetBox(widgets=[
            widget.Systray(),
            ],
            text_closed=' ',
            text_open=' ',
            ),
        widget.Spacer(length=5),
        widget.Battery(
            foreground=colors[0],
            background=colors[8],
            low_background=colors[7],
            battery="BAT1",
            show_short_text=False,
            charge_char='  󱐋  ',
            full_char='  󱐋  ',
            discharge_char='  󱐌  ',
            empty_char='  󱐌  ',
            unknown_char='  ?  ',
            format='{char}',
            ),
        widget.Spacer(length=5),
        widget.TextBox(
            text='',
            background=colors[3],
            mouse_callbacks={"Button1": controlcenter},
            ),
        widget.Spacer(length=5, background=colors[3]),
        widget.Spacer(length=5),
        widget.Clock(
            format="%I:%M",
            background=colors[3],
            padding=8,
            ),
        widget.Volume(
            fmt='󰕾',
            scroll=True,
            step=10,
            padding=7,
            ),
        widget.Wlan(
            format='󰤨',
            disconnected_message='󰤭',
            padding=7,
            ),
        widget.Spacer(length=5),
        widget.CurrentLayoutIcon(
            use_mask=True,
            scale=0.6,
            padding=5,
            background=colors[3],
            ),
        widget.Spacer(length=3),
        ]
    return widgets

# Define our screens, you can add more if you have more monitors here
screens = [
    Screen(
        top=bar.Bar(
            get_widgets(),
            23,
            border_color="#161616",
            border_width=5,
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
    Match(wm_class='Gpick'),
    Match(wm_class='Places'), # firefox downloads screen, i like it floating
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], fullscreen_border_width = 0, border_width = 0)

def wallpaper():
    path = '~/Pictures/Wallpapers/Uncategorized/sakura-bw.png' # cool beans
    os.system('feh --bg-scale ' + path)

# Autostart script, for starting important apps, refer to autostart.sh
@hook.subscribe.startup_once
def autostart():
    wallpaper()
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
