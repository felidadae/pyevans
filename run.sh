#!/bin/bash
scriptPath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

function run_fluidsynth_alsa {
	if [[ $(pgrep fluidsynth) == "" ]]; then
		fluidsynth --server --no-shell --audio-driver=alsa \
			--reverb=0.1 --chorus=0.1 --gain=0.3 -o audio.period-size=512 \
			"$scriptPath"/resources/HSSynth.sf2 \
			&>/tmp/fluidsynth.out &
	fi
}

cd $scriptPath
if [[ $(pgrep fluidsynth) == "" ]]; then
	run_fluidsynth_alsa
	sleep 0.5 
fi
python3 pyevans/main.py
killall fluidsynth
