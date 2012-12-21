#!  /usr/bin/env python

import wx

#   ============================================================================
class FileControl(wx.Panel):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent, value, size=None):
    #   ------------------------------------------------------------------------
        super(FileControl, self).__init__(parent)
        self.xInitGui(value, size)
        
        self.button.Bind(wx.EVT_BUTTON, self.xOnButton)


    #   ------------------------------------------------------------------------
    def GetValue(self):
    #   ------------------------------------------------------------------------
        return self.edit.GetValue()
    
    
    #   ------------------------------------------------------------------------
    def SetValue(self, value):
    #   ------------------------------------------------------------------------
        self.edit.SetValue(value)
        
        
    #   ------------------------------------------------------------------------
    def xInitGui(self, value, size):
    #   ------------------------------------------------------------------------
        self.edit = wx.TextCtrl(self, value=value)
        self.button = wx.Button(self, label="...", size=(22,22))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.edit, proportion=1, flag=wx.ALL, border=0)
        sizer.Add(self.button, proportion=0, flag=wx.ALL, border=0)
        sizer.Fit(self)
        self.SetSizer(sizer)
        self.SetMinSize(size or (200,22))
    
    
    #   ------------------------------------------------------------------------
    def xOnButton(self, event):
    #   ------------------------------------------------------------------------
        dialog = wx.FileDialog(self, "Select File:", "", self.GetValue())
        if dialog.ShowModal() == wx.ID_CANCEL:
            dialog.Destroy()
            return
        self.SetValue(dialog.GetPath())
        dialog.Destroy()
        
    
#   ============================================================================
def Main1():
#   ============================================================================
    app = wx.App()
    frame = wx.Frame(None, -1, "FileControl")
    control = FileCtrl(frame, value="/home/frank/noise.wav")
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.AddSpacer(1)
    sizer.Add(control)
    sizer.AddSpacer(1)
    sizer.Fit(frame)
    frame.SetSizer(sizer)
    frame.Show()
    app.MainLoop()


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    Main1()
