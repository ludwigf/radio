#!  /usr/bin/env python

import wx

#   ============================================================================
class FileMenu(wx.Menu):
#   ============================================================================
    """
    The application's File menu. It binds to the containing menu bar's "handler"
    member as its menu handler.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        """
        Initializes the underlying wx.Menu item and triggers creation of the
        menu items.
        """
        
        super(FileMenu, self).__init__()
        self.xInitGui()
    
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemOpen)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemSave)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemSaveAs)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemExit)
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        """
        Adds the actual menu items.
        """
        
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
    """
    The application's Config menu. It binds to the containing menu bar's 
    "Handler" member as its menu handler.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        """
        Initializes the underlying wx.Menu item and triggers creation of the
        menu items.
        """
        
        super(ConfigMenu, self).__init__()
        self.xInitGui()

        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemUDP)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemFile)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemWave)

    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        """
        Adds the actual menu items.
        """
        
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
    """
    The application's Help menu. It binds to the containing menu bar's 
    "Handler" member as its menu handler.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        """
        Initializes the underlying wx.Menu item and triggers creation of the
        menu items.
        """
        
        super(HelpMenu, self).__init__()
        self.xInitGui()
    
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemAbout)
    
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        """
        Adds the actual menu items.
        """
        
        self.itemAbout = self.Append(
            wx.ID_ABOUT, "A&bout", "About Signal Generator")
        
        
#   ============================================================================
class MenuBar(wx.MenuBar):
#   ============================================================================
    """
    The application's menu bar. It also provides the handler for the menu items
    in all the menus it contains.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, parent, handler=None):
    #   ------------------------------------------------------------------------
        """
        Initializes the underlying wx.MenuBar object and triggers the addition
        of all the application's standard menus.
        """
        
        super(MenuBar, self).__init__()
        self.parent = parent
        self.handler = handler
        self.xInitGui()
        parent.SetMenuBar(self)
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        """
        Adds the application's main menus.
        """
        
        self.Append(FileMenu(self), "&File")
        self.Append(ConfigMenu(self), "&Config")
        self.Append(HelpMenu(self), "&Help")
        
    
    #   ------------------------------------------------------------------------
    def Handler(self, event):
    #   ------------------------------------------------------------------------
        """
        Returns the default handler for all the menu events originating from all
        the menu items it contains. Does any menu updates, then calls an 
        external handler, if provided (typically the handler of the containing
        frame).
        """
        
        if self.handler:
            self.handler(event)
