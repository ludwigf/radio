#!  /usr/bin/env python

from gnuradio import gr
from gnuradio.gr import firdes

#   ============================================================================
class HighpassAdapter(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, samprate=48000, cutoff=1000, transit=100):
    #   ------------------------------------------------------------------------
        super(HighpassAdapter, self).__init__()
        self.filter = gr.fir_filter_fff(1, firdes.high_pass(
            1, samprate, cutoff, transit, firdes.WIN_HAMMING, 6.76))
        self.samprate = samprate
        self.cutoff = cutoff
        self.transit = transit
        
        
    #   ------------------------------------------------------------------------
    def Filter(self):
    #   ------------------------------------------------------------------------
        return self.filter
        
        
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, command):
    #   ------------------------------------------------------------------------
        if command[0] == "cutoff":
            self.cutoff = int(command[1])
        if command[0] == "transit":
            self.transit = int(command[1])
        self.filter.set_taps(
            firdes.high_pass(1, self.samprate, self.cutoff, self.transit, 
            firdes.WIN_HAMMING, 6.76))
        