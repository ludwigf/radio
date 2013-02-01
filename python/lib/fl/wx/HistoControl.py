#!  /usr/bin/env python

from gnuradio.wxgui import histosink_gl

import wx

#   ============================================================================
class HistoControl(wx.Panel):
#   ============================================================================
    """
    Wrapper for the Gnuradio histosink_gl.histo_sink_f sink class.
    """

    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
        """
        Initialize, create and place wrapped Gnuradio object onto the underlying
        wx.Panel.
        """
        super(HistoControl, self).__init__(parent)
        self.sink = histosink_gl.histo_sink_f(
            self,
            title="Histogram Plot",
            num_bins=27,
            frame_size=1000,
        )
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.sink.win, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)
        
    #   ------------------------------------------------------------------------
    def Sink(self):
    #   ------------------------------------------------------------------------
        return self.sink
        
        
#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    print "Hello, HistoControl!"
