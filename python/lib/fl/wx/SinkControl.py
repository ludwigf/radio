#!  /usr/bin/env python

import wx

#   ============================================================================
class SinkControl(wx.Panel):
#   ============================================================================
    """
    wx.Panel based control to turn signal sinks (such as Audio Out, File Out, 
    ...) on or off.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, parent, name, state=True, handlers=[]):
    #   ------------------------------------------------------------------------
        """
        Initialize the underlying wx component and trigger creation of the user
        interface. Wire embedded controls to the embedded command handler.
        """
        super(SinkControl, self).__init__(parent, size=(200,120))
        self.name = name
        self.handlers = handlers
        self.xInitGui(state)
        
        self.runButton.Bind(wx.EVT_BUTTON, self.xHandler)

    #   ------------------------------------------------------------------------
    def SetHandlers(self, handlers):
    #   ------------------------------------------------------------------------
        """
        Set list of external command handlers to be called when settings change
        (in addition to the internal handler).
        """
        self.handlers = handlers
              
    #   ------------------------------------------------------------------------
    def SetStatus(self, status):
    #   ------------------------------------------------------------------------
        """
        Set GUI state to either ON or OFF. Used to adjust GUI state in response
        to external events such as a configuration change.
        """
        if status == "on":
            self.runButton.SetLabel("Stop")
        if status == "off":
            self.runButton.SetLabel("Start")
    
    #   ------------------------------------------------------------------------
    def xInitGui(self, state):
    #   ------------------------------------------------------------------------
        """
        Create the signal control user interface.
        """
        sinkLabel = wx.StaticText(self, label=self.name)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.AddStretchSpacer(1)
        hbox1.Add(sinkLabel, proportion=0, flag=wx.ALL, border=1)
        hbox1.AddStretchSpacer(1)
        
        label = "Start"
        if state == False:
            label = "Stop"
        self.runButton = wx.Button(self, label=label, size=(80,20))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.AddStretchSpacer(1)
        hbox2.Add(self.runButton, proportion=0, flag=wx.ALL, border=1)
        hbox2.AddStretchSpacer(1)
        
        staticbox = wx.StaticBox(self, label="")
        staticsizer = wx.StaticBoxSizer(staticbox, wx.VERTICAL)
        staticsizer.AddStretchSpacer(2)
        staticsizer.Add(hbox1, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.AddStretchSpacer(1)
        staticsizer.Add(hbox2, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.AddStretchSpacer(2)
        staticsizer.Fit(self)
        self.SetSizer(staticsizer)
        
        self.SetMinSize((120,80))
        self.SetMaxSize((120,80))
    
    
    #   ------------------------------------------------------------------------
    def xHandler(self, event):
    #   ------------------------------------------------------------------------
        """
        Internal event handler. Creates command based on current control 
        settings then triggers invokation of external command handlers.
        """
        sender = event.GetEventObject()
        if sender == self.runButton:
            if sender.GetLabel() == "Start":
                command = ("run", "true")
                self.xProcessCommand(command)
                sender.SetLabel("Stop")
                return        
            if sender.GetLabel() == "Stop":
                command = ("run", "false")
                self.xProcessCommand(command)
                sender.SetLabel("Start")
                return        

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
    control = SinkControl(frame, name="Audio Out", handlers=[Handler()])
    control.CenterOnParent()
    frame.Show()
    app.MainLoop()


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    Main1()
    