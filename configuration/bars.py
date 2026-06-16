from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget

from configuration.variables import *
from configuration.widgets import arrow_right, my_widgets


class MyBars:
    """
    Custom bar for screens

    Xorg:

    - main_bar_x11_desktop
    - main_bar_x11_laptop
    - small_screen_bar_x11_desktop
    - small_screen_bar_x11_laptop

    Wayland:

    - main_bar_wayland_desktop
    - main_bar_wayland_laptop
    - small_main_bar_wayland_desktop
    - small_main_bar_wayland_laptop

    Independent:

    - secondary_bar
    """

    def base_bar_left(self) -> list[widget]:
        return [
            widget.CurrentLayout(
                mode="icon",
                mouse_callbacks={"Button1": lazy.next_layout()}
            ),
            my_widgets.group_box(),
            widget.WindowName()
            ]

    def base_bar_right(self) -> list[widget]:
        return [
            widget.TextBox(**arrow_right),
            my_widgets.wallpaper_switcher(**arrow_right),
            widget.Net(
                font=mono_font,
                format=" {down:^5.1f}{down_suffix:<2}",
                background=colours["BLUE"],
                **arrow_right
            ),
            widget.Net(
                font=mono_font,
                format=" {up:^5.1f}{up_suffix:<2}",
                background=colours["DARK_GREEN"],
                **arrow_right
            ),
            widget.NetGraph(
                background=colours["GREEN"],
                graph_color=colours["BLUE"],
                type="line",
                line_width=2,
                **arrow_right,
            ),
            my_widgets.volume(),
            my_widgets.microphone(**arrow_right),
            widget.Clock(
                format="%d/%m/%Y %a %I:%M %p",
                background=colours["LIGHT_BLUE"],
                **arrow_right
            ),
            my_widgets.power_button(),
            widget.Spacer(length=5)
            ]

    def base_bar_right_small(self) -> list[widget]:
        return [
            widget.TextBox(**arrow_right),
            my_widgets.wallpaper_switcher(**arrow_right),
            my_widgets.volume(**arrow_right),
            widget.Clock(
                format="%d/%m/%Y %a %I:%M %p",
                background=colours["LIGHT_BLUE"],
                **arrow_right
            ),
            my_widgets.power_button(),
            widget.Spacer(length=5)
            ]

    def base_bar_right_secondary(self) -> list[widget]:
        return [
            widget.TextBox(**arrow_right),
            widget.Clock(
                format="%d/%m/%Y %a %I:%M %p",
                background=colours["LIGHT_BLUE"],
                **arrow_right
            ),
            my_widgets.power_button(),
            widget.Spacer(length=5)
            ]


    def main_bar_x11_desktop(self):
        widgets = self.base_bar_left() + [widget.Prompt(), widget.Systray()] + self.base_bar_right()
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )

    def main_bar_x11_laptop(self):
        widgets = self.base_bar_left() + [widget.Prompt(), widget.Systray()] + self.base_bar_right()
        widgets.insert(
            -2,
            widget.Battery(
                format="  {percent:.0%}",
                background=colours["BLUE"],
                **arrow_right
            )
        )
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )

    def small_screen_bar_x11_desktop(self):
        widgets = self.base_bar_left() + [widget.Prompt(), widget.Systray()] + self.base_bar_right_small()
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )

    def small_screen_bar_x11_laptop(self):
        widgets = self.base_bar_left() + [widget.Prompt(), widget.Systray()] + self.base_bar_right_small()
        widgets.insert(
            -2,
            widget.Battery(
                format="  {percent:.0%}",
                background=colours["BLUE"],
                **arrow_right
            )
        )
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )

    def main_bar_wayland_desktop(self):
        widgets = self.base_bar_left() + [widget.Prompt(), widget.StatusNotifier(icon_theme="Adwaita")] + self.base_bar_right()
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )

    def main_bar_wayland_laptop(self):
        widgets = self.base_bar_left() + [widget.Prompt(), widget.StatusNotifier(icon_theme="Adwaita")] + self.base_bar_right()
        widgets.insert(
            -2,
            widget.Battery(
                format="  {percent:.0%}",
                background=colours["BLUE"],
                **arrow_right
            )
        )
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )

    def small_main_bar_wayland_laptop(self):
        widgets = self.base_bar_left() + [widget.Prompt(), widget.StatusNotifier(icon_theme="Adwaita")] + self.base_bar_right()
        widgets.insert(
            -2,
            widget.Battery(
                format="  {percent:.0%}",
                background=colours["BLUE"],
                **arrow_right
            )
        )
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )

    def small_main_bar_wayland_desktop(self):
        widgets = self.base_bar_left() + [widget.Prompt(), widget.StatusNotifier(icon_theme="Adwaita")] + self.base_bar_right_small()
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )

    def secondary_bar(self):
        widgets = self.base_bar_left() + self.base_bar_right_secondary()
        return bar.Bar(
            widgets,
            size=bar_size,
            opacity=bar_opacity,
            margin=bar_margin
        )


my_bars = MyBars()
