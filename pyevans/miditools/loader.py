from mido import MidiFile, MetaMessage
import time

from miditools.connector import *
setMidoBackend()
port = getMidiOutput()



def findTrackWithMaxEvents(tracks):
	import operator
	index, value = max(
		enumerate([len(track) for track in tracks]), 
			key=operator.itemgetter(1))
	return index

def findTrackWithMaxEventsWithout0Time(tracks):
	"""
	count accords as one
	"""
	imax_, max_ = (0,0) 
	for it, track in enumerate(tracks):
		Nevents = 0
		for message in track:
			if (message.time != 0):
				Nevents+=1
		if Nevents > max_:
			imax_, max_ = (it, Nevents)
	return imax_

def convertMidiFileToMonoMelody(filePath):
	midfref = MidiFile(filePath)
	tracks = midfref.tracks
	indexOfChoosenTrack = findTrackWithMaxEvents(tracks) 

	for message in tracks[indexOfChoosenTrack]:
		if not isinstance(message, MetaMessage):
			if (message.type != 'note_on' and 
					message.type != 'note_off'):
				continue

			# if (message.time == 0 ):
			#  	continue

			print (message)
			time.sleep(message.time/400.0)
			port.send(message)
