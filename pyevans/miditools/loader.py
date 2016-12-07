from mido import MidiFile, MetaMessage
import time
import operator

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

	previousMessage = 0 
	accord = []

	chTrack = tracks[indexOfChoosenTrack]
	for im, message in enumerate(chTrack):
		if not isinstance(message, MetaMessage):
			if (message.type != 'note_on' and message.type != 'note_off'):
				continue

			if (message.time == 0):
				accord.append(message)
				continue
			if (len(accord) > 0 and message.time > 0 and not(type(previousMessage) is int)):
				print (message)
				time.sleep(message.time/400.0)

				diff = [abs(previousMessage.note-m.note) for m in accord]
				index, value = min(enumerate(diff), key=operator.itemgetter(1))
				chn = accord[index]
				port.send(accord[index])
				cmessage = mido.Message('note_off', 
					note=chn.note, velocity=chn.velocity)
				port.send(cmessage)
				previousMessage = chn
				accord = []
				continue
				
			if (not(type(previousMessage) is int) and 
					abs(message.note - previousMessage.note) > 8 ):
				time.sleep(message.time/400.0)
				continue


			previousMessage = message
			print (message)
			time.sleep(message.time/400.0)
			port.send(message)
			cmessage = mido.Message('note_off', 
				note=message.note, velocity=message.velocity)
			port.send(cmessage)
