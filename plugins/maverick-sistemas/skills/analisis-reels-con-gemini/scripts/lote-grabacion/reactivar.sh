#!/bin/bash
# Mantiene al frente la ventana de Chrome indicada ($1) mientras se graba.
while true; do
  osascript -e "tell application \"Google Chrome\" to set index of window id $1 to 1" -e 'tell application "Google Chrome" to activate' >/dev/null 2>&1
  sleep 2
done
