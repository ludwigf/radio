#!  /usr/bin/env python

from fl.gr.FilterLab import FilterLab
from fl.wx.SignalBank import SignalBank
from fl.wx.SinkBank import SinkBank
from fl.wx.StatusBar import StatusBar
from fl.wx.LowpassFilterControl import LowpassFilterControl
from fl.wx.FilterBank import FilterBank
from MenuBar import MenuBar
from AboutBox import AboutBox
from LowpassDialog import LowpassDialog
from HighpassDialog import HighpassDialog
from BandpassDialog import BandpassDialog
from BandrejectDialog import BandrejectDialog
from ConfigureUdpDialog import ConfigureUdpDialog
from ConfigureFileDialog import ConfigureFileDialog
from Monitor import Monitor
from IDs import ID
#from Config import Config

import wx

#   ============================================================================
class Frame(wx.Frame):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self):
    #   ------------------------------------------------------------------------
        super(Frame, self).__init__(
            None, -1, "GNU Audio Filter Lab")
        self.SetIcon(wx.GetApp().resources.Icon("64x64", "filters"))
        self.xInitGui()
        self.xGetConfig()
        self.filterlab = FilterLab(
            self.monitor.InputProbes(), self.monitor.OutputProbes())
        self.filterbank.AddHandler(self.filterlab)
        self.filterlab.Start()
        #self.configfile = None

        
    #   ------------------------------------------------------------------------
    def PostStatus(self, message):
    #   ------------------------------------------------------------------------
        self.statusbar.PostMessage(message)
        
    
    #   ------------------------------------------------------------------------
    def MenuHandler(self, event):
    #   ------------------------------------------------------------------------
        handlers = {
            ID.MenuFileExit: self.xOnFileExit,
            ID.MenuIoAudioIn: self.xOnIoAudioIn,
            ID.MenuIoUdpIn: self.xOnIoUdpIn,
            ID.MenuIoFileIn: self.xOnIoFileIn,
            ID.MenuIoAudioOut: self.xOnIoAudioOut,
            ID.MenuFilterLowpass: self.xOnAddLowpass,
            ID.MenuFilterHighpass: self.xOnAddHighpass,
            ID.MenuFilterBandpass: self.xOnAddBandpass,
            ID.MenuFilterBandreject: self.xOnAddBandreject,
            ID.MenuFilterRemove: self.xOnRemoveFilter,
            ID.MenuHelpAbout: self.xOnHelpAbout,
        }
            
        action = event.GetId()
        if action not in handlers:
            print "Frame.MenuHandler: Unhandled menu action:", action
            return
        return handlers[action](event)
        

    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.menubar = MenuBar(self, self.MenuHandler)
        self.statusbar = StatusBar(self)
        
        self.panel = wx.Panel(self)
        self.monitor = Monitor(self.panel, size=(1000,-1))
        self.monitor.SetMinSize((1000,-1))
        self.filterbank = FilterBank(self.panel, size=(1000,-1))
        self.filterbank.SetMinSize((1000,138))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.monitor, proportion=0, flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Add(self.filterbank, proportion=0, flag=wx.EXPAND|wx.ALL, border=2)
        sizer.Fit(self.panel)
        self.panel.SetSizer(sizer)
        
        minsize = self.panel.GetSize()
        minsize.SetHeight(
            minsize.GetHeight() + self.menubar.GetSize().GetHeight() +
            self.statusbar.GetSize().GetHeight() + 4)
        self.SetMinSize(minsize)
        #self.Layout()
        self.Show()


    #   ------------------------------------------------------------------------
    def xGetConfig(self):
    #   ------------------------------------------------------------------------
        self.config = {}
        self.config["file-in"] = {"filename": ""}
        self.config["udp-in"] = {"host": "", "port": "9966"}
    
    
    #   ------------------------------------------------------------------------
    def xOnFileExit(self, event):
    #   ------------------------------------------------------------------------
        self.Close()
        
        
    #   ------------------------------------------------------------------------
    def xOnIoAudioIn(self, event):
    #   ------------------------------------------------------------------------
        if event.IsChecked():
            return self.filterlab.ProcessCommand("audio-in", ("mute", "false"))
        else:
            return self.filterlab.ProcessCommand("audio-in", ("mute", "true"))
    

    #   ------------------------------------------------------------------------
    def xOnIoUdpIn(self, event):
    #   ------------------------------------------------------------------------
        if not event.IsChecked():
            return self.filterlab.ProcessCommand("udp-in", ("mute", "true"))
        
        dlg = ConfigureUdpDialog(self, self.config["udp-in"])
        if dlg.ShowModal() != wx.ID_OK:
            dlg.Destroy()
            self.menubar.ResetIoInputs()
            return
        host = dlg.GetDestinationHost()
        port = dlg.GetDestinationPort()
        dlg.Destroy()
        
        self.config["udp-in"]["host"] = host
        self.config["udp-in"]["port"] = port
        if not host or not port:
            self.menubar.ResetIoInputs()
            return

        address = ":".join([host, port])
        self.filterlab.ProcessCommand("udp-in", ("address", address))
        return self.filterlab.ProcessCommand("udp-in", ("mute", "false"))
    
    
    #   ------------------------------------------------------------------------
    def xOnIoFileIn(self, event):
    #   ------------------------------------------------------------------------
        if not event.IsChecked():
            return self.filterlab.ProcessCommand("file-in", ("mute", "true"))
        
        dlg = ConfigureFileDialog(self, self.config["file-in"])
        if dlg.ShowModal() != wx.ID_OK or not dlg.GetDestinationFile():
            dlg.Destroy()
            self.menubar.ResetIoInputs()
            return
        filename = dlg.GetDestinationFile()
        dlg.Destroy()
        self.config["file-in"]["filename"] = filename
        self.filterlab.ProcessCommand("file-in", ("filename", filename))
        return self.filterlab.ProcessCommand("file-in", ("mute", "false"))
    
    
    #   ------------------------------------------------------------------------
    def xOnIoAudioOut(self, event):
    #   ------------------------------------------------------------------------
        if event.IsChecked():
            return self.filterlab.ProcessCommand("audio-out", ("mute", "false"))
        else:
            return self.filterlab.ProcessCommand("audio-out", ("mute", "true"))
    
    
    #   ------------------------------------------------------------------------
    def xOnHelpAbout(self, event):
    #   ------------------------------------------------------------------------
        about = AboutBox()
        about.Show()

    
    #   ------------------------------------------------------------------------
    def xOnAddLowpass(self, event):
    #   ------------------------------------------------------------------------
        dlg = LowpassDialog(self)
        if dlg.ShowModal() == wx.ID_CANCEL:
            dlg.Destroy()
            return
        config = dlg.GetConfig()
        dlg.Destroy()
        if "name" not in config or not config["name"]:
            return
        name = config["name"]
        cutoff = config["cutoff"]
        transit = config["transit"]
        self.filterlab.ProcessCommand("filterchain", ("lowpass", name))
        self.filterlab.ProcessCommand(name, ("cutoff", cutoff))
        self.filterlab.ProcessCommand(name, ("transit", transit))
        self.filterbank.AddLowpassFilter(
            name, cutoff=int(cutoff), transit=int(transit))
        self.menubar.AddConfiguredFilter(name)
        
    #   ------------------------------------------------------------------------
    def xOnAddHighpass(self, event):
    #   ------------------------------------------------------------------------
        dlg = HighpassDialog(self)
        if dlg.ShowModal() == wx.ID_CANCEL:
            dlg.Destroy()
            return
        config = dlg.GetConfig()
        dlg.Destroy()
        if "name" not in config or not config["name"]:
            return
        name = config["name"]
        cutoff = config["cutoff"]
        transit = config["transit"]
        self.filterlab.ProcessCommand("filterchain", ("highpass", name))
        self.filterlab.ProcessCommand(name, ("cutoff", cutoff))
        self.filterlab.ProcessCommand(name, ("transit", transit))
        self.filterbank.AddHighpassFilter(
            name, cutoff=int(cutoff), transit=int(transit))
        self.menubar.AddConfiguredFilter(name)
        

    #   ------------------------------------------------------------------------
    def xOnAddBandpass(self, event):
    #   ------------------------------------------------------------------------
        dlg = BandpassDialog(self)
        if dlg.ShowModal() == wx.ID_CANCEL:
            dlg.Destroy()
            return
        config = dlg.GetConfig()
        dlg.Destroy()
        if "name" not in config or not config["name"]:
            return
        name = config["name"]
        cutoff_low = config["cutoff-low"]
        cutoff_high = config["cutoff-high"]
        transit = config["transit"]
        self.filterlab.ProcessCommand("filterchain", ("bandpass", name))
        self.filterlab.ProcessCommand(name, ("cutoff-low", cutoff_low))
        self.filterlab.ProcessCommand(name, ("cutoff-high", cutoff_high))
        self.filterlab.ProcessCommand(name, ("transit", transit))
        self.filterbank.AddBandpassFilter(
            name, cutoff_low=int(cutoff_low), cutoff_high=int(cutoff_high), 
            transit=int(transit))
        self.menubar.AddConfiguredFilter(name)
        

    #   ------------------------------------------------------------------------
    def xOnAddBandreject(self, event):
    #   ------------------------------------------------------------------------
        dlg = BandrejectDialog(self)
        if dlg.ShowModal() == wx.ID_CANCEL:
            dlg.Destroy()
            return
        config = dlg.GetConfig()
        dlg.Destroy()
        if "name" not in config or not config["name"]:
            return
        name = config["name"]
        cutoff_low = config["cutoff-low"]
        cutoff_high = config["cutoff-high"]
        transit = config["transit"]
        self.filterlab.ProcessCommand("filterchain", ("bandreject", name))
        self.filterlab.ProcessCommand(name, ("cutoff-low", cutoff_low))
        self.filterlab.ProcessCommand(name, ("cutoff-high", cutoff_high))
        self.filterlab.ProcessCommand(name, ("transit", transit))
        self.filterbank.AddBandrejectFilter(
            name, cutoff_low=int(cutoff_low), cutoff_high=int(cutoff_high), 
            transit=int(transit))
        self.menubar.AddConfiguredFilter(name)


    #   ------------------------------------------------------------------------
    def xOnRemoveFilter(self, event):
    #   ------------------------------------------------------------------------
        name = event.filtername
        self.filterlab.ProcessCommand("filterchain", ("remove", name))
        self.filterbank.RemoveFilter(name)
        self.menubar.RemoveConfiguredFilter(name)
        
        