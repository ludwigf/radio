#!  /usr/bin/env python

import wx

from IDs import ID

#   ============================================================================
class FileMenu(wx.Menu):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        super(FileMenu, self).__init__()
        self.xInitGui()
    
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemExit)
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.itemExit = self.Append(
            ID.MenuFileExit, "Exit", "Exit Signal Generator")
            

#   ============================================================================
class FilterMenu(wx.Menu):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        super(FilterMenu, self).__init__()
        self.menubar = menubar
        self.menuRemove = wx.Menu()
        self.removeItems = {}
        self.xInitGui()
        
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemAddLowpass)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemAddHighpass)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemAddBandpass)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemAddBandreject)
        

    #   ------------------------------------------------------------------------
    def AddConfiguredFilter(self, name):
    #   ------------------------------------------------------------------------
        key = ID.UniqueId()
        self.removeItems[key] = name
        item = self.menuRemove.Append(key, name, "Remove filter \"%s\"" % name)
        self.menubar.parent.Bind(wx.EVT_MENU, self.menubar.Handler, item)
        self.Enable(ID.MenuFilterRemove, True)
            
    
    #   ------------------------------------------------------------------------
    def RemoveConfiguredFilter(self, name):
    #   ------------------------------------------------------------------------
        if name not in self.removeItems.values():
            return
        for key in self.removeItems:
            if name == self.removeItems[key]:
                break
        self.menuRemove.Delete(key)
        del(self.removeItems[key])
        if not self.removeItems:
            self.Enable(ID.MenuFilterRemove, False)
            
    
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        bmp = wx.GetApp().resources.Bitmap("16x16", "lowpass")
        self.itemAddLowpass = wx.MenuItem(
            self, ID.MenuFilterLowpass, "Add Lowpass ...", 
            "Configure Lowpass Filter")
        self.itemAddLowpass.SetBitmap(bmp)
        self.AppendItem(self.itemAddLowpass)
        
        bmp = wx.GetApp().resources.Bitmap("16x16", "highpass")
        self.itemAddHighpass = wx.MenuItem(
            self, ID.MenuFilterHighpass, "Add Highpass ...", 
            "Configure Highpass Filter")
        self.itemAddHighpass.SetBitmap(bmp)
        self.AppendItem(self.itemAddHighpass)
        
        bmp = wx.GetApp().resources.Bitmap("16x16", "bandpass")
        self.itemAddBandpass = wx.MenuItem(
            self, ID.MenuFilterBandpass, "Add Bandpass ...", 
            "Configure Bandpass Filter")
        self.itemAddBandpass.SetBitmap(bmp)
        self.AppendItem(self.itemAddBandpass)
        
        bmp = wx.GetApp().resources.Bitmap("16x16", "bandreject")
        self.itemAddBandreject = wx.MenuItem(
            self, ID.MenuFilterBandreject, "Add Bandreject ...", 
            "Configure Band Reject Filter")
        self.itemAddBandreject.SetBitmap(bmp)
        self.AppendItem(self.itemAddBandreject)
        
        self.AppendSeparator()
        self.AppendMenu(ID.MenuFilterRemove, "Remove Filter", self.menuRemove)
        self.Enable(ID.MenuFilterRemove, False)

                
#   ============================================================================
class IoMenu(wx.Menu):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, menubar):
    #   ------------------------------------------------------------------------
        super(IoMenu, self).__init__()
        self.xInitGui()
        
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemAudioIn)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemUdpIn)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemFileIn)
        menubar.parent.Bind(wx.EVT_MENU, menubar.Handler, self.itemAudioOut)

    #   ------------------------------------------------------------------------
    def ResetInputs(self):
    #   ------------------------------------------------------------------------
        self.itemAudioIn.Check(False)
        self.itemUdpIn.Check(False)
        self.itemFileIn.Check(False)
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.itemAudioIn = wx.MenuItem(
            self, ID.MenuIoAudioIn, "Audio In", "Activate \"Audio In\"", 
            kind=wx.ITEM_CHECK)
        self.AppendItem(self.itemAudioIn)
        self.itemUdpIn = wx.MenuItem(
            self, ID.MenuIoUdpIn, "UDP In ...", "Activate \"UDP In\"", 
            kind=wx.ITEM_CHECK)
        self.AppendItem(self.itemUdpIn)
        self.itemFileIn = wx.MenuItem(
            self, ID.MenuIoFileIn, "File In ...", "Activate \"Raw File In\"", 
            kind=wx.ITEM_CHECK)
        self.AppendItem(self.itemFileIn)
    
        self.AppendSeparator()
        self.itemAudioOut = wx.MenuItem(
            self, ID.MenuIoAudioOut, "Audio Out", "Activate \"Audio Out\"", 
            kind=wx.ITEM_CHECK)
        self.AppendItem(self.itemAudioOut)
            
    #   ------------------------------------------------------------------------
    def xSetDeviceActive(self, device):
    #   ------------------------------------------------------------------------
        print "Setting active device", device
        if device == ID.MenuIoAudioIn and self.itemAudioIn.IsChecked():
            self.itemUdpIn.Check(False)
            self.itemFileIn.Check(False)
        if device == ID.MenuIoUdpIn and self.itemUdpIn.IsChecked():
            self.itemAudioIn.Check(False)
            self.itemFileIn.Check(False)
        if device == ID.MenuIoFileIn and self.itemFileIn.IsChecked():
            self.itemAudioIn.Check(False)
            self.itemUdpIn.Check(False)
    
    
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
            ID.MenuHelpAbout, "A&bout", "About FilterLab")
        
        
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
    def AddConfiguredFilter(self, name):
    #   ------------------------------------------------------------------------
        self.filtermenu.AddConfiguredFilter(name)
        
        
    #   ------------------------------------------------------------------------
    def RemoveConfiguredFilter(self, name):
    #   ------------------------------------------------------------------------
        self.filtermenu.RemoveConfiguredFilter(name)
        
    
    #   ------------------------------------------------------------------------
    def ResetIoInputs(self):
    #   ------------------------------------------------------------------------
        self.iomenu.ResetInputs()
        
        
    #   ------------------------------------------------------------------------
    def xInitGui(self):
    #   ------------------------------------------------------------------------
        self.filemenu = FileMenu(self)
        self.Append(self.filemenu, "&File")
        self.iomenu = IoMenu(self)
        self.Append(self.iomenu, "I&/O")
        self.filtermenu = FilterMenu(self)
        self.Append(self.filtermenu, "&Filters")
        self.helpmenu = HelpMenu(self)
        self.Append(self.helpmenu, "&Help")
        
    
    #   ------------------------------------------------------------------------
    def Handler(self, event):
    #   ------------------------------------------------------------------------
        command = event.GetId()
        if command in self.filtermenu.removeItems:
            event.SetId(ID.MenuFilterRemove)
            event.filtername = self.filtermenu.removeItems[command]
        if self.handler:
            self.handler(event)
        if command in (ID.MenuIoAudioIn, ID.MenuIoUdpIn, ID.MenuIoFileIn, 
                ID.MenuIoAudioOut):
            self.iomenu.xSetDeviceActive(command)
            
            