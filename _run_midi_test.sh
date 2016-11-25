#!/bin/bash
kill -9 $(pgrep fluidsynth);
source tools.sh
run_fluidsynth_alsa;
sleep 1;
if [[ $1 == 1 ]]; then
	python3 pyevans/playFromMidiFile.py
fi
