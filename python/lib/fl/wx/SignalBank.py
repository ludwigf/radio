#!  /usr/bin/env python

from SignalControl import SignalControl
from NoiseControl import NoiseControl
import wx

#   ============================================================================
class SignalBank(wx.Panel):
#   ============================================================================
    """
    wx.Panel based control that aggregates multiple SignalControls and/or
    NoiseControls.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, parent, signals, noises=[], handlers=[]):
    #   ------------------------------------------------------------------------
        """
        Initializes the underlying wx object and triggers GUI creation.
        """
        super(SignalBank, self).__init__(parent)
        self.xInitGui(signals, noises, handlers)
        
        
    #   ------------------------------------------------------------------------
    def SetHandlers(self, handlers):
    #   ------------------------------------------------------------------------
        """
        Assigns external handlers to each of the constituent SignalContols 
        and/or NoiseControls.
        """
        for signal in self.signals:
            signal.SetHandlers(handlers)
            
    
    #   ------------------------------------------------------------------------
    def GetConfig(self):
    #   ------------------------------------------------------------------------
        """
        Get current settings for all constituent Signal/NoiseControls as a list
        of config dictionaries.
        """
        config = [signal.GetConfig() for signal in self.signals]
        return config
    
    
    #   ------------------------------------------------------------------------
    def SetConfig(self, config):
    #   ------------------------------------------------------------------------
        """
        Adjusts current settings ofall constituent Signal/NoiseControls from a
        list of config disctionaries.
        """
        for signal in self.signals:
            signal.SetConfig(config)
            
    #   ------------------------------------------------------------------------
    def xInitGui(self, signals, noises, handlers):
    #   ------------------------------------------------------------------------
        """
        Creates the user interface.
        """
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.signals = []
        for signal in signals:
            if self.signals:
                sizer.AddStretchSpacer(1)
            self.signals.append(SignalControl(self, signal, handlers))
            sizer.Add(self.signals[-1], proportion=0, flag=wx.ALL, border=2)
        for noise in noises:
            if self.signals:
                sizer.AddStretchSpacer(1)
            self.signals.append(NoiseControl(self, noise, handlers))
            sizer.Add(self.signals[-1], proportion=0, flag=wx.ALL, border=2)
        sizer.Fit(self)
        self.SetSizer(sizer)
    
    
#   ============================================================================
class Handler(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self):
    #   ------------------------------------------------------------------------
        super(Handler, self).__init__()
        
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        print sender, command
        
        
#   ============================================================================
def Main1():
#   ============================================================================
    signals = ["S1", "S2", "S3", "S4"]
    noises = ["N1"]
    
    app = wx.App()
    frame = wx.Frame(None, -1, "SignalBank")
    control = SignalBank(frame, signals , noises, handlers=[Handler()])
    frame.SetMinSize(control.GetSize())
    frame.Show()
    app.MainLoop()


#   ============================================================================
def Main2():
#   ============================================================================
    signals = ["S1", "S2", "S3", "S4"]
    noises = ["N1"]

    import sys
    sys.path.append("/home/frank/Develop/radio/python/lib")
    from fl.gr.SignalGenerator import SignalGenerator
    
    generator = SignalGenerator(signals=signals, noises=noises)
    generator.Start()
    
    app = wx.App()
    frame = wx.Frame(None, -1, "SignalBank")
    control = SignalBank(frame, signals , noises, handlers=[generator])
    frame.SetMinSize(control.GetSize())
    frame.Show()
    app.MainLoop()


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    Main2()

