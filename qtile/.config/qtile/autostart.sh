#!/bin/sh

redshift &
caffeine &
xcape -e 'Super_L=Alt_L|F1'
nitrogen --restore &
nowater -T
nm-applet &
blueman-applet &
# deadd-notification-center &
picom &
/opt/clash-for-windows-bin/cfw &
xfce4-clipman &
# mate-power-manager &
udiskie &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
xfce4-power-manager &
cfw &
