#!  /usr/bin/env python

from gnuradio import gr

#   ============================================================================
class AnySource(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, controller, sources):
    #   ------------------------------------------------------------------------
        super(AnySource, self).__init__()
        self.controller = controller
        self.xInit(sources)
    
    
    #   ------------------------------------------------------------------------
    def Sources(self):
    #   ------------------------------------------------------------------------
        return self.sources.keys()
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        print "AnySource.ProcessCommand", sender, command
        if not sender in self.sources:
            print "AnySource.ProcessCommand: Unknown destination \"%s\"" % (
                sender)
        if command[0] == "mute" and command[1] == "false":
            for source in self.sources.values():
                source.ProcessCommand(("mute", "true"))
        return self.sources[sender].ProcessCommand(command)
        
    
    #   ------------------------------------------------------------------------
    def Connect(self):
    #   ------------------------------------------------------------------------
        print "AnySource.Connect"
        if len(self.sources) == 1:
            source = self.sources.values()[0]
            source.Connect()
            self.controller.connect((source.Outport(),0), (self.mixer,0))
            return
        index = 0
        for source in self.sources.values():
            source.Connect()
            self.controller.connect(source.Outport(), (self.mixer,index))
            index += 1
            
    #   ------------------------------------------------------------------------
    def Outport(self):
    #   ------------------------------------------------------------------------
        return (self.mixer,0)
    
    #   ------------------------------------------------------------------------
    def xInit(self, sources):
    #   ------------------------------------------------------------------------
        self.sources = sources
        if not self.sources:
            print "AnySource.xInit: ERROR: Building flowgraph without sources."
            return
        if len(self.sources) == 1:
            self.mixer = gr.multiply_const_vff((1, ))
        else:
            self.mixer = gr.add_vff(1)
            
            
        
    
    