#!  /usr/bin/env python

import wx

#   ============================================================================
class FileMenu(wx.Menu):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        super(FileMenu, self).__init__()
        self.xInitGui()
    
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemOpen)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemSave)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemSaveAs)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemExit)
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.itemOpen = self.Append(
            wx.ID_OPEN, "Open", "Load Generator Configuration")
        self.itemSave = self.Append(
            wx.ID_SAVE, "Save", "Save Generator Configuration")
        self.itemSaveAs = self.Append(
            wx.ID_SAVEAS, "Save As ...", "Save Generator Configuration As ...")
        self.AppendSeparator()
        self.itemExit = self.Append(
            wx.ID_EXIT, "Exit", "Exit Signal Generator")
            

#   ============================================================================
class ConfigMenu(wx.Menu):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        super(ConfigMenu, self).__init__()
        self.xInitGui()

        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemUDP)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemFile)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemWave)

    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        bmp = wx.GetApp().resources.Bitmap("16x16", "udpsink")
        self.itemUDP = wx.MenuItem(
            self, wx.ID_FILE1, "UDP Sink...", "Configure UDP Sink")
        self.itemUDP.SetBitmap(bmp)
        self.AppendItem(self.itemUDP)

        bmp = wx.GetApp().resources.Bitmap("16x16", "filesink")
        self.itemFile = wx.MenuItem(
            self, wx.ID_FILE2, "File Sink...", "Configure Raw File Sink")
        self.itemFile.SetBitmap(bmp)
        self.AppendItem(self.itemFile)

        bmp = wx.GetApp().resources.Bitmap("16x16", "wavesink")
        self.itemWave = wx.MenuItem(
            self, wx.ID_FILE3, "Wave Sink...", "Configure Wave File Sink")
        self.itemWave.SetBitmap(bmp)
        self.AppendItem(self.itemWave)


#   ============================================================================
class HelpMenu(wx.Menu):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        super(HelpMenu, self).__init__()
        self.xInitGui()
    
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemAbout)
    
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.itemAbout = self.Append(
            wx.ID_ABOUT, "A&bout", "About Signal Generator")
        
        
#   ============================================================================
class MenuBar(wx.MenuBar):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, parent, handler=None):
    #   ------------------------------------------------------------------------
        super(MenuBar, self).__init__()
        self.parent = parent
        self.handler = handler
        self.xInitGui()
        parent.SetMenuBar(self)
        
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.Append(FileMenu(self), "&File")
        self.Append(ConfigMenu(self), "&Config")
        self.Append(HelpMenu(self), "&Help")
        
    
    #   ------------------------------------------------------------------------
    def Handler(self, event):
    #   ------------------------------------------------------------------------
        if self.handler:
            self.handler(event)
