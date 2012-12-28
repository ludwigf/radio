#!  /usr/bin/env python

from gnuradio import audio
from gnuradio import gr

#   ============================================================================
class AudioSourceAdapter(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, controller, muted=True):
    #   ------------------------------------------------------------------------
        super(AudioSourceAdapter, self).__init__()
        self.controller = controller
        self.samprate = controller.samprate
        self.source = audio.source(self.samprate, "", True)
        self.mute = gr.mute_ff(muted)
        
        
    #   ------------------------------------------------------------------------
    def Outport(self):
    #   ------------------------------------------------------------------------
        return (self.mute,0)
    
    
    #   ------------------------------------------------------------------------
    def Source(self):
    #   ------------------------------------------------------------------------
        return self.source
    
    
    #   ------------------------------------------------------------------------
    def Connect(self):
    #   ------------------------------------------------------------------------
        self.controller.connect((self.source,0), (self.mute,0))
        
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, command):
    #   ------------------------------------------------------------------------
        print "AudioSourceAdapter.ProcessCommand", command
        if command[0] == "mute":
            self.mute.set_mute(command[1]=="true")
            
            