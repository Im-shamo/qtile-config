#!/usr/bin/env bash

/usr/lib/polkit-kde-authentication-agent-1 &    # Polkit Agent
dunst &                                         # Notification

if [[ "$XDG_SESSION_TYPE" == "x11" ]]; then
  ~/.config/qtile/scripts/xrandr_setup.sh &
  picom &                                       # Compositor
  sleep 1
  xscreensaver &                                # Screensaver
  sleep 1
  deskflow &                                    # Input device sharing
  sleep 1

elif [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
  ~/.config/qtile/scripts/wlr-randr_setup.sh &
  swayidle -w \                                 # session lock
    timeout 300 'swaylock -f -i ~/Pictures/current-wallpaper' \
    before-sleep 'swaylock -f -i ~/Pictures/current-wallpaper' &
fi

~/.config/qtile/scripts/wallpaper_changer.sh &  # Waypaper

# Applets
udiskie -t --appindicator &                     # Disk mounting
sleep 1
nm-applet &                                     # Network Manager
sleep 1
blueman-applet &                                # Bluetooth
