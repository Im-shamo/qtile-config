from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget

from configuration.variables import *
from configuration.widgets import arrow_right, my_widgets


class MyBars:
    def __init__(self):
        self.colours = colours
        self.bar_margin = bar_margin
        self.size = 26
        self.opacity = 1

    def main_bar_x11_desktop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                widget.Net(
                    font=mono_font,
                    format=" {down:^5.1f}{down_suffix:<2}",
                    background=self.colours["BLUE"],
                    **arrow_right
                ),
                widget.Net(
                    font=mono_font,
                    format=" {up:^5.1f}{up_suffix:<2}",
                    background=self.colours["DARK_GREEN"],
                    **arrow_right
                ),
                widget.NetGraph(
                    background=self.colours["GREEN"],
                    graph_color=self.colours["BLUE"],
                    type="line",
                    line_width=2,
                    **arrow_right,
                ),
                my_widgets.volume(),
                my_widgets.microphone(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )

    def main_bar_x11_laptop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                widget.Net(
                    font=mono_font,
                    format=" {down:^5.1f}{down_suffix:<2}",
                    background=self.colours["BLUE"],
                    **arrow_right
                ),
                widget.Net(
                    font=mono_font,
                    format=" {up:^5.1f}{up_suffix:<2}",
                    background=self.colours["DARK_GREEN"],
                    **arrow_right
                ),
                widget.NetGraph(
                    background=self.colours["GREEN"],
                    graph_color=self.colours["BLUE"],
                    type="line",
                    line_width=2,
                    **arrow_right,
                ),
                my_widgets.volume(),
                my_widgets.microphone(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                widget.Battery(
                    format="  {percent:.0%}",
                    emoji=True,
                    background=self.colours["BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )

    def secondary_bar_x11(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.TextBox(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )

    def small_screen_bar_x11_desktop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                my_widgets.volume(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )

    def small_screen_bar_x11_laptop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.Systray(),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                my_widgets.volume(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                widget.Battery(
                    format="  {percent:.0%}",
                    emoji=True,
                    background=self.colours["BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )

    def main_bar_wayland_desktop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.StatusNotifier(icon_theme="Adwaita"),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                widget.Net(
                    font=mono_font,
                    format=" {down:^5.1f}{down_suffix:<2}",
                    background=self.colours["BLUE"],
                    **arrow_right
                ),
                widget.Net(
                    font=mono_font,
                    format=" {up:^5.1f}{up_suffix:<2}",
                    background=self.colours["DARK_GREEN"],
                    **arrow_right
                ),
                widget.NetGraph(
                    background=self.colours["GREEN"],
                    graph_color=self.colours["BLUE"],
                    type="line",
                    line_width=2,
                    **arrow_right,
                ),
                my_widgets.volume(),
                my_widgets.microphone(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )

    def main_bar_wayland_laptop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.StatusNotifier(icon_theme="Adwaita"),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                widget.Net(
                    font=mono_font,
                    format=" {down:^5.1f}{down_suffix:<2}",
                    background=self.colours["BLUE"],
                    **arrow_right
                ),
                widget.Net(
                    font=mono_font,
                    format=" {up:^5.1f}{up_suffix:<2}",
                    background=self.colours["DARK_GREEN"],
                    **arrow_right
                ),
                widget.NetGraph(
                    background=self.colours["GREEN"],
                    graph_color=self.colours["BLUE"],
                    type="line",
                    line_width=2,
                    **arrow_right,
                ),
                my_widgets.volume(),
                my_widgets.microphone(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                widget.Battery(
                    format="  {percent:.0%}",
                    emoji=True,
                    background=self.colours["BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )

    def secondary_bar_wayland(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.TextBox(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=1,
            margin=self.bar_margin
        )

    def main_bar_wayland_small(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.StatusNotifier(icon_theme="Adwaita"),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                my_widgets.volume(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                widget.Battery(
                    format="  {percent:.0%}",
                    emoji=True,
                    background=self.colours["BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )

    def main_bar_wayland_small_desktop(self):
        return bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    mouse_callbacks={"Button1": lazy.next_layout()}
                ),
                my_widgets.group_box(),
                widget.WindowName(),
                widget.Prompt(),
                widget.StatusNotifier(icon_theme="Adwaita"),
                widget.TextBox(**arrow_right),
                my_widgets.wallpaper_switcher(**arrow_right),
                my_widgets.volume(**arrow_right),
                widget.Clock(
                    format="%d/%m/%Y %a %I:%M %p",
                    background=self.colours["LIGHT_BLUE"],
                    **arrow_right
                ),
                my_widgets.power_button(),
                widget.Spacer(length=5),
            ],
            size=self.size,
            opacity=self.opacity,
            margin=self.bar_margin
        )


my_bars = MyBars()
