#!  /usr/bin/env python

import wx

#   ============================================================================
class NoiseControl(wx.Panel):
#   ============================================================================
    """
    wx.Panel based control that allows configuration of a single channel 
    noise generator. Any changes initiated by modifying control settings are
    sent to a command handler. The syntax of the commands sent to the handler
    is "target (setting, value)".
    """
    
    NoiseForms = ["Uniform", "Gaussian", "Laplacian", "Impulse"]
    
    #   ------------------------------------------------------------------------
    def __init__(self, parent, name="", handlers=[]):
    #   ------------------------------------------------------------------------
        """
        Initialize the underlying wx component and trigger creation of the user
        interface. Wire embedded controls to the embedded command handler.
        """
        super(NoiseControl, self).__init__(parent, size=(200,200))
        self.name = name
        self.handlers = handlers
        self.xInitGui()
        
        self.muteBox.Bind(wx.EVT_CHECKBOX, self.xHandler)
        self.noiseForm.Bind(wx.EVT_COMBOBOX, self.xHandler)
        self.ampSlider.Bind(wx.EVT_SCROLL, self.xHandler)
        self.ampEdit.Bind(wx.EVT_TEXT_ENTER, self.xHandler)

    #   ------------------------------------------------------------------------
    def SetHandlers(self, handlers):
    #   ------------------------------------------------------------------------
        """
        Set list of external command handlers to be called when settings change
        (in addition to the internal handler).
        """
        self.handlers = handlers
        
    #   ------------------------------------------------------------------------
    def GetConfig(self):
    #   ------------------------------------------------------------------------
        """
        Return dictionary containing current signal settings.
        """
        config = {}
        config["type"] = "noise"
        config["name"] = self.name
        if self.muteBox.GetValue():
            config["mute"] = "true"
        else:
            config["mute"] = "false"
        config["noiseform"] = str(self.noiseForm.GetValue()).lower()
        config["amplitude"] = int(self.ampEdit.GetValue())
        return config
    
    #   ------------------------------------------------------------------------
    def SetConfig(self, config):
    #   ------------------------------------------------------------------------
        """
        Initialize signal control setting from the values of a given dictionary.
        """
        if config["name"] != self.name:
            return
        self.noiseForm.SetValue(config["noiseform"].capitalize())
        self.ampSlider.SetValue(int(config["amplitude"]))
        self.ampEdit.SetValue(config["amplitude"])
        self.muteBox.SetValue(True)
        
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        """
        Create the noise control user interface.
        """
        noiseLabel = wx.StaticText(self, label="Noise:", size=(40,20),
            style=wx.ST_NO_AUTORESIZE)
        self.noiseForm = wx.ComboBox(self, choices=NoiseControl.NoiseForms, 
            style=wx.CB_READONLY)
        self.noiseForm.SetValue("Uniform")
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(noiseLabel, proportion=0, flag=wx.ALL, border=1)
        hbox1.Add(self.noiseForm, proportion=1, flag=wx.ALL, border=1)
        
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
        staticsizer.AddStretchSpacer(1)
        staticsizer.Add(hbox1, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.Add(hbox3, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.Add(hbox4, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.AddStretchSpacer(2)
        staticsizer.Fit(self)
        self.SetSizer(staticsizer)
        
        self.SetMinSize((200,140))
        self.SetMaxSize((200,140))
    
    
    #   ------------------------------------------------------------------------
    def xHandler(self, event):
    #   ------------------------------------------------------------------------
        """
        Internal event handler. Creates command based on current control 
        settings then triggers invokation of external command handlers.
        """
        sender = event.GetEventObject()
        if sender == self.muteBox:
            mute = "true"
            if not self.muteBox.GetValue():
                mute = "false"
            command = ("mute", mute)
            print ">d", command
            self.xProcessCommand(command)
            return
        if sender == self.noiseForm:
            command = ("noiseform", str(self.noiseForm.GetValue()).lower())
            self.xProcessCommand(command)
            return
        if sender == self.ampSlider:
            self.ampEdit.SetValue(str(self.ampSlider.GetValue()))
            command = ("amplitude", self.ampSlider.GetValue())
            self.xProcessCommand(command)
            return
        if sender == self.ampEdit:
            self.ampSlider.SetValue(int(self.ampEdit.GetValue()))
            command = ("amplitude", int(self.ampEdit.GetValue()))
            self.xProcessCommand(command)
        

    #   ------------------------------------------------------------------------
    def xProcessCommand(self, command):
    #   ------------------------------------------------------------------------
        """
        Invoke external command handlers on the given command.
        """
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
    frame = wx.Frame(None, -1, "NoiseControl")
    control = NoiseControl(frame, name="Noise1", handlers=[Handler()])
    control.CenterOnParent()
    frame.Show()
    app.MainLoop()


#   ============================================================================
def Main2():
#   ============================================================================
    noises = ["N1"]
    
    import sys
    sys.path.append("/home/frank/Develop/radio/python/lib")
    from fl.gr.SignalGenerator import SignalGenerator
    
    generator = SignalGenerator(noises=noises)
    generator.Start()
    
    app = wx.App()
    frame = wx.Frame(None, -1, "NoiseControl")
    control = NoiseControl(frame, name=noises[0], handlers=[generator])
    control.CenterOnParent()
    frame.Show()
    app.MainLoop()


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    Main2()
    