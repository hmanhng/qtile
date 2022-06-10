import os

from libqtile.bar import Bar

from libqtile import widget
from libqtile.lazy import lazy

from colors import gruvbox

bar = Bar([
    widget.TextBox(
        text='',
        foreground='#3490bb',
        fontsize=24,
        mouse_callbacks={"Button1": lazy.group['scratchpad'].dropdown_toggle('term')},
    ),
    widget.GroupBox(
        disable_drag=True,
        active='#ffa2a2',
        inactive='#6e6e6e',
        highlight_method='line',
        block_highlight_text_color='#ffa643',
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg'],
        fontsize=17,
    ),
    widget.Spacer(
        length=10,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
        background = gruvbox['dark-yellow'],
        padding = 0,
        scale = 0.7
    ),
    widget.CurrentLayout(
        background=gruvbox['dark-yellow'],
        padding=5,
        fontsize=16,
    ),
    widget.WindowCount(
        text_format='缾 {num}',
        background=gruvbox['magenta'],
        fontsize=16,
        show_zero=True,
    ),

    widget.WindowName(
        foreground='#ffffff',
        fontsize=16,
    ),

    # Spacer(length=100),

    # Spacer(length=10),
    widget.CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['dark-cyan']),
    widget.Memory(
        format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['dark-magenta']),
    widget.Net(
        format='龍 {down} ↓↑ {up}',
        background=gruvbox['dark-blue'],
    ),
    # widget.Wlan(
    #     background='#ffc1c1',
    #     interface='wlp0s20f3',
    #     fmt='  {}',
    #     format='{essid} {percent:2.0%}',
    # ),
    widget.Volume(
        fmt=' {}',
        background='#a8bdbe',
        volume_up_command='pactl -- set-sink-volume 0 +5%',
        volume_down_command='pactl -- set-sink-volume 0 -5%',
        mouse_callbacks={"Button3": lazy.spawn('pavucontrol')},
        ),
    widget.Backlight(
        background='#a8bdbe',
        fmt=' {}',
        backlight_name='intel_backlight',
        change_command='light -S {0}',
    ),
    widget.Clock(
        background=gruvbox['cyan'],
        format=' %Y-%m-%d %a %H:%M'),
    # Prompt(foreground=gruvbox['fg']),
    widget.Systray(
        # padding=10,
        icon_size=21,
        background=gruvbox['bg'],
    ),
    widget.Spacer(length=10, background=gruvbox['bg']),
],
    # margin=[0, 10, 5, 10],
    background=gruvbox['bg'],
    opacity=1,
    size=25,
)
