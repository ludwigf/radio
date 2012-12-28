#!  /usr/bin/env python

from gnuradio import gr
from gnuradio.gr import firdes

#   ============================================================================
class BandpassAdapter(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, samprate=48000, cutoff_low=300, cutoff_high=3000, 
        transit=100):
    #   ------------------------------------------------------------------------
        super(BandpassAdapter, self).__init__()
        self.filter = gr.fir_filter_fff(1, firdes.band_pass(
            1, samprate, cutoff_low, cutoff_high, transit, firdes.WIN_HAMMING, 
            6.76))
        self.samprate = samprate
        self.cutoff_low = cutoff_low
        self.cutoff_high = cutoff_high
        self.transit = transit
        

    #   ------------------------------------------------------------------------
    def Filter(self):
    #   ------------------------------------------------------------------------
        return self.filter
        
        
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, command):
    #   ------------------------------------------------------------------------
        if command[0] == "cutoff-low":
            self.cutoff_low = int(command[1])
        if command[0] == "cutoff-high":
            self.cutoff_high = int(command[1])
        if command[0] == "transit":
            self.transit = int(command[1])
        self.filter.set_taps(
            firdes.band_pass(
                1, self.samprate, self.cutoff_low, self.cutoff_high, 
                self.transit, firdes.WIN_HAMMING, 6.76))
        