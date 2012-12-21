#!  /usr/bin/env python

from Frame import Frame

import wx
import os
from fl.wx.Resources import Resources

#   ============================================================================
class App(wx.App):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, signals, noises, sinks):
    #   ------------------------------------------------------------------------
        super(App, self).__init__()
        self.resources = Resources(os.environ["RESOURCES"])
        self.frame = Frame(signals, noises, sinks)
        self.generator = self.frame.generator
    
    #   ------------------------------------------------------------------------
    def PostStatus(self, status):
    #   ------------------------------------------------------------------------
        self.frame.statusbar.PostMessage(status)
        
        
#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    signals = ["S1", "S2", "S3", "S4"]
    noises = ["N1"]
    sinks = [("Audio Out", True), ("UDP Out", True), ("File Out", True),
        ("Wave Out", True)]
    
    App(signals, noises, sinks).MainLoop()
