#!  /usr/bin/env python

import wx
havePsutil = True
try:
    import psutil
except:
    havePsutil = False
from datetime import datetime

#   ============================================================================
class StatusBar(wx.StatusBar):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent,cpu=True, mem=True, tick=True):
    #   ------------------------------------------------------------------------
        super(StatusBar, self).__init__(parent)
        parent.SetStatusBar(self)
        self.xInitGui(cpu, mem, tick)
        self.xInitTimer()
        if not havePsutil:
            self.PostMessage("Warning: psutil not available")
        
    #   ------------------------------------------------------------------------
    def PostMessage(self, message):
    #   ------------------------------------------------------------------------
        self.SetStatusText(message, 0)
        
    #   ------------------------------------------------------------------------
    def xInitTimer(self):
    #   ------------------------------------------------------------------------
        self.counter = 0
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.xOnTimer, self.timer)
        self.timer.Start(1000)
    
    #   ------------------------------------------------------------------------
    def xInitGui(self, cpu, mem, tick):
    #   ------------------------------------------------------------------------
        widths = [-1]
        self.posCpu = 0
        if havePsutil and cpu:
            self.posCpu = 1
            widths.append(80)
        self.posMem = 0
        if havePsutil and mem:
            self.posMem = self.posCpu + 1
            widths.append(100)
        self.posTick = 0
        if tick:
            self.posTick = self.posMem + 1
            widths.append(60)
        self.SetFieldsCount(1 + self.posTick)
        self.SetStatusWidths(widths)
        
    #   ------------------------------------------------------------------------
    def xOnTimer(self, event):
    #   ------------------------------------------------------------------------
        if self.posTick:
            self.SetStatusText(
                datetime.now().strftime("%H:%M:%S"), self.posTick)
        if self.posCpu and 0 == self.counter % 1:
            self.SetStatusText(
                "CPU: %s%%" % psutil.cpu_percent(0), self.posCpu)
        if self.posMem and 0 == self.counter % 1:
            self.SetStatusText(
                "Free: %.1fMB" % (psutil.avail_phymem()*1e-6,), self.posMem)
        self.counter += 1
        
    
#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    print "Hello, StatusBar!"
