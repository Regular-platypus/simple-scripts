pkg install busybox termux-services

chmod -R 777 /storage/emulated/0/.server

cat <<EOF >$HOME/.config/termux-services/ftpd.properties
enabled=true
port=8021
readonly=false
dir=/storage/emulated/0/.server
EOF

sv-enable ftpd
sv up ftpd

termux-reload-settings

echo "FTP server setup complete!"
