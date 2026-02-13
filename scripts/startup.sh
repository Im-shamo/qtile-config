#!/usr/bin/env bash

/usr/lib/polkit-kde-authentication-agent-1 &    # Polkit Agent
dunst &                                         # Notification

if [[ "$XDG_SESSION_TYPE" == "x11" ]]; then
  ~/.config/qtile/scripts/xrandr_setup.sh &
  picom && sleep 1 &                            # Compositor
  powerkit && sleep 1 &                         # Power management
  deskflow && sleep 1 &                         # Input device sharing

elif [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
  ~/.config/qtile/scripts/wlr-randr_setup.sh &
  swayidle -w \     # session lock
    timeout 300 'swaylock -f -i ~/Pictures/current-wallpaper' \
    before-sleep 'swaylock -f -i ~/Pictures/current-wallpaper' &
fi

~/.config/qtile/scripts/wallpaper_changer.sh &  # Waypaper

# Applets
udiskie -t --appindicator && sleep 1 &          # Disk mounting
nm-applet && sleep 1 &                          # Network Manager
blueman-applet && sleep 1 &                     # Bluetooth
