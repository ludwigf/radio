#!  /usr/bin/env python

from gnuradio.wxgui import fftsink2

import wx

#   ============================================================================
class FftControl(wx.Panel):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
        super(FftControl, self).__init__(parent)
        self.sink = fftsink2.fft_sink_f(
            self,
            baseband_freq=0,
            y_per_div=10,
            y_divs=10,
            ref_level=0,
            ref_scale=2.0,
            sample_rate=48000,
            fft_size=1024,
            fft_rate=15,
            average=True,
            avg_alpha=None,
            title="FFT Plot",
            peak_hold=False,
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
    print "Hello, FftControl!"
