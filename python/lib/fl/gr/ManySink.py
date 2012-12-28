#!  /usr/bin/env python

from gnuradio import gr

#   ============================================================================
class ManySink(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, controller, sinks):
    #   ------------------------------------------------------------------------
        super(ManySink, self).__init__()
        self.controller = controller
        self.xInit(sinks)
    
    
    #   ------------------------------------------------------------------------
    def Sinks(self):
    #   ------------------------------------------------------------------------
        return self.sinks.keys()
    

    #   ------------------------------------------------------------------------
    def Inport(self):
    #   ------------------------------------------------------------------------
        return (self.splitter, 0)
    
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, device, command):
    #   ------------------------------------------------------------------------
        print "ManySink.ProcessCommand", device, command
        if not device in self.sinks:
            print "ManySink.ProcessCommand: Unknown destination \"%s\"" % device
        return self.sinks[device].ProcessCommand(command)
        
    
    #   ------------------------------------------------------------------------
    def Connect(self):
    #   ------------------------------------------------------------------------
        print "ManySink.Connect"
        if len(self.sinks) == 1:
            sink = self.sinks.values()[0]
            sink.Connect()
            self.controller.connect((self.splitter,0),sink.Inport())
            return
        for sink in self.sinks.values():
            sink.Connect()
            self.controller.connect((self.splitter,0),sink.Inport())
            

    #   ------------------------------------------------------------------------
    def xInit(self, sinks):
    #   ------------------------------------------------------------------------
        self.sinks = sinks
        if not self.sinks:
            print "ManySink.xInit: ERROR: Building flowgraph without sinks."
            return
        self.splitter = gr.multiply_const_vff((1, ))
        