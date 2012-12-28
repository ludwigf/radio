#!  /usr/bin/env python

from fl.gr.FilterChain import FilterChain
from fl.gr.LowpassAdapter import LowpassAdapter
from fl.gr.AnySource import AnySource
from fl.gr.AudioSourceAdapter import AudioSourceAdapter
from fl.gr.FileSourceAdapter import FileSourceAdapter
from fl.gr.UdpSourceAdapter import UdpSourceAdapter
from fl.gr.ManySink import ManySink
from fl.gr.AudioSinkAdapter import AudioSinkAdapter
from fl.gr.SinkAdapter import SinkAdapter

from gnuradio import analog
from gnuradio import gr
from gnuradio import blocks
from gnuradio import audio
from gnuradio.gr import firdes

import wx

#   ============================================================================
class FilterLab(gr.top_block):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, input_monitors, output_monitors, handlers=[]):
    #   ------------------------------------------------------------------------
        super(FilterLab, self).__init__()
        self.samprate = 48000
        self.handlers = handlers
        self.xInit(input_monitors, output_monitors)  


    #   ------------------------------------------------------------------------
    def AddCommandHandler(self, handler):
    #   ------------------------------------------------------------------------
        self.handlers.append(handlers)
        
    
    #   ------------------------------------------------------------------------
    def xInit(self, input_monitors, output_monitors):
    #   ------------------------------------------------------------------------
        sources = {
            "audio-in": AudioSourceAdapter(self, True),
            "udp-in": UdpSourceAdapter(self, "", True),
            "file-in": FileSourceAdapter(self, "", True)}
        self.sources = AnySource( self, sources)
        
        presinks = {}
        index = 0
        for monitor in input_monitors:
            key = "pre%d" % index
            presinks[key] = SinkAdapter(self, monitor)
            index += 1
        self.presinks = ManySink(self, presinks)
        
        postsinks = {
            "audio-out": AudioSinkAdapter(self, True)}
        index = 0
        for monitor in output_monitors:
            key = "post%d" % index
            postsinks[key] = SinkAdapter(self, monitor)
            index += 1
        self.postsinks = ManySink(self, postsinks)
        
        self.filterchain = FilterChain(self, self.samprate)
        self.extra_sinks = {}

        
    #   ------------------------------------------------------------------------
    def Start(self):
    #   ------------------------------------------------------------------------
        self.xConnect()
        self.start()
        
    
    #   ------------------------------------------------------------------------
    def Stop(self):
    #   ------------------------------------------------------------------------
        self.stop()
        self.wait()
    
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        print "FilterLab.ProcessCommand", sender, command
        if sender == "source":
            self.Stop()
            self.source.ProcessCommand(sender, command)
            self.Start()
            return
        if sender == "filterchain":
            self.Stop()
            self.filterchain.ProcessCommand(sender, command)
            self.Start()
            return
        if sender in self.sources.Sources() and command[0] == "mute":
            return self.sources.ProcessCommand(sender, command)
        if sender in self.sources.Sources():
            self.Stop()
            self.sources.ProcessCommand(sender, command)
            self.Start()
            return
        if sender in self.filterchain.Filters():
            return self.filterchain.ProcessCommand(sender, command)
        if sender in self.postsinks.Sinks():
            return self.postsinks.ProcessCommand(sender, command)
        
        
    #   ------------------------------------------------------------------------
    def xConnect(self):
    #   ------------------------------------------------------------------------
        self.disconnect_all()
        self.sources.Connect()
        self.filterchain.Connect()
        self.presinks.Connect()
        self.postsinks.Connect()
        self.connect(self.sources.Outport(), self.presinks.Inport())
        self.connect(self.sources.Outport(), self.filterchain.Inport())
        self.connect(self.filterchain.Outport(), self.postsinks.Inport())
      