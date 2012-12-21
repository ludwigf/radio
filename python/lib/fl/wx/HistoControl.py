#!  /usr/bin/env python

from gnuradio.wxgui import histosink_gl

import wx

#   ============================================================================
class HistoControl(wx.Panel):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
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
