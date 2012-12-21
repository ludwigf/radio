#!  /usr/bin/env python

from gnuradio import analog
from gnuradio import gr
from gnuradio import blocks
from gnuradio import audio

import wx

#   ============================================================================
class SignalGenerator(gr.top_block):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, signals=[], noises=[], sinks=[]):
    #   ------------------------------------------------------------------------
        super(SignalGenerator, self).__init__()
        self.samprate = 48000
        self.udpconfig = {"host": "", "port":9966}
        self.fileconfig = {"filename": ""}
        self.waveconfig = {"filename": ""}
        self.xInit(signals, noises, sinks)  
        
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
    def Run(self):
    #   ------------------------------------------------------------------------
        self.run()

    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        #print sender, command
        if command[0] == "mute":
            return self.xSetMute(sender, command[1]=="true")
        if command[0] == "waveform":
            return self.xSetWaveForm(sender, command[1])
        if command[0] == "noiseform":
            return self.xSetNoiseForm(sender, command[1])
        if command[0] == "frequency":
            return self.xSetFrequency(sender, int(command[1]))
        if command[0] == "amplitude":
            return self.xSetAmplitude(sender, int(command[1]))
        if command[0] == "run":
            return self.xSetRun(sender, command[1]=="true")
        wx.GetApp().PostStatus(
            "SignalGenerator Error: Unknown command \"%s\"" % command[0])
        
        
    #   ------------------------------------------------------------------------
    def SetUdpConfig(self, config):
    #   ------------------------------------------------------------------------
        if "host" in config:
            self.udpconfig["host"] = config["host"]
        if "port" in config:
            self.udpconfig["port"] = config["port"]
           
        
    #   ------------------------------------------------------------------------
    def SetFileConfig(self, config):
    #   ------------------------------------------------------------------------
        if "filename" in config:
            self.fileconfig["filename"] = config["filename"]
        
        
    #   ------------------------------------------------------------------------
    def SetWaveConfig(self, config):
    #   ------------------------------------------------------------------------
        if "filename" in config:
            self.waveconfig["filename"] = config["filename"]
            
    #   ------------------------------------------------------------------------
    def SetSourceConfig(self, config):
    #   ------------------------------------------------------------------------
        if config["type"] == "signal":
            sender = config["name"]
            for item in ["waveform", "frequency", "amplitude", "mute"]:
                command = (item, config[item])
                self.ProcessCommand(sender, command)
        if config["type"] == "noise":
            sender = config["name"]
            for item in ["noiseform", "amplitude", "mute"]:
                command = (item, config[item])
                self.ProcessCommand(sender, command)
        
        
    #   ------------------------------------------------------------------------
    def StopAllSinks(self):
    #   ------------------------------------------------------------------------
        self.audiomute.set_mute(True)
        self.Stop()
        self.udp = gr.null_sink(gr.sizeof_float)
        self.rawfile = gr.null_sink(gr.sizeof_float)
        self.wavefile = gr.null_sink(gr.sizeof_float)
        self.Start()
        
        
    #   ------------------------------------------------------------------------
    def xInit(self, signals, noises, sinks):
    #   ------------------------------------------------------------------------
        self.sources = {}
        self.mutes = {}
        self.amps = {}
        
        #sources
        for signal in signals:
            self.sources[signal] = gr.sig_source_f(
                self.samprate, gr.GR_SIN_WAVE, 440, 0.25, 0)
            self.mutes[signal] = gr.mute_ff(True)
            self.amps[signal] = gr.multiply_const_ff(0.25)
        for noise in noises:
            self.sources[noise] = analog.noise_source_f(
                analog.GR_LAPLACIAN, 1, 0)
            self.mutes[noise] = gr.mute_ff(True)
            self.amps[noise] = gr.multiply_const_ff(0.25)
        #mixer
        if len(self.sources) > 1:
            self.adder = self.add = gr.add_vff(1)
        else:
            self.adder = gr.multiply_const_vff((1, ))
        self.level = gr.multiply_const_ff(1)
        
        #sinks
        self.sinks = sinks
            
        self.audiomute = gr.mute_ff(True)
        self.audio = audio.sink(self.samprate, "", True)
        self.udp = gr.null_sink(gr.sizeof_float)
        self.rawfile = gr.null_sink(gr.sizeof_float)
        self.wavefile = gr.null_sink(gr.sizeof_float)
        
        
    #   ------------------------------------------------------------------------
    def xConnect(self):
    #   ------------------------------------------------------------------------
        self.disconnect_all()
        channel=0
        for source in self.sources:
            self.connect((self.sources[source], 0), (self.mutes[source], 0))
            self.connect((self.mutes[source], 0), (self.amps[source], 0))
            self.connect((self.amps[source], 0), (self.adder, channel))
            channel += 1
        self.connect((self.adder,0), (self.level, 0))
        for sink in self.sinks:
            self.connect((self.level, 0), (sink, 0))
            channel += 1
        self.connect((self.level, 0), (self.audiomute, 0))
        self.connect((self.audiomute, 0), (self.audio, 0))
        self.connect((self.level, 0), (self.udp, 0))
        self.connect((self.level, 0), (self.rawfile, 0))
        self.connect((self.level, 0), (self.wavefile, 0))
        
        
    #   ------------------------------------------------------------------------
    def xSetMute(self, sender, level):
    #   ------------------------------------------------------------------------
        if sender in self.mutes:
            self.mutes[sender].set_mute(level)
            return
        wx.GetApp().PostStatus(
            "SignalGenerator Error: Unknown source device \"%s\"" % sender)
        
        
    #   ------------------------------------------------------------------------
    def xSetWaveForm(self, sender, form):
    #   ------------------------------------------------------------------------
        wavemap = {"sine": gr.GR_SIN_WAVE, "cosine": gr.GR_COS_WAVE, 
            "square": gr.GR_SQR_WAVE, "triangle": gr.GR_TRI_WAVE, 
            "sawtooth": gr.GR_SAW_WAVE}
        if form not in wavemap or not wavemap[form]:
            wx.GetApp().PostStatus(
                "SignalGenerator Error: Unknown wave form \"%s\"" % form)
            return
        self.sources[sender].set_waveform(wavemap[form])
        
        
    #   ------------------------------------------------------------------------
    def xSetNoiseForm(self, sender, form):
    #   ------------------------------------------------------------------------
        noisemap = {"uniform": analog.GR_UNIFORM, 
            "gaussian": analog.GR_GAUSSIAN, "laplacian": analog.GR_LAPLACIAN,
            "impulse": analog.GR_IMPULSE}
        if form not in noisemap or not noisemap[form]:
            wx.GetApp().PostStatus( 
                "SignalGenerator Error: Unknown noise form \"%s\"" % form)
            return
        self.sources[sender].set_type(noisemap[form])
    
    
    #   ------------------------------------------------------------------------
    def xSetFrequency(self, sender, frequency):
    #   ------------------------------------------------------------------------
        self.sources[sender].set_frequency(frequency)
        
        
    #   ------------------------------------------------------------------------
    def xSetAmplitude(self, sender, amplitude):
    #   ------------------------------------------------------------------------
        self.amps[sender].set_k(0.01*amplitude)
        total = sum([self.amps[s].k() for s in self.amps])
        if total > 1:
            self.level.set_k(1.0/total)
        
        
    #   ------------------------------------------------------------------------
    def xSetRun(self, sender, state):
    #   ------------------------------------------------------------------------
        if sender == "Audio Out":
            self.audiomute.set_mute(not state)
            
        if sender == "UDP Out":
            host = self.udpconfig["host"]
            port = self.udpconfig["port"]
            self.Stop()
            if state == False or not host or not port:
                self.udp = gr.null_sink(gr.sizeof_float)
                wx.GetApp().PostStatus(
                    "SignalGenerator Info: Stopped UDP output to \"%s:%s\"" % (
                        host, port))
            else:
                self.udp = gr.udp_sink(gr.sizeof_float, host, port, 1472, True)
                wx.GetApp().PostStatus(
                    "SignalGenerator Info: Started UDP output to \"%s:%s\"" % (
                        host, port))
            self.Start()
            
        if sender == "File Out":
            filename = self.fileconfig["filename"]
            self.Stop()
            if state == False or not filename:
                self.rawfile = gr.null_sink(gr.sizeof_float)
                wx.GetApp().PostStatus(
                    "SignalGenerator Info: Stopped rawfile device \"%s\"" % (
                        filename,))
            else:
                self.rawfile = gr.file_sink(gr.sizeof_float, filename)
                wx.GetApp().PostStatus(
                    "SignalGenerator Info: Started rawfile device \"%s\"" % (
                        filename,))
            self.Start()
                    
        if sender == "Wave Out":
            filename = self.waveconfig["filename"]
            self.Stop()
            if state == False or not filename:
                self.wavefile = gr.null_sink(gr.sizeof_float)
                wx.GetApp().PostStatus(
                    "SignalGenerator Info: Stopped wave device \"%s\"" % (
                        filename,))
                        
            else:
                self.wavefile = gr.wavfile_sink(filename, 1, self.samprate, 16)
                wx.GetApp().PostStatus(
                    "SignalGenerator Info: Started wave device \"%s\"" % (
                        filename,))
            self.Start()
                    
                    
#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    generator = SignalGenerator(["sig1", "sig2"])
    generator.Run()
    