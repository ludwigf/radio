#!  /usr/bin/env python

import wx

#   ============================================================================
class TextTrace(wx.TextCtrl):
#   ============================================================================
    """
    Control that simply traces all commands it receives into a wx>textCtrl. Used
    for debugging purposes.
    """

    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
        """
        Initializes underlying wx.TextCtrl object.
        """
        super(TextTrace, self).__init__(
            parent, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.xInitGui()
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        pass
    
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        """
        Trace given command as a new line of text.
        """
        text = "%-8.8s: %s %s\n" % (sender, command[0], command[1])
        self.AppendText(text)
        
        
#   ============================================================================
def Main1():
#   ============================================================================
    app = wx.App()
    frame = wx.Frame(None, -1, "TextTrace")
    control = TextTrace(frame)
    frame.Show()
    control.ProcessCommand("S1", ("waveform", "sine"))
    control.ProcessCommand("S2", ("frequency", 440))
    control.ProcessCommand("S3", ("amplitude", 50))
    control.ProcessCommand("S4", ("mute", True))
    app.MainLoop()
    
    
#   ============================================================================
def Main2():
#   ============================================================================
    signals = ["S1", "S2", "S3", "S4"]

    import sys
    sys.path.append("/home/frank/Develop/radio/python/lib")
    from fl.gr.SignalGenerator import SignalGenerator
    from SignalBank import SignalBank

    generator = SignalGenerator(signals=signals)
    generator.Start()
    
    app = wx.App()
    frame = wx.Frame(None, -1, "TextTrace")
    
    panel = wx.Panel(frame)
    trace = TextTrace(panel)
    signalbank = SignalBank(panel, signals , handlers=[generator, trace])
    psizer = wx.BoxSizer(wx.VERTICAL)
    psizer.Add(signalbank, proportion=0, flag=wx.ALL|wx.EXPAND, border=1)
    psizer.Add(trace, proportion=1, flag=wx.ALL|wx.EXPAND, border=1)
    psizer.Fit(panel)
    panel.SetSizer(psizer)
    frame.SetMinSize(panel.GetSize())
    frame.Show()
    app.MainLoop()


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    Main2()
    