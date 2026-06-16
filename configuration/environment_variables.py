import os

def set_environment_variables():
    os.environ["QT_QPA_PLATFORMTHEME"] = "qt6ct"    # Theming
    os.environ["XDG_SESSION_DESKTOP"] = "qtile"     # Session

