#!  /usr/bin/env python

import wx

#   ============================================================================
class ConfigureUdpDialog(wx.Dialog):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent, info={}):
    #   ------------------------------------------------------------------------
        super(ConfigureUdpDialog, self).__init__(
            parent, title="Configure UDP Sink:")
        self.xInitGui(info)
        
    
    #   ------------------------------------------------------------------------
    def GetDestinationHost(self):
    #   ------------------------------------------------------------------------
        return str(self.editDestHost.GetValue())
    
    
    #   ------------------------------------------------------------------------
    def GetDestinationPort(self):
    #   ------------------------------------------------------------------------
        return str(self.editDestPort.GetValue())
    
    
    #   ------------------------------------------------------------------------
    def xInitGui(self, info):
    #   ------------------------------------------------------------------------
        labelDestHost = wx.StaticText(self, label="Destination Host:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editDestHost = wx.TextCtrl(self, size=(-1,20))
        desthost = wx.BoxSizer(wx.HORIZONTAL)
        desthost.Add(labelDestHost, proportion=0, flag=wx.ALL, border=2)
        desthost.Add(self.editDestHost, proportion=1, flag=wx.ALL, border=2)
        
        labelDestPort = wx.StaticText(self, label="Destination Port:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editDestPort = wx.TextCtrl(self, size=(-1,20))
        destport = wx.BoxSizer(wx.HORIZONTAL)
        destport.Add(labelDestPort, proportion=0, flag=wx.ALL, border=2)
        destport.Add(self.editDestPort, proportion=1, flag=wx.ALL, border=2)
        
        cancelButton = wx.Button(self, wx.ID_CANCEL, label="Cancel")
        okButton = wx.Button(self, wx.ID_OK, label="OK")
        buttons = wx.BoxSizer(wx.HORIZONTAL)
        buttons.AddStretchSpacer(1)
        buttons.Add(cancelButton, proportion=0, flag=wx.ALL, border=2)
        buttons.Add(okButton, proportion=0, flag=wx.ALL, border=2)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(desthost, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        sizer.Add(destport, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        sizer.AddStretchSpacer(1)
        sizer.Add(buttons, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        self.SetSizer(sizer)
        
        if "host" in info:
            self.editDestHost.SetValue(info["host"])
        if "port" in info:
            self.editDestPort.SetValue(str(info["port"]))
            
        