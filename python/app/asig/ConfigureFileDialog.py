#!  /usr/bin/env python

import wx

from fl.wx.FileControl import FileControl

#   ============================================================================
class ConfigureFileDialog(wx.Dialog):
#   ============================================================================
    """
    Dialog to allow customization of the application's File sink.
    """

    #   ------------------------------------------------------------------------
    def __init__(self, parent, info={}):
    #   ------------------------------------------------------------------------
        """
        Initialize underlying wx.Dialog object and setup dialog GUI.
        """
        super(ConfigureFileDialog, self).__init__(
            parent, title="Configure Raw File Sink:")
        self.xInitGui(info)
        
    
    #   ------------------------------------------------------------------------
    def GetDestinationFile(self):
    #   ------------------------------------------------------------------------
        """
        Return full path name of the File sink's underlying disk file.
        """
        
        return str(self.editDestFile.GetValue())
    
    
    #   ------------------------------------------------------------------------
    def xInitGui(self, info):
    #   ------------------------------------------------------------------------
        """
        Initialize dialog's GUI elements. Initial values are passed through the
        method's info parameter.
        """
        
        labelDestFile = wx.StaticText(self, label="File Name:", 
            size=(120,20), style=wx.ST_NO_AUTORESIZE)
        self.editDestFile = FileControl(self, value="", size=(-1,22))
        destfile = wx.BoxSizer(wx.HORIZONTAL)
        destfile.Add(labelDestFile, proportion=0, flag=wx.ALL, border=2)
        destfile.Add(self.editDestFile, proportion=1, flag=wx.ALL, border=2)
        
        cancelButton = wx.Button(self, wx.ID_CANCEL, label="Cancel")
        okButton = wx.Button(self, wx.ID_OK, label="OK")
        buttons = wx.BoxSizer(wx.HORIZONTAL)
        buttons.AddStretchSpacer(1)
        buttons.Add(cancelButton, proportion=0, flag=wx.ALL, border=2)
        buttons.Add(okButton, proportion=0, flag=wx.ALL, border=2)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(destfile, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        sizer.AddStretchSpacer(1)
        sizer.Add(buttons, proportion=0, flag=wx.ALL|wx.EXPAND, border=2)
        self.SetSizer(sizer)
        
        if "filename" in info:
            self.editDestFile.SetValue(info["filename"])
            
        