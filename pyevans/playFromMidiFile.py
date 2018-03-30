from miditools.loader import *

if __name__ == '__main__':
    import os
    pathIn  = (os.path.dirname(os.path.abspath(__file__)))
    pathIn  = os.path.dirname(pathIn)
    # convertMidiFileToMonoMelody(pathIn + "/resources/bwv772.mid")
    # convertMidiFileToMonoMelody(pathIn + "/resources/PinkPanther2.mid")
    convertMidiFileToMonoMelody(pathIn + "/resources/Bach_How_Brightly_Shines_Morning_Star_BWV1.mid")
