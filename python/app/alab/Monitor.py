#!  /usr/bin/env python

from fl.wx.TextTrace import TextTrace
from fl.wx.ScopeControl import ScopeControl as ScopePage
from fl.wx.FftControl import FftControl as FftPage
from fl.wx.WaterfallControl import WaterfallControl as WaterfallPage

import wx

#   ============================================================================
class Monitor(wx.Notebook):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent, size=None):
    #   ------------------------------------------------------------------------
        super(Monitor, self).__init__(parent, size=size)
        self.xInitGui()
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.in_scope = ScopePage(self, channels=2)
        self.AddPage(self.in_scope, "Scope")
        self.in_fft = FftPage(self)
        self.AddPage(self.in_fft, "FFT IN")
        self.in_waterfall = WaterfallPage(self)
        self.AddPage(self.in_waterfall, "Waterfall IN")
        self.out_fft = FftPage(self)
        self.AddPage(self.out_fft, "FFT OUT")
        self.out_waterfall = WaterfallPage(self)
        self.AddPage(self.out_waterfall, "Waterfall OUT")

    #   ------------------------------------------------------------------------
    def InputProbes(self):
    #   ------------------------------------------------------------------------
        return [(self.in_scope.Sink(), 0), (self.in_fft.Sink(), 0), 
            (self.in_waterfall.Sink(), 0)]
    
    #   ------------------------------------------------------------------------
    def OutputProbes(self):
    #   ------------------------------------------------------------------------
        return [(self.in_scope.Sink(),1), 
            (self.out_fft.Sink(), 0), (self.out_waterfall.Sink(), 0)]
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        #self.trace.ProcessCommand(sender, command)
        pass
    
    

#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    print "Hello, Monitor!"
    