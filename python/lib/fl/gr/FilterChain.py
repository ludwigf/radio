#!  /usr/bin/env python

from gnuradio import analog
from gnuradio import gr
from gnuradio import blocks
from gnuradio import audio

import wx

from fl.gr.LowpassAdapter import LowpassAdapter
from fl.gr.HighpassAdapter import HighpassAdapter
from fl.gr.BandpassAdapter import BandpassAdapter
from fl.gr.BandrejectAdapter import BandrejectAdapter

#   ============================================================================
class FilterChain(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent, samprate):
    #   ------------------------------------------------------------------------
        super(FilterChain, self).__init__()
        self.parent = parent
        self.samprate = samprate
        self.chain = []
        self.filters = {}
        self.dummy = None
        
        
    #   ------------------------------------------------------------------------
    def Connect(self):
    #   ------------------------------------------------------------------------
        if self.chain:
            if self.dummy:
                self.dummy = None
            for index in range(len(self.chain)-1):
                self.parent.connect(
                    (self.chain[index],0), (self.chain[index+1],0))
            return
        if not self.dummy:
            self.dummy = gr.multiply_const_vff((1, ))
            
    
    #   ------------------------------------------------------------------------
    def Inport(self):
    #   ------------------------------------------------------------------------
        if self.chain:
            return (self.chain[0],0)
        if not self.dummy:
            self.dummy = gr.multiply_const_vff((1, ))
        return (self.dummy,0)
    
            
    #   ------------------------------------------------------------------------
    def Outport(self):
    #   ------------------------------------------------------------------------
        if self.chain:
            return (self.chain[-1],0)
        if not self.dummy:
            self.dummy = gr.multiply_const_vff((1, ))
        return (self.dummy,0)
    
            
    #   ------------------------------------------------------------------------
    def Filters(self):
    #   ------------------------------------------------------------------------
        return self.filters
    
    
    #   ------------------------------------------------------------------------
    def xAddFilter(self, name, adapter):
    #   ------------------------------------------------------------------------
        print "FilterChain.xAddFilter", name, adapter
        self.chain.append(adapter.Filter())
        self.filters[name] = adapter
        
    
    #   ------------------------------------------------------------------------
    def xRemoveFilter(self, name):
    #   ------------------------------------------------------------------------
        print "FilterChain.xRemoveFilter", name
        del(self.chain[self.chain.index(self.filters[name].Filter())])
        del(self.filters[name])
        
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        print "FilterChain.ProcessCommand", sender, command
        if sender in self.filters:
            return self.filters[sender].ProcessCommand(command)
        if sender == "filterchain" and command[0] == "lowpass":
            adapter = LowpassAdapter()
            self.xAddFilter(command[1], adapter)
            return
        if sender == "filterchain" and command[0] == "highpass":
            adapter = HighpassAdapter()
            self.xAddFilter(command[1], adapter)
            return
        if sender == "filterchain" and command[0] == "bandpass":
            adapter = BandpassAdapter()
            self.xAddFilter(command[1], adapter)
            return
        if sender == "filterchain" and command[0] == "bandreject":
            adapter = BandrejectAdapter()
            self.xAddFilter(command[1], adapter)
            return
        if sender == "filterchain" and command[0] == "remove":
            self.xRemoveFilter(command[1])
