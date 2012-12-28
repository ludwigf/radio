#!  /usr/bin/env python

from Frame import Frame

import wx
import os
from fl.wx.Resources import Resources

#   ============================================================================
class App(wx.App):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self):
    #   ------------------------------------------------------------------------
        super(App, self).__init__()
        self.resources = Resources(os.environ["RESOURCES"])
        self.frame = Frame()
    
    #   ------------------------------------------------------------------------
    def PostStatus(self, status):
    #   ------------------------------------------------------------------------
        self.frame.statusbar.PostMessage(status)
        
        
#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
     App().MainLoop()