#!  /usr/bin/env python

import wx

#   ============================================================================
class AboutBox(wx.AboutDialogInfo):
#   ============================================================================
    """
    The asig applications' About box.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self):
    #   ------------------------------------------------------------------------
        """
        Initialize the About box's textual content.
        """
        super(AboutBox, self).__init__()
        self.SetName("GNU Radio Signal Generator")
        self.SetVersion("0.0")
        self.SetCopyright("(C) 2012 Frank Ludwig (KB3ZOQ)")
        self.AddDeveloper("Frank Ludwig (KB3ZOQ) <ludwig.frank@gmail.com>")
        self.xInitGui()
        
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        """
        Initialize the About box's GUI elements.
        """
        pass
    
    
    #   ------------------------------------------------------------------------
    def Show(self):
    #   ------------------------------------------------------------------------
        """
        Display the About box.
        """
        wx.AboutBox(self)
        