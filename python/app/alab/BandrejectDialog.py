#!  /usr/bin/env python

import wx

#   ============================================================================
class BandrejectDialog(wx.Dialog):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
        super(BandrejectDialog, self).__init__(parent,
            title="Configure Band Reject Filter")
        self.xInitGui()
        
    #   ------------------------------------------------------------------------
    def GetConfig(self):
    #   ------------------------------------------------------------------------
        config = {"name": str(self.editName.GetValue()),
            "cutoff-low": str(self.editCutoffLow.GetValue()),
            "cutoff-high": str(self.editCutoffHigh.GetValue()),
            "transit": str(self.editTransit.GetValue())}
        return config
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        labelName = wx.StaticText(self, label="Name:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editName = wx.TextCtrl(self, value="", size=(-1,22))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(labelName, proportion=0, flag=wx.ALL, border=2)
        hbox1.Add(self.editName, proportion=1, flag=wx.ALL, border=2)
        
        labelCutoffLow = wx.StaticText(self, label="Cutoff Low:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editCutoffLow = wx.TextCtrl(self, value="300", size=(-1,22))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(labelCutoffLow, proportion=0, flag=wx.ALL, border=2)
        hbox2.Add(self.editCutoffLow, proportion=1, flag=wx.ALL, border=2)
        
        labelCutoffHigh = wx.StaticText(self, label="Cutoff High:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editCutoffHigh = wx.TextCtrl(self, value="3000", size=(-1,22))
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(labelCutoffHigh, proportion=0, flag=wx.ALL, border=2)
        hbox3.Add(self.editCutoffHigh, proportion=1, flag=wx.ALL, border=2)
        
        labelTransit = wx.StaticText(self, label="Transit:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editTransit = wx.TextCtrl(self, value="100", size=(-1,22))
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(labelTransit, proportion=0, flag=wx.ALL, border=2)
        hbox4.Add(self.editTransit, proportion=1, flag=wx.ALL, border=2)
        
        cancelButton = wx.Button(self, wx.ID_CANCEL, label="Cancel")
        okButton = wx.Button(self, wx.ID_OK, label="OK")
        buttons = wx.BoxSizer(wx.HORIZONTAL)
        buttons.AddStretchSpacer(1)
        buttons.Add(cancelButton, proportion=0, flag=wx.ALL, border=2)
        buttons.Add(okButton, proportion=0, flag=wx.ALL, border=2)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(hbox1, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        sizer.Add(hbox2, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        sizer.Add(hbox3, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        sizer.Add(hbox4, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        sizer.AddStretchSpacer(1)
        sizer.Add(buttons, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        self.SetSizer(sizer)
    
    
        