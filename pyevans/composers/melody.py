from collections import namedtuple



Note = namedtuple('Note', ['frequency', 'length'])
class MonoMelody(object):
	def __init__(self):
		self.notes_ = []

	def addNote(self, note: Note):
		self.notes_.append(note)

	def __str__(self):
		f_ = [f.frequency for f in self.notes_]
		f_ = list(map(lambda e: e-f_[0], f_))
		return str(f_)
	def printColorfullyToTerminus(self):
		intervals = self.getIntervals()
		intervalsWithArrows = []
		plus_  = '↑ '
		minus_ = '↓ '
		zero_  = '•'
		for interval in intervals:
			if interval > 0:
				intervalsWithArrows.append( plus_  + str(interval))
			elif interval < 0:
				intervalsWithArrows.append( minus_ + str(abs(interval)))
			else:
				intervalsWithArrows.append( zero_ + str(interval))
		print ( "☼  " +  "  ".join(intervalsWithArrows))

	def __len__(self):
		return len(self.notes_)
	def __getitem__(self, position):
		return self.notes_[position]

	def getIntervals(self):
		intervals = []
		f_ = [f.frequency for f in self.notes_]
		for i in range(1,len(f_)):
			intervals.append(f_[i]-f_[i-1])
		return intervals
