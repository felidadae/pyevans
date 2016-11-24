from mido import MidiFile, MetaMessage
import time

from miditools.connector import *
setMidoBackend()
port = getMidiOutput()

def convertMidiFileToMonoMelody(filePath):
	midfref = MidiFile(filePath)

	for i, track in enumerate(midfref.tracks):
		print('Track {}: {}'.format(i, track.name))
		for message in track:
			if not isinstance(message, MetaMessage):
				print (message)
				time.sleep(message.time)
				port.send(message)

	# for message in MidiFile(midfref):
	# 	time.sleep(message.time)
	# 	if not isinstance(message, MetaMessage):
	# 		port.send(message)

