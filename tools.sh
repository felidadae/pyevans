font0="$labs"/MusicalLab/resources/FluidR3GM2-2.SF2
# font0="$scriptPath"/resources/HSSynth.sf2

function run_fluidsynth_alsa {
	if [[ $(pgrep fluidsynth) == "" ]]; then
		fluidsynth --server --no-shell --audio-driver=alsa \
			--reverb=0.0 --chorus=0.0 --gain=0.3 -o audio.period-size=512 \
			"$font0" \
			&>/tmp/fluidsynth.out &
	fi
}
