#!  /usr/bin/env python

import wx

#   ============================================================================
class ID:
#   ============================================================================
    MenuFileExit = wx.ID_EXIT
    
    MenuIoAudioIn = 1
    MenuIoUdpIn = 2
    MenuIoFileIn = 3
    MenuIoAudioOut = 4
    
    MenuFilterLowpass = 10
    MenuFilterHighpass = 11
    MenuFilterBandpass = 12
    MenuFilterBandreject = 13
    MenuFilterRemove = 14
    
    MenuHelpAbout = wx.ID_ABOUT
    
    unique_id = 7000
    #   ------------------------------------------------------------------------
    @staticmethod
    def UniqueId():
    #   ------------------------------------------------------------------------
        ID.unique_id +=1
        return ID.unique_id
    
    