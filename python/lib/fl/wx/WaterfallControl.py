#!  /usr/bin/env python

from gnuradio.wxgui import waterfallsink2

import wx

#   ============================================================================
class WaterfallControl(wx.Panel):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
        super(WaterfallControl, self).__init__(parent)
        self.sink = waterfallsink2.waterfall_sink_f(
            self,
            baseband_freq=0,
            dynamic_range=100,
            ref_level=0,
            ref_scale=2.0,
            sample_rate=48000,
            fft_size=512,
            fft_rate=15,
            average=False,
            avg_alpha=None,
            title="Waterfall Plot",
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
    print "Hello, WaterfallPage!"
