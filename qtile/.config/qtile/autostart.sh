#!/bin/sh

redshift &
caffeine &
xcape -e 'Super_L=Alt_L|F1'
# nitrogen --restore &
nowater -T
nm-applet &
blueman-applet &
picom &
"/opt/xdman/jre/bin/java" -Xmx1024m -jar "/opt/xdman/xdman.jar" -m &
xfce4-clipman &
udiskie &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
xfce4-power-manager &
cfw &
