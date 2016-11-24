import time
import random
from collections import namedtuple

from composers.melody import MonoMelody, Note



def subWithMin(a, b, min_):
	if a-b < min_:
		return min_
	else:
		return a-b
def addWithMax(a, b, max_):
	if a+b > max_:
		return max_
	else:
		return a+b



RangeMinMax=namedtuple('Range', 'min max')
def composeRandom( 
	Nnotes, 
	rangeLength: RangeMinMax, rangeFreq: RangeMinMax, 
	maxInterval) -> MonoMelody:
	"""
		@Nnotes			<-	1...
		@rangeLength	<-	.min .max
		@rangeFreq		<-	.min .max
		@maxInterval	<-	1...
	"""

	# shortcuts
	maxI = maxInterval

	melody = MonoMelody()

	# first rand first note
	f = random.randint(rangeFreq.min, rangeFreq.max)
	lAll = 0.0
	for i in range(0, Nnotes):
		if i>0:
			f = random.randint( 
				subWithMin(melody[i-1].frequency, maxI, rangeFreq.min),
				addWithMax(melody[i-1].frequency, maxI, rangeFreq.max))
		l = random.uniform(rangeLength.min, rangeLength.max)
		melody.addNote(Note(frequency=f, length=l))
		lAll = lAll + l
	return melody
