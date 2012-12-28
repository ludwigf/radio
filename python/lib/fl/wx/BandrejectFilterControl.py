#!  /usr/bin/env python

import wx

#   ============================================================================
class BandrejectFilterControl(wx.Panel):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent, name, cutoff_low=300, cutoff_high=3000,
        transit=100, handlers=[]):
    #   ------------------------------------------------------------------------
        super(BandrejectFilterControl, self).__init__(parent, size=(200,200))
        self.name = name
        self.handlers = handlers
        self.cutoff_low = str(cutoff_low)
        self.cutoff_high = str(cutoff_high)
        self.transit = str(transit)
        self.xInitGui()
        
        self.cutoff_low_edit.Bind(wx.EVT_TEXT_ENTER, self.xHandler)
        self.cutoff_high_edit.Bind(wx.EVT_TEXT_ENTER, self.xHandler)
        self.transit_edit.Bind(wx.EVT_TEXT_ENTER, self.xHandler)

        self.cutoff_low_edit.Bind(wx.EVT_KILL_FOCUS, self.xHandler)
        self.cutoff_high_edit.Bind(wx.EVT_KILL_FOCUS, self.xHandler)
        self.transit_edit.Bind(wx.EVT_KILL_FOCUS, self.xHandler)
        
    #   ------------------------------------------------------------------------
    def Name(self):
    #   ------------------------------------------------------------------------
        return self.name
    
    
    #   ------------------------------------------------------------------------
    def AddHandler(self, handler):
    #   ------------------------------------------------------------------------
        self.handlers.append(handler)
        
    
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        cutoffLabelLow = wx.StaticText(self, label="Cutoff Low:", size=(80,20),
            style=wx.ST_NO_AUTORESIZE)
        self.cutoff_low_edit = wx.TextCtrl(
            self, value=str(self.cutoff_low), size=(60,20),
            style=wx.TE_CENTRE|wx.TE_PROCESS_ENTER)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(cutoffLabelLow, proportion=0, flag=wx.ALL, border=1)
        hbox1.Add(self.cutoff_low_edit, proportion=1, flag=wx.ALL, border=1)
        
        cutoffLabelHigh = wx.StaticText(self, label="Cutoff High:", size=(80,20),
            style=wx.ST_NO_AUTORESIZE)
        self.cutoff_high_edit = wx.TextCtrl(
            self, value=str(self.cutoff_high), size=(60,20),
            style=wx.TE_CENTRE|wx.TE_PROCESS_ENTER)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(cutoffLabelHigh, proportion=0, flag=wx.ALL, border=1)
        hbox2.Add(self.cutoff_high_edit, proportion=1, flag=wx.ALL, border=1)
        
        transitLabel = wx.StaticText(self, label="Transit:", size=(80,20),
            style=wx.ST_NO_AUTORESIZE)
        self.transit_edit = wx.TextCtrl(
            self, value=str(self.transit), size=(60,20),
            style=wx.TE_CENTRE|wx.TE_PROCESS_ENTER)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(transitLabel, proportion=0, flag=wx.ALL, border=1)
        hbox3.Add(self.transit_edit, proportion=1, flag=wx.ALL, border=1)

        staticbox = wx.StaticBox(self, label=self.name)
        staticsizer = wx.StaticBoxSizer(staticbox, wx.VERTICAL)
        staticsizer.AddStretchSpacer(1)
        staticsizer.Add(hbox1, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.Add(hbox2, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.Add(hbox3, proportion=0, flag=wx.EXPAND|wx.ALL, border=1)
        staticsizer.AddStretchSpacer(2)
        staticsizer.Fit(self)
        self.SetSizer(staticsizer)
        
        self.SetMinSize((200,120))
        self.SetMaxSize((200,120))
    
    
    #   ------------------------------------------------------------------------
    def xHandler(self, event):
    #   ------------------------------------------------------------------------
        ctrl = event.GetEventObject()
        value = str(ctrl.GetValue())
        if ctrl == self.cutoff_low_edit:
            if value == self.cutoff_low:
                return
            self.cutoff_low = value
            for handler in self.handlers:
                handler.ProcessCommand(self.name, ("cutoff-low", value))
        if ctrl == self.cutoff_high_edit:
            if value == self.cutoff_high:
                return
            self.cutoff_high = value
            for handler in self.handlers:
                handler.ProcessCommand(self.name, ("cutoff-high", value))
        if ctrl == self.transit_edit:
            if value == self.transit:
                return
            self.transit = value
            for handler in self.handlers:
                handler.ProcessCommand(self.name, ("transit", value))
            
    
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
    frame = wx.Frame(None, -1, "BandrejectFilterControl")
    control = BandrejectFilterControl(frame, name="BR1", handlers=[Handler()])
    control.CenterOnParent()
    frame.Show()
    app.MainLoop()


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    Main1()
