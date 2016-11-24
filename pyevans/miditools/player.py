import mido
import time
import random
import sys
from collections import namedtuple

from composers.melody import MonoMelody


class MonoMelodyPlayer(object):
	def __init__(self, midoSink):
		self.last_ = MonoMelody()
		self.midoSink_ = midoSink

	def play(self, ifPrintDotsToStdout=False):
		for note in self.last_:
			#turn on
			self.midoSink_.send(
				mido.Message('note_on', 
					note=note.frequency, velocity=80))

			#if print dot
			if ifPrintDotsToStdout:
				print('•', end="")
				if note == self.last_[-1]:
					print("")
				sys.stdout.flush()

			#sleep
			time.sleep(note.length)
			#turn off
			self.midoSink_.send(
				mido.Message(
					'note_off', 
					note=note.frequency, 
					velocity=80))

	def set(self, m: MonoMelody):
		self.last_ = m	
