#!  /usr/bin/env python

import wx

#   ============================================================================
class SignalControl(wx.Panel):
#   ============================================================================

    WaveForms = ["Sine", "Cosine", "Square", "Triangle", "Sawtooth"]
    
    #   ------------------------------------------------------------------------
    def __init__(self, parent, name="", handlers=[]):
    #   ------------------------------------------------------------------------
        super(SignalControl, self).__init__(parent, size=(200,200))
        self.name = name
        self.handlers = handlers
        self.xInitGui()
        
        self.muteBox.Bind(wx.EVT_CHECKBOX, self.xHandler)
        self.waveForm.Bind(wx.EVT_COMBOBOX, self.xHandler)
        self.freqSlider.Bind(wx.EVT_SCROLL, self.xHandler)
        self.freqEdit.Bind(wx.EVT_TEXT_ENTER, self.xHandler)
        self.ampSlider.Bind(wx.EVT_SCROLL, self.xHandler)
        self.ampEdit.Bind(wx.EVT_TEXT_ENTER, self.xHandler)


    #   ------------------------------------------------------------------------
    def SetHandlers(self, handlers):
    #   ------------------------------------------------------------------------
        self.handlers = handlers
        
    
    #   ------------------------------------------------------------------------
    def GetConfig(self):
    #   ------------------------------------------------------------------------
        config = {}
        config["type"] = "signal"
        config["name"] = self.name
        if self.muteBox.GetValue():
            config["mute"] = "true"
        else:
            config["mute"] = "false"
        config["waveform"] = str(self.waveForm.GetValue()).lower()
        config["frequency"] = int(self.freqEdit.GetValue())
        config["amplitude"] = int(self.ampEdit.GetValue())
        return config
    
        
    #   ------------------------------------------------------------------------
    def SetConfig(self, config):
    #   ------------------------------------------------------------------------
        if config["name"] != self.name:
            return
        self.freqSlider.SetValue(int(config["frequency"]))
        self.freqEdit.SetValue(config["frequency"])
        self.ampSlider.SetValue(int(config["amplitude"]))
        self.ampEdit.SetValue(config["amplitude"])
        self.muteBox.SetValue(config["mute"]=="true")
        self.waveForm.SetValue(config["waveform"].capitalize())
         
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        waveLabel = wx.StaticText(self, label="Wave:", size=(40,20),
            style=wx.ST_NO_AUTORESIZE)
        self.waveForm = wx.ComboBox(self, choices=SignalControl.WaveForms, 
            style=wx.CB_READONLY)
        self.waveForm.SetValue("Sine")
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(waveLabel, proportion=0, flag=wx.ALL, border=1)
        hbox1.Add(self.waveForm, proportion=1, flag=wx.ALL, border=1)
        
        freqLabel = wx.StaticText(self, label="Freq:", size=(40,20),
            style=wx.ST_NO_AUTORESIZE)
        self.freqSlider = wx.Slider(self, value=440, minValue=0, maxValue=12000,
            style=wx.SL_HORIZONTAL)
        self.freqEdit = wx.TextCtrl(self, value="440", size=(60,20),
            style=wx.TE_CENTRE|wx.TE_PROCESS_ENTER)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(freqLabel, proportion=0, flag=wx.ALL, border=1)
        hbox2.Add(self.freqSlider, proportion=1, flag=wx.ALL, border=1)
        hbox2.Add(self.freqEdit, proportion=0, flag=wx.ALL, border=1)
        
        ampLabel = wx.StaticText(self, label="Amp:", size=(40,20),
            style=wx.ST_NO_AUTORESIZE)
        self.ampSlider = wx.Slider(self, value=50, minValue=0, maxValue=100,
            style=wx.SL_HORIZONTAL)
        self.ampEdit = wx.TextCtrl(self, value="50", size=(60,20),
            style=wx.TE_CENTRE|wx.TE_PROCESS_ENTER)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(ampLabel, proportion=0, flag=wx.ALL, border=1)
        hbox3.Add(self.ampSlider, proportion=1, flag=wx.ALL, border=1)
        hbox3.Add(self.ampEdit, proportion=0, flag=wx.ALL, border=1)
        
        mutelabel = wx.StaticText(self, label="Mute:", size=(40,20),
            style=wx.ST_NO_AUTORESIZE)
        self.muteBox = wx.CheckBox(self, label="", size=(20,20))
        self.muteBox.SetValue(True)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.AddStretchSpacer(1)
        hbox4.Add(mutelabel, proportion=0, flag=wx.ALL, border=1)
        hbox4.Add(self.muteBox, proportion=0, flag=wx.ALL, border=1)
        hbox4.AddStretchSpacer(1)
        
        staticbox = wx.StaticBox(self, label=self.name)
        staticsizer = wx.StaticBoxSizer(staticbox, wx.VERTICAL)
        #vbox = wx.BoxSizer(wx.VERTICAL)
        staticsizer.Add(hbox1, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.Add(hbox2, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.Add(hbox3, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.Add(hbox4, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.Fit(self)
        self.SetSizer(staticsizer)
        
        self.SetMinSize((200,140))
        self.SetMaxSize((200,140))
    
    
    #   ------------------------------------------------------------------------
    def xHandler(self, event):
    #   ------------------------------------------------------------------------
        sender = event.GetEventObject()
        if sender == self.muteBox:
            mute = "true"
            if not self.muteBox.GetValue():
                mute = "false"
            command = ("mute", mute)
            self.xProcessCommand(command)
            return
        if sender == self.waveForm:
            command = ("waveform", str(self.waveForm.GetValue()).lower())
            self.xProcessCommand(command)
            return
        if sender == self.freqSlider:
            self.freqEdit.SetValue(str(self.freqSlider.GetValue()))
            command = ("frequency", str(self.freqSlider.GetValue()))
            self.xProcessCommand(command)
            return
        if sender == self.freqEdit:
            self.freqSlider.SetValue(int(self.freqEdit.GetValue()))
            command = ("frequency", str(self.freqEdit.GetValue()))
            self.xProcessCommand(command)
        if sender == self.ampSlider:
            self.ampEdit.SetValue(str(self.ampSlider.GetValue()))
            command = ("amplitude", str(self.ampSlider.GetValue()))
            self.xProcessCommand(command)
            return
        if sender == self.ampEdit:
            self.ampSlider.SetValue(int(self.ampEdit.GetValue()))
            command = ("amplitude", str(self.ampEdit.GetValue()))
            self.xProcessCommand(command)
        

    #   ------------------------------------------------------------------------
    def xProcessCommand(self, command):
    #   ------------------------------------------------------------------------
        for handler in self.handlers:
            handler.ProcessCommand(self.name, command)
            
            
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
    app = wx.App()
    frame = wx.Frame(None, -1, "SignalControl")
    control = SignalControl(frame, name="Signal1", handlers=[Handler()])
    control.CenterOnParent()
    frame.Show()
    app.MainLoop()


#   ============================================================================
def Main2():
#   ============================================================================
    signals = ["S1"]
    
    import sys
    sys.path.append("/home/frank/Develop/radio/python/lib")
    from fl.gr.SignalGenerator import SignalGenerator
    
    generator = SignalGenerator(signals=signals)
    generator.Start()
    
    app = wx.App()
    frame = wx.Frame(None, -1, "SignalControl")
    control = SignalControl(frame, name=signals[0], handlers=[generator])
    control.CenterOnParent()
    frame.Show()
    app.MainLoop()


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    Main2()
    