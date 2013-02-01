#!  /usr/bin/env python

from fl.gr.SignalGenerator import SignalGenerator
from fl.wx.SignalBank import SignalBank
from fl.wx.SinkBank import SinkBank
from fl.wx.StatusBar import StatusBar
from MenuBar import MenuBar
from AboutBox import AboutBox
from ConfigureUdpDialog import ConfigureUdpDialog
from ConfigureFileDialog import ConfigureFileDialog
from ConfigureWaveDialog import ConfigureWaveDialog
from Monitor import Monitor
from Config import Config

import wx

#   ============================================================================
class Frame(wx.Frame):
#   ============================================================================
    """
    The application's main window. Also doubles as the application's main menu
    handler.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, signals, noises, sinks):
    #   ------------------------------------------------------------------------
        """
        Initialize wx.Frame and trigger initialization of all embedded objects. 
        Embedded object include:
        - controls for signal generators
        - controls for noise generators
        - the gnuradio based SignalGenerator object that provides the backend
        - default configurations for all available output options
        Starts the backend SignalGenerator object once everything is set up.
        """
        
        super(Frame, self).__init__(
            None, -1, "GNU Radio Signal Generator")
        self.SetIcon(wx.GetApp().resources.Icon("64x64", "signals"))
        self.xInitGui(signals, noises, sinks)
        
        # Create backend processor and set as handler for signal and noise GUI
        #  controls
        self.generator = SignalGenerator(
            signals=signals, noises=noises, sinks=self.trace.Sinks())
        self.signals.SetHandlers([self.generator, self.trace])
        self.sinks.SetHandlers([self.generator])
        
        # Create default configurations for available gnuradio sinks
        self.configfile = None
        self.fileConfig = {"filename": ""}
        self.waveConfig = {"filename": ""}
        self.udpConfig = {"host": "", "port": 9966}
        self.generator.SetUdpConfig(self.udpConfig)
        
        self.generator.Start()

        
    #   ------------------------------------------------------------------------
    def MenuHandler(self, event):
    #   ------------------------------------------------------------------------
        """
        
        Menu handler for all main menu items. Specific menu handlers are invoked
        based on sending item's ID.
        """
        action = event.GetId()
        if action == wx.ID_EXIT:
            self.Close()
        if action == wx.ID_OPEN:
            return self.xOnFileOpen(event)
        if action == wx.ID_SAVE:
            return self.xOnFileSave(event)
        if action == wx.ID_SAVEAS:
            return self.xOnFileSaveAs(event)
        if action == wx.ID_ABOUT:
            return self.xOnHelpAbout(event)
        if action == wx.ID_FILE1:
            return self.xOnConfigUdp(event)
        if action == wx.ID_FILE2:
            return self.xOnConfigFile(event)
        if action == wx.ID_FILE3:
            return self.xOnConfigWave(event)
        
        
    #   ------------------------------------------------------------------------
    def PostStatus(self, message):
    #   ------------------------------------------------------------------------
        """
        Post given message to the window's status bar.
        """
        
        self.statusbar.PostMessage(message)
        
    
    #   ------------------------------------------------------------------------
    def xInitGui(self, signals, noises, sinks):
    #   ------------------------------------------------------------------------
        """
        Creates and initializes the main GUI elements, such as:
        - a monitor view that displays generated signals graphically
        - the application's menu and status bars
        - a bank of signal and noise controls
        - a bank of controls for the available sinks
        """
        
        self.menubar = MenuBar(self, self.MenuHandler)
        self.statusbar = StatusBar(self)
        
        panel = wx.Panel(self)
        self.trace = Monitor(panel)
        self.signals = SignalBank(panel, signals , noises, handlers=[])
        self.sinks = SinkBank(panel, sinks, handlers=[])
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.signals, proportion=0, flag=wx.ALL|wx.EXPAND, border=4)
        sizer.Add(self.sinks, proportion=0, flag=wx.ALL|wx.EXPAND, border=4)
        sizer.Add(self.trace, proportion=1, flag=wx.ALL|wx.EXPAND, border=4)
        sizer.Fit(panel)
        panel.SetSizer(sizer)
        
        minsize = panel.GetSize()
        minsize.SetHeight(
            minsize.GetHeight() + self.menubar.GetSize().GetHeight() +
            self.statusbar.GetSize().GetHeight() + 4)
        self.SetMinSize(minsize)
        self.Show()


    #   ------------------------------------------------------------------------
    def xOnFileOpen(self, event):
    #   ------------------------------------------------------------------------
        """
        Menu handler to display dialog to load a previously saved configuration 
        for the available signal and noise sources and sinks.
        """
        
        dialog = wx.FileDialog(self, "Load Configuration", 
            style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
        if self.configfile:
            dialog.SetFilename(self.configfile)
        if not dialog.ShowModal() == wx.ID_OK:
            dialog.Destroy()
            return
        self.configfile = dialog.GetPath()
        config = Config(self)
        config.LoadConfig(self.configfile)
        dialog.Destroy()
        
        
    #   ------------------------------------------------------------------------
    def xOnFileSave(self, event):
    #   ------------------------------------------------------------------------
        """
        Menu handler to save current signal and noise source and sink 
        configuration to a previously established file name.
        """
        
        if not self.configfile:
            return self.xOnFileSaveAs(event)
        config = Config(self)
        config.SaveConfig(self.configfile)
        
        
    #   ------------------------------------------------------------------------
    def xOnFileSaveAs(self, event):
    #   ------------------------------------------------------------------------
        """
        Menu handler to establish (new) file name for signal, noise and sink 
        configuration, then save current configuration to that file.
        """
        
        dialog = wx.FileDialog(self, "Save Configuration", 
            style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        if self.configfile:
            dialog.SetFilename(self.configfile)
        if not dialog.ShowModal() == wx.ID_OK:
            dialog.Destroy()
            return
        self.configfile = dialog.GetPath()
        config = Config(self)
        config.SaveConfig(self.configfile)
        dialog.Destroy()
        
    
    #   ------------------------------------------------------------------------
    def xOnHelpAbout(self, event):
    #   ------------------------------------------------------------------------
        """
        Menu handler to show the application's About box.
        """
        about = AboutBox()
        about.Show()
        
        
    #   ------------------------------------------------------------------------
    def xOnConfigUdp(self, event):
    #   ------------------------------------------------------------------------
        """
        Menu handler to display dialog to allow customization of the 
        application's UDP sink configuration.
        """
        
        dialog = ConfigureUdpDialog(self, self.udpConfig)
        if dialog.ShowModal() == wx.ID_CANCEL:
            dialog.Destroy()
            return
        host = dialog.GetDestinationHost()
        if host:
            self.udpConfig["host"] = host
        port = dialog.GetDestinationPort()
        if port:
            self.udpConfig["port"] = port
        self.generator.SetUdpConfig(self.udpConfig)
        dialog.Destroy()
        
        
    #   ------------------------------------------------------------------------
    def xOnConfigFile(self, event):
    #   ------------------------------------------------------------------------
        """
        Menu handler to display dialog to allow customization of the 
        application's file sink configuration.
        """

        dialog = ConfigureFileDialog(self, self.fileConfig)
        if dialog.ShowModal() == wx.ID_CANCEL:
            dialog.Destroy()
            return
        filename = dialog.GetDestinationFile()
        if filename:
            self.fileConfig["filename"] = filename
        self.generator.SetFileConfig(self.fileConfig)
        dialog.Destroy()
        

    #   ------------------------------------------------------------------------
    def xOnConfigWave(self, event):
    #   ------------------------------------------------------------------------
        """
        Menu handler to display dialog to allow customization of the 
        application's wave file sink configuration.
        """

        dialog = ConfigureWaveDialog(self, self.waveConfig)
        if dialog.ShowModal() == wx.ID_CANCEL:
            dialog.Destroy()
            return
        filename = dialog.GetDestinationFile()
        if filename:
            self.waveConfig["filename"] = filename
        self.generator.SetWaveConfig(self.waveConfig)
        dialog.Destroy()
