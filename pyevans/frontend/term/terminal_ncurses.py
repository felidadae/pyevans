import sys
from collections import namedtuple

import miditools.connector as midiconnector
midiconnector.setMidoBackend()
output=midiconnector.getMidiOutput()

from miditools.player import MonoMelodyPlayer
from composers.random import composeRandom, RangeMinMax

import curses
from curses import wrapper as curses_wrapper

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def main(stdscr):
	monoMelodyPlayer = MonoMelodyPlayer(output)

	stdscr.clear()
	curses.noecho()
	def print_s(s, y,x):
		stdscr.addstr(y,x,s)
	print_s ('To get new melody press c',   0,0)
	print_s ('To repeat melody press SPACE',1,0)
	print_s ('To see answer press v',		2,0)
	print_s ('To quit press q',				3,0)

	while True:
		ch = stdscr.getkey() 
		if ord(ch) == 99:
			if len(monoMelodyPlayer.last_):
				monoMelodyPlayer.last_.printColorfullyToTerminus()
			print("")
			print_s (bcolors.WARNING + "New melody" + bcolors.ENDC)
			newMonoMelody = composeRandom(
				Nnotes      = 5,
				rangeLength = RangeMinMax(0.4, 1.0),
				rangeFreq   = RangeMinMax(60, 80),
				maxInterval = 5
			)
			monoMelodyPlayer.set(newMonoMelody)
			monoMelodyPlayer.play(ifPrintDotsToStdout=True)
		elif ord(ch) == 32:
			monoMelodyPlayer.play(ifPrintDotsToStdout=True)
		elif ord(ch) == 118:
			monoMelodyPlayer.last_.printColorfullyToTerminus()

		stdscr.refresh()

		if not ch or ch == chr(113):
			break

def run_main():
	curses_wrapper(main)
