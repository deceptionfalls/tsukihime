from typing import List
import os
import subprocess

from libqtile import qtile, layout, bar, hook, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile.lazy import lazy

from qtile_extras import widget

mod = "mod4"
terminal = "kitty"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])

keys = [
# Open terminal
    Key([mod], "Return", lazy.spawn(terminal)),
# Qtile System Actions
    # Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "r", lazy.reload_config()),
# Active Window Actions
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "c", lazy.window.kill()),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete()
        ),
    Key([mod, "control"], "Right",
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
    Key([mod, "control"], "Left",
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
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster()
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster()
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster()
        ),

# Window Focus (Arrows and Vim keys)
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# Qtile Layout Actions
    Key(["mod1"], "r", lazy.spawncmd()),
    Key([mod], "r", lazy.layout.reset()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "f", lazy.layout.flip()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

# Move windows around MonadTall/MonadWide Layouts
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),

# Switch focus to specific monitor (out of three
    Key([mod], "i", lazy.to_screen(0)), 
    Key([mod], "o", lazy.to_screen(1)),

# Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

]

# Create labels for groups and assign them a default layout.
groups = []

group_names = ["1", "2", "3", "4", "5", "6"]

group_labels = ["", "", "󰭹", "󰉋", "", "󰍳"]
# group_labels = ["1", "2", "3", "4", "5", "6"]

group_layouts = ["monadtall", "monadtall", "max", "monadtall", "columns", "max"]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

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
    DropDown("term", "kitty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("term2", "kitty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("ranger", "kitty --class=ranger -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("volume", "kitty --class=volume -e alsamixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("mus", "kitty --class=mus -e ncmpcpp", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
]))

# Scratchpad keybindings
keys.extend([
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod, "shift"], "m", lazy.group['scratchpad'].dropdown_toggle('term2')),
    Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('mus')),
])

#Colors
colors = []
cache='/home/tsukki/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)

# Define layouts and layout themes
layout_theme = {
    "margin":5,
    "border_width": 4,
    "border_focus": colors[3],
    "border_normal": colors[1]
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.MonadThreeCol(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.Spiral(**layout_theme),
    # layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

# Mouse callback functions
def powermenu():
    qtile.cmd_spawn("./rofi/powermenu.rasi")

widget_defaults = dict(
    font="FiraCode Nerd Font Bold",
    fontsize=13,
    padding=5,
    background=colors[0],
)

extension_defaults = widget_defaults.copy()

def get_widgets():
    widgets = [
        widget.Spacer(
            length=10,
            ),
        widget.GroupBox(
            fontsize=12,
            rounded=False,
            center_aligned=True,
            disable_drag=True,
            borderwidth=3,
            highlight_method='text',
            active=colors[1],
            this_current_screen_border=colors[2],
            urgent_border=colors[0],
            ),
        widget.Spacer(
            ),
        widget.Mpd2(
            play_states={'pause': '', 'play': '󰏦', 'stop': '󰙧'},
            status_format='{play_status} {artist} - {title}',
            port='6601',
            host='localhost',
            no_connection='Offline',
            foreground=colors[1],
            padding=5,
            ),
        widget.Spacer(
            ),
         widget.UPowerWidget(
            battery_height=9,
            percentage_low=0.90,
            battery_name="BAT1",
            fill_charge=colors[1],
            fill_critical=colors[2],
            fill_low=colors[1],
            fill_normal=colors[1],
            border_colour=colors[1],
            border_charge_colour=colors[1],
            border_critical_colour=colors[2],
            foreground=colors[1],
            text_charging='{percentage:.0f}%',
            text_discharging='{percentage:.0f}%',
            margin=4,
            ),
        widget.Battery(
            battery_name='BAT1',
            format='{percent:2.0%}',
            foreground=colors[1],
            padding=5,
            ),
        widget.Spacer(
            length=1,
            ),
        widget.Wlan(
            foreground=colors[1],
            format='󰤯 {essid}',
            disconnected_message='󰤮 Offline',
            interface='wlan0',
            padding=3,
            ),
        widget.Spacer(
            length=1,
            ),
        widget.PulseVolume(
            fmt=" {}",
            foreground=colors[1],
            padding=5,
            ),
        widget.Spacer(
            length=1,
            ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=colors[1],
            padding=5,
            ),
        widget.Spacer(
            length=10,
            ),
        # widget.TextBox(
        #     text=" ",
        #     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("sh /home/tsukki/.config/rofi/deathemonic/bin/powermenu")},
        #     fontsize=15,
        #     background=colors[1],
        #     foreground=colors[0],
        #     font='Fira Code Nerd Font Bold',
        #     padding=5,
        #     ),
            ]
    return widgets

screens = [
    Screen(
        top=bar.Bar(
            get_widgets(),
            26,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
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
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], fullscreen_border_width = 0, border_width = 0)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "Qtile"
