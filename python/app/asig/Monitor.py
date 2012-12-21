#!  /usr/bin/env python

from fl.wx.TextTrace import TextTrace
from fl.wx.ScopeControl import ScopeControl as ScopePage
from fl.wx.FftControl import FftControl as FftPage
from fl.wx.HistoControl import HistoControl as HistoPage
from fl.wx.WaterfallControl import WaterfallControl as WaterfallPage

import wx

#   ============================================================================
class Monitor(wx.Notebook):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
        super(Monitor, self).__init__(parent)
        self.xInitGui()
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.scope = ScopePage(self)
        self.AddPage(self.scope, "Scope")
        self.fft = FftPage(self)
        self.AddPage(self.fft, "FFT")
        self.histo = HistoPage(self)
        self.AddPage(self.histo, "Histogram")
        self.waterfall = WaterfallPage(self)
        self.AddPage(self.waterfall, "Waterfall")
        #self.trace = TextTrace(self)
        #self.AddPage(self.trace, "Trace")

    #   ------------------------------------------------------------------------
    def Sinks(self):
    #   ------------------------------------------------------------------------
        return [self.scope.Sink(), self.fft.Sink(), self.histo.Sink(),
            self.waterfall.Sink()]
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        #self.trace.ProcessCommand(sender, command)
        pass
    
    

#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    print "Hello, Monitor!"
    