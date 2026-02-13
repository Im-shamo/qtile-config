from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy

from configuration.variables import *
from configuration.keybinds import keys
from configuration.groups import groups

launch_command = {}

if qtile.core.name == "wayland":
    launch_command["clipse"] = f"{terminal} clipse"
    launch_command["btop"] = f"{terminal} btop"
    launch_command["term"] = f"{terminal}"
else:
    launch_command["clipse"] = f"{terminal} -class clipse clipse"
    launch_command["btop"] = f"{terminal} -class btop btop"
    launch_command["term"] = f"{terminal}"

groups.extend([
    ScratchPad(
        "terminals",
        [
            DropDown(
                "clipse",
                launch_command["clipse"],
                on_focus_lost_hide=False,
                opacity=1,
                height=0.4,
                width=0.4,
                x=0.3,
                y=0.3
            ),
            DropDown(
                "btop",
                launch_command["btop"],
                on_focus_host_hide=False,
                opacity=1,
                height=0.6,
                width=0.6,
                x=0.2,
                y=0.2
            ),
            DropDown(
                "term",
                launch_command["term"],
                on_focus_host_hide=False,
                opacity=1,
                height=0.5,
                width=0.5,
                x=0.25,
                y=0.25
            )

        ]
    )
])

keys.extend([
    Key([mod], 'v', lazy.group["terminals"].dropdown_toggle("clipse")),
    Key([mod], 's', lazy.group["terminals"].dropdown_toggle("btop")),
    Key([mod], 'p', lazy.group["terminals"].dropdown_toggle("term")),
])
