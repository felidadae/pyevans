#!/bin/bash
scriptPath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$scriptPath"
source $scriptPath/tools.sh

cd $scriptPath
if [[ $(pgrep fluidsynth) == "" ]]; then
	run_fluidsynth_alsa resources/HSSynth.sf2
	sleep 0.5
fi
python3 pyevans/main.py
killall fluidsynth
