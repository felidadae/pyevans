"""
	@TODO way of inputing result
	# l = ""
	# ch = sys.stdin.read(1)
	# while ord(ch) != 13:
	# 	l += ch
	# 	print(ch, end="")
	# 	ch = sys.stdin.read(1)
	# print (l)	

	Keyboard codes
	a = 97 b = 98 c = 99 d = 100 e = 101 f = 102 g = 103
	h = 104 i = 105 j = 106 k = 107 l = 108 m = 109 n = 110
	o = 111 p = 112 q = 113 r = 114 s = 115 t = 116 u = 117
	v = 118 w = 119 x = 120 y = 121 z = 122
	return = 13 escape = 27 space bar = 32
"""
import sys
import termios
import contextlib
from collections import namedtuple

import miditools.connector as midiconnector
midiconnector.setMidoBackend()
output=midiconnector.getMidiOutput()

from miditools.player import MonoMelodyPlayer
from composers.random import composeRandom, RangeMinMax

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


@contextlib.contextmanager
def raw_mode(file):
	old_attrs = termios.tcgetattr(file.fileno())
	new_attrs = old_attrs[:]
	new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
	try:
		termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
		yield
	finally:
		termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


def main():
	print (bcolors.OKGREEN + 'To get new melody press c' + bcolors.ENDC)
	print (bcolors.OKGREEN + 'To repeat melody press SPACE' + bcolors.ENDC)
	print (bcolors.OKGREEN + 'To see answer press v' + bcolors.ENDC)
	print (bcolors.OKGREEN + 'To quit press q' + bcolors.ENDC)
	print ("")

	monoMelodyPlayer = MonoMelodyPlayer(output)
	# import IPython
	# IPython.embed()

	with raw_mode(sys.stdin):
		try:
			while True:
				ch = sys.stdin.read(1)
				if ord(ch) == 99:
					if len(monoMelodyPlayer.last_):
						monoMelodyPlayer.last_.printColorfullyToTerminus()
					print("")
					print (bcolors.WARNING + "New melody" + bcolors.ENDC)
					newMonoMelody = composeRandom(
						Nnotes      = 5,
						rangeLength = RangeMinMax(0.4, 1.0),
						rangeFreq   = RangeMinMax(60, 80),
						maxInterval = 5
					)
					monoMelodyPlayer.set(newMonoMelody)
					monoMelodyPlayer.play(ifPrintDotsToStdout=True)
				if ord(ch) == 32:
					monoMelodyPlayer.play(ifPrintDotsToStdout=True)
				if ord(ch) == 118:
					monoMelodyPlayer.last_.printColorfullyToTerminus()

				if not ch or ch == chr(113):
					break
				# print '%02x' % ord(ch),
		except (KeyboardInterrupt, EOFError):
			pass
