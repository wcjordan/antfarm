#!/bin/bash
export DISPLAY=:20
Xvfb :20 -screen 0 640x480x16 &
x11vnc -passwd TestVNC -nonc -display :20 -N -forever -noxdamage &
PID_SUB=$!

echo -e "\n\n------------------ EXECUTE COMMAND ------------------"
echo "Executing command: '$@'"
exec "$@"

wait $PID_SUB