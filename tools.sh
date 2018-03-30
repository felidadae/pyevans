fontPiano="$labs"/MusicalLab/resources/FluidR3GM2-2.SF2
fontSynth="$scriptPath"/resources/HSSynth.sf2

function run_fluidsynth_alsa {
	local fontFile=${1}
	if [[ $(pgrep fluidsynth) == "" ]]; then
		fluidsynth --server --no-shell --audio-driver=alsa \
			--reverb=0.0 --chorus=0.0 --gain=0.3 -o audio.period-size=512 \
			"$fontFile" \
			&>/tmp/fluidsynth.out &
	fi
}
