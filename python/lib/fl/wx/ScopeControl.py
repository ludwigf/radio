#!  /usr/bin/env python

from gnuradio import gr
from gnuradio.wxgui import scopesink2

import wx

#   ============================================================================
class ScopeControl(wx.Panel):
#   ============================================================================

     #   ------------------------------------------------------------------------
    def __init__(self, parent, channels=1):
    #   ------------------------------------------------------------------------
        super(ScopeControl, self).__init__(parent)
        self.sink = scopesink2.scope_sink_f(
            self,
            title="Scope Plot",
            sample_rate=48000,
            v_scale=0.2,
            v_offset=0,
            t_scale=0.01,
            ac_couple=False,
            xy_mode=False,
            num_inputs=channels,
            trig_mode=gr.gr_TRIG_MODE_AUTO,
            y_axis_label="Amplitude",
        )
        self.sink.set_autorange(False)
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
    print "Hello, ScopePage!"
    