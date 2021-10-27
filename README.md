# openrgb_pywal.py
Python Script that sets OpenRGB Ledstripe to pywal colors

needs openrgb server running (simply click the button to start OpenRGB Server in the GUI)

OR 

use a systemd unit file

[Unit]
Description=Run openrgb server
After=network.target lm_sensors.service

/usr/lib/systemd/system/openrgb.service

[Service]
Type=simple
RemainAfterExit=yes
ExecStart=/usr/bin/openrgb --server
ExecStop=/usr/bin/killall openrgb
Restart=always

[Install]
WantedBy=multi-user.target


systemctl daemon-reload
systemctl start openrgb
systemctl enable openrgb


i trigger the script with this (also let's me set a wallpaper):
wallpaper='wal --backend colorz -i "$(sxiv -tfbo ~/.local/share/wallpapers)" && ~/.config/wal/led.py'

