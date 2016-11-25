"""
Usage:
import miditools.midiconnector as midiconnector
midiconnector.setMidoBackend()
output=midiconnector.getMidiOutput()
"""

from sys import platform as _platform
import mido

JACK_MIDI=0

def setMidoBackend():
	"""
		library mido sends MIDI 
		to some other application running;
		here we set to what;
	"""
	if JACK_MIDI == 1:
		if _platform == "linux" or _platform == "linux2":
			mido.set_backend('mido.backends.rtmidi/UNIX_JACK')
		elif _platform == "darwin":
			# OS X
			pass
		elif _platform == "win32":
			# Windows...
			pass

def getMidiOutput():
	"""
		returns mido reference to midiSink
	"""
	print(mido.get_output_names()) 
	output = mido.open_output( mido.get_output_names()[1] )
	return output
