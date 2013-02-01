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
    """
    The application's signal visualizer. Consists of a wx.Notebook containing
    scope, FFT, histogram, and waterfall visualizations of the generated signal.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
        """
        Initialize the underlying wx.Notebook object and trigger addition of the
        signal views.
        """
        super(Monitor, self).__init__(parent)
        self.xInitGui()
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        """
        Create and add the various signal visualizations.
        """
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
        """
        Return list of Gnuradio sinks associated with the contained signal
        visualizers.
        """
        return [self.scope.Sink(), self.fft.Sink(), self.histo.Sink(),
            self.waterfall.Sink()]
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        """
        Visualizer'c command handler. Currently not used.
        """
        #self.trace.ProcessCommand(sender, command)
        pass
    

#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    print "Hello, Monitor!"
    