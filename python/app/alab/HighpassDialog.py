#!  /usr/bin/env python

import wx

#   ============================================================================
class HighpassDialog(wx.Dialog):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent):
    #   ------------------------------------------------------------------------
        super(HighpassDialog, self).__init__(parent,
            title="Configure Highpass Filter")
        self.xInitGui()
        
    #   ------------------------------------------------------------------------
    def GetConfig(self):
    #   ------------------------------------------------------------------------
        config = {"name": str(self.editName.GetValue()),
            "cutoff": str(self.editCutoff.GetValue()),
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
        
        labelCutoff = wx.StaticText(self, label="Cutoff:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editCutoff = wx.TextCtrl(self, value="1000", size=(-1,22))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(labelCutoff, proportion=0, flag=wx.ALL, border=2)
        hbox2.Add(self.editCutoff, proportion=1, flag=wx.ALL, border=2)
        
        labelTransit = wx.StaticText(self, label="Transit:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editTransit = wx.TextCtrl(self, value="100", size=(-1,22))
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(labelTransit, proportion=0, flag=wx.ALL, border=2)
        hbox3.Add(self.editTransit, proportion=1, flag=wx.ALL, border=2)
        
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
        sizer.AddStretchSpacer(1)
        sizer.Add(buttons, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        self.SetSizer(sizer)
    
    
        