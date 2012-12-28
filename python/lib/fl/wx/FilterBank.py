#!  /usr/bin/env python

from LowpassFilterControl import LowpassFilterControl
from HighpassFilterControl import HighpassFilterControl
from BandpassFilterControl import BandpassFilterControl
from BandrejectFilterControl import BandrejectFilterControl

import wx

#   ============================================================================
class FilterBank(wx.Panel):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent, handlers=[], size=(1000,200)):
    #   ------------------------------------------------------------------------
        super(FilterBank, self).__init__(parent, size=size)
        self.handlers = handlers
        self.filternames = []
        self.filters = []
        self.sizer = None
        self.xInitGui()
        
        
    #   ------------------------------------------------------------------------
    def FilterNames(self):
    #   ------------------------------------------------------------------------
        return [item.Name() for item in self.filters]
    
    
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        if self.sizer:
            self.sizer.Clear()
        staticbox = wx.StaticBox(self, label="")
        self.sizer = wx.StaticBoxSizer(staticbox, wx.HORIZONTAL)
        for ctrl in self.filters:
            self.sizer.Add(ctrl, proportion=0, flag=wx.ALL, border=1)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)
        self.SetMinSize((-1,138))
    
    
    #   ------------------------------------------------------------------------
    def AddLowpassFilter(self, name, cutoff=1000, transit=100):
    #   ------------------------------------------------------------------------
        self.filters.append(LowpassFilterControl(self, name, cutoff, transit,
            handlers=[self]))
        self.xInitGui()
        return
    
    #   ------------------------------------------------------------------------
    def AddHighpassFilter(self, name, cutoff=1000, transit=100):
    #   ------------------------------------------------------------------------
        self.filters.append(HighpassFilterControl(self, name, cutoff, transit,
            handlers=[self]))
        self.xInitGui()
        return
    
    #   ------------------------------------------------------------------------
    def AddBandpassFilter(self, name, cutoff_low=300, cutoff_high=3000,
        transit=100):
    #   ------------------------------------------------------------------------
        self.filters.append(BandpassFilterControl(self, name, cutoff_low, 
            cutoff_high, transit, handlers=[self]))
        self.xInitGui()
        return        
    
    #   ------------------------------------------------------------------------
    def AddBandrejectFilter(self, name, cutoff_low=300, cutoff_high=3000,
        transit=100):
    #   ------------------------------------------------------------------------
        self.filters.append(BandrejectFilterControl(self, name, cutoff_low, 
            cutoff_high, transit, handlers=[self]))
        self.xInitGui()
        return        
    
    #   ------------------------------------------------------------------------
    def RemoveFilter(self, name):
    #   ------------------------------------------------------------------------
        for index in range(len(self.filters)):
            if name != self.filters[index].Name():
                continue
            self.RemoveChild(self.filters[index])
            self.filters[index].Destroy()
            del(self.filters[index])
            self.sizer.Clear()
            self.xInitGui()
            return
        
        
    #   ------------------------------------------------------------------------
    def AddHandler(self, handler):
    #   ------------------------------------------------------------------------
        self.handlers.append(handler)
        
        
    #   ------------------------------------------------------------------------
    def ProcessCommand(self, sender, command):
    #   ------------------------------------------------------------------------
        for handler in self.handlers:
            handler.ProcessCommand(sender, command)
            

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
    frame = wx.Frame(None, -1, "FilterBank", size=(1000,200))
    control = FilterBank(frame, handlers=[Handler()])
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    sizer.Add(control, proportion=1, flag=wx.ALL|wx.EXPAND, border=1)
    frame.SetSizer(sizer)
    frame.SetMinSize(control.GetSize())
    frame.Show()
    control.AddLowpassFilter("LP1")
    control.AddLowpassFilter("LP2")
    control.RemoveFilter("LP1")
    control.AddLowpassFilter("LP3")
    app.MainLoop()


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    Main1()

