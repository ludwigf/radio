#!  /usr/bin/env python

from gnuradio import audio
from gnuradio import gr

#   ============================================================================
class FileSourceAdapter(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, controller, filename="", muted=True):
    #   ------------------------------------------------------------------------
        super(FileSourceAdapter, self).__init__()
        self.controller = controller
        self.samprate = controller.samprate
        if filename:
            self.source = gr.file_source(gr.sizeof_float, filename, True)
        else:
            self.source = gr.null_source(gr.sizeof_float)
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
        print "FileSourceAdapter.ProcessCommand", command
        if command[0] == "mute":
            self.mute.set_mute(command[1]=="true")
            return
        if command[0] == "filename":
            if command[1]:
                self.source = gr.file_source(gr.sizeof_float, command[1], True)
            else:
                self.source = gr.null_source(gr.sizeof_float)
            return
        print "FileSourceAdapter.ProcessCommand: Unknown command \"%s\"" % (
            command[0])
                
            
            