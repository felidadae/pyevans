"""
Usage:
import miditools.midiconnector as midiconnector
midiconnector.setMidoBackend()
output=midiconnector.getMidiOutput()
"""

from sys import platform as _platform
import mido

JACK_MIDI=1

def setMidoBackend():
    """
        library mido sends MIDI 
        to some other application running;
        here we set to what;
    """
    if _platform == "linux" or _platform == "linux2":
        mido.set_backend('mido.backends.rtmidi')
    elif _platform == "darwin":
        # OS X
        pass
    elif _platform == "win32":
        # Windows
        pass

def getMidiOutput():
    """
        returns mido reference to midiSink
    """
    fluid_outputs = [output for output in mido.get_output_names() 
                            if "FLUID" in output]
    assert(len(fluid_outputs) > 0, "fluidsynth input midi input port is not available")
    fluid_output = fluid_outputs[0]
    output = mido.open_output(fluid_output)
    return output
