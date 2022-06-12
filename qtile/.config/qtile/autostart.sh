#!/bin/sh

redshift &
caffeine &
xcape -e 'Super_L=Alt_L|F1'
nitrogen --restore &
nm-applet &
blueman-applet &
# deadd-notification-center &
picom &
/opt/clash-for-windows-bin/cfw &
"/opt/xdman/jre/bin/java" -Xmx1024m -jar "/opt/xdman/xdman.jar" -m &
xfce4-clipman &
# mate-power-manager &
udiskie &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
xfce4-power-manager &
