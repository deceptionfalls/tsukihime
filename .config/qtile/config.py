import os
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile import layout, bar, hook, widget
from libqtile.lazy import lazy

from qtile_extras import widget

mod = "mod4"
terminal = "alacritty"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])

keys = [
# Open terminal
    Key([mod], "Return", lazy.spawn(terminal)),
# Qtile System Actions
    Key([mod, "shift"], "r", lazy.restart()),
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
]

# Create labels for groups and assign them a default layout.
groups = []

group_names = ["1", "2", "3", "4", "5"]

group_labels = ["", "", "󰙯", "󰉋", "󰅢"]
# group_labels = ["1", "2", "3", "4", "5"]

group_layouts = ["monadtall", "monadtall", "max", "monadtall", "monadtall"]

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
    DropDown("term", "alacritty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("term2", "alacritty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("ranger", "alacritty --class=ranger -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("volume", "alacritty --class=volume -e alsamixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("mus", "alacritty --class=mus -e ncmpcpp", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
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
catppuccin = {
    "base":         "#24273a",
    "crust":        "#1e2030",
    "surface0":     "#363a4f",
    "surface1":     "#494d64",
    "surface2":     "#5b6078",
    "text":         "#cad3f5",
    "rosewater":    "#f4dbd6",
    "lavender":     "#b7bdf8",
    "red":          "#ed8796",
    "peach":        "#f5a97f",
    "yellow":       "#eed49f",
    "green":        "#a6da95",
    "teal":         "#8bd5ca",
    "blue":         "#8aadf4",
    "flamingo":     "#f0c6c6",
    "mauve":        "#c6a0f6",
        }

layouts = [
    layout.MonadTall(
        margin=6,
        border_width=2,
        border_normal=catppuccin['crust'],
        border_focus=catppuccin['mauve'],
        ),
    layout.Columns(
        margin=6,
        border_width=1,
        border_normal=catppuccin['crust'],
        border_focus=catppuccin['mauve'],
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(
    #     margin=4,
    #     border_width=2,
    #     border_normal=catppuccin['crust'],
    #     border_focus=catppuccin['mauve'],
    #     ),
    # layout.Matrix(),
    layout.MonadWide(
        margin=6,
        border_width=1,
        border_normal=catppuccin['crust'],
        border_focus=catppuccin['mauve'],
        ),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Mouse callback functions
def launch_menu():
    qtile.cmd_spawn("rofi -show drun -show-icons")

def open_rofi():
    qtile.cmd_spawn("rofi -show drun -show-icons")

widget_defaults = dict(
    font="FiraCode Nerd Font Bold",
    fontsize=13,
    padding=2,
    foreground=catppuccin["base"],
    background=catppuccin["base"],
)

extension_defaults = widget_defaults.copy()

def get_widgets():
    widgets = [
        # widget.TextBox(
        #     text=" 󰣇 ",
        #     mouse_callbacks={"Button1": open_rofi},
        #     fontsize=13,
        #     background=catppuccin["base"],
        #     foreground=catppuccin["mauve"],
        #     margin=4,
        #     ),
        widget.CurrentLayoutIcon(
            scale=0.5,
            foreground=catppuccin['mauve'],
            use_mask=True,
            padding=10,
            ),
        widget.GroupBox(
            fontsize=12,
            rounded=False,
            center_aligned=True,
            disable_drag=True,
            borderwidth=3,
            highlight_method='text',
            active=catppuccin['surface2'],
            inactive=catppuccin['surface0'],
            highlight_color=catppuccin['mauve'],
            this_current_screen_border=catppuccin['mauve'],
            this_screen_border=catppuccin['base'],
            other_screen_border=catppuccin['base'],
            other_current_screen_border=catppuccin['base'],
            urgent_border=catppuccin['red']
            ),
        widget.Spacer(
            length=5,
            background=catppuccin['base'],
            ),
        widget.Prompt(
            foreground=catppuccin['text'],
            cursorblink=0.9,
            prompt='Run: '
            ),
        widget.Spacer(
            length=1,
            background=catppuccin['base'],
            ),
        widget.WindowName(
            fontsize=12,
            foreground=catppuccin['surface0'],
            padding=5,
            max_chars=25,
            ),
        widget.Spacer(
            length=1,
            background=catppuccin['base'],
            ),
        widget.Mpd2(
            play_states={'pause': '', 'play': '', 'stop': ''},
            status_format='{play_status} {artist} - {title}',
            port='8820',
            host='192.168.100.252',
            no_connection='Offline',
            foreground=catppuccin['flamingo'],
            padding=5,
            ),
        widget.Spacer(
            length=1,
            background=catppuccin['base'],
            ),
        widget.Memory(
            format=" {MemUsed:.0f}{mm}",
            foreground=catppuccin['mauve'],
            background=catppuccin['base'],
            padding=5,
            ),
        # widget.UPowerWidget(
        #     fill_charge=catppuccin['mauve'],
        #     fill_critical=catppuccin['mauve'],
        #     fill_low=catppuccin['mauve'],
        #     fill_normal=catppuccin['mauve'],
        #     foreground=catppuccin['mauve'],
        #     background=catppuccin['base'],
        #     padding=5,
        #     ),
        widget.CPU(
            format=" {load_percent}%",
            foreground=catppuccin['blue'],
            background=catppuccin['base'],
            padding=5,
            ),
        widget.Spacer(
            length=1,
            background=catppuccin['base'],
            ),
        widget.DF(
            foreground=catppuccin['teal'],
            format=' {f}{m}',
            measure='G',
            partition='/',
            update_interval=60,
            visible_on_warn=False,
            padding=5,
            ),
        widget.Spacer(
            length=1,
            background=catppuccin['base'],
            ),
        widget.Wlan(
            foreground=catppuccin['green'],
            format=' {essid}',
            disconnected_message=' Offline',
            interface='wlp0s18f0u2u3',
            padding=5,
            ),
        widget.Spacer(
            length=1,
            background=catppuccin['base'],
            ),
        widget.PulseVolume(
            fmt=" {}",
            foreground=catppuccin['yellow'],
            background=catppuccin['base'],
            padding=5,
            ),
        widget.Spacer(
            length=1,
            background=catppuccin['base'],
            ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=catppuccin["peach"],
            background=catppuccin["base"],
            padding=5,
            ),
        widget.Spacer(
            length=1,
            background=catppuccin['base'],
            ),
        widget.ScriptExit(
            foreground=catppuccin['red'],
            exit_script='~/.config/qtile/shutdown.sh',
            default_text='󰐦 ',
            countdown_format='{} ',
            countdown_start=6,
            padding=5,
            ),
            ]
    return widgets

screens = [
    Screen(
        top=bar.Bar(
            get_widgets(),
            26,
            background=catppuccin['base'],
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
