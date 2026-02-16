from libqtile import hook
import subprocess

from configuration.variables import *
from configuration.environment_varables import set_environment_variables

@hook.subscribe.startup_once
def startup_once():
    set_environment_variables()
    subprocess.Popen(
        scripts_dir / "startup.sh",
        start_new_session=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

