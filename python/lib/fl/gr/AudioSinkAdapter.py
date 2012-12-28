#!  /usr/bin/env python

from gnuradio import audio
from gnuradio import gr

#   ============================================================================
class AudioSinkAdapter(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, controller, muted=True):
    #   ------------------------------------------------------------------------
        super(AudioSinkAdapter, self).__init__()
        self.controller = controller
        self.samprate = controller.samprate
        self.mute = gr.mute_ff(muted)
        self.sink = audio.sink(self.samprate, "", True)
        
        
    #   ------------------------------------------------------------------------
    def Inport(self):
    #   ------------------------------------------------------------------------
        return (self.mute,0)
    
    
    #   ------------------------------------------------------------------------
    def Sink(self):
    #   ------------------------------------------------------------------------
        return self.sink
    
    
    #   ------------------------------------------------------------------------
    def Connect(self):
    #   ------------------------------------------------------------------------
        self.controller.connect((self.mute,0), (self.sink,0))
        print "Connected (%s,0) to (%s,0)" % (self.mute, self.sink)
        
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, command):
    #   ------------------------------------------------------------------------
        print "AudioSinkAdapter.ProcessCommand", command
        if command[0] == "mute":
            self.mute.set_mute(command[1]=="true")
            
            