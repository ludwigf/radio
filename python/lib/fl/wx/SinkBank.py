#!  /usr/bin/env python

from SinkControl import SinkControl
import wx

#   ============================================================================
class SinkBank(wx.Panel):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent, sinks, handlers=[]):
    #   ------------------------------------------------------------------------
        super(SinkBank, self).__init__(parent)
        self.xInitGui(sinks, handlers)
        
        
    #   ------------------------------------------------------------------------
    def SetHandlers(self, handlers):
    #   ------------------------------------------------------------------------
        for sink in self.sinks:
            sink.SetHandlers(handlers)
            
    
    #   ------------------------------------------------------------------------
    def StopAll(self):
    #   ------------------------------------------------------------------------
        for sink in self.sinks:
            sink.SetStatus("off")
        
        
    #   ------------------------------------------------------------------------
    def xInitGui(self, sinks, handlers):
    #   ------------------------------------------------------------------------
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sinks = []
        sizer.AddStretchSpacer(1)
        for sink in sinks:
            if self.sinks:
                sizer.AddStretchSpacer(2)
            self.sinks.append(SinkControl(self, sink[0], sink[1], handlers))
            sizer.Add(self.sinks[-1], proportion=0, flag=wx.ALL, border=2)
        sizer.AddStretchSpacer(1)
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
    sinks = [("Audio Out", False), ("UDP Out", True)]
    
    app = wx.App()
    frame = wx.Frame(None, -1, "SinkBank")
    control = SinkBank(frame, sinks, handlers=[Handler()])
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
    Main1()

