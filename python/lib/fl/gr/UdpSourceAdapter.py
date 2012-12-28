#!  /usr/bin/env python

from gnuradio import audio
from gnuradio import gr

#   ============================================================================
class UdpSourceAdapter(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, controller, address="", muted=True):
    #   ------------------------------------------------------------------------
        super(UdpSourceAdapter, self).__init__()
        self.controller = controller
        self.source = self.xUdpSource(address) or self.xNullSource()
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
    def xUdpSource(self, address):
    #   ------------------------------------------------------------------------
        try:
            host, port = address.split(":")
        except:
            print "UdpSourceAdapter.xUdpSource: Bad address \"%s\"" % address
            return None
        try:
            return gr.udp_source(
                gr.sizeof_float, host, int(port), 1472, False, True)
        except:
            print "UdpSourceAdapter.xUdpSource: Blown creation \"%s\"" % address
            return None
    
    #   ------------------------------------------------------------------------
    def xNullSource(self):
    #   ------------------------------------------------------------------------
        return gr.null_source(gr.sizeof_float)
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, command):
    #   ------------------------------------------------------------------------
        print "UdpSourceAdapter.ProcessCommand", command
        if command[0] == "mute":
            self.mute.set_mute(command[1]=="true")
            return
        if command[0] == "address":
            self.source = self.xUdpSource(command[1]) or self.xNullSource()
            print "UdpSourceAdapter: Created", self.source
            return
        print "FileSourceAdapter.ProcessCommand: Unknown command \"%s\"" % (
            command[0])
                
            
            