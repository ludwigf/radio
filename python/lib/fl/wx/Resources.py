#!  /usr/bin/env python
#   ****************************************************************************
#   ResourceManager.py
#   ****************************************************************************

import wx
import os
import os.path

#   ============================================================================
class Resources(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, basedir=None):
    #   ------------------------------------------------------------------------
        super(Resources, self).__init__()
        self.Initialize(basedir or "resources")


    #   ------------------------------------------------------------------------
    def Initialize(self, basedir):
    #   ------------------------------------------------------------------------
        self.InitializeBitmaps(basedir)


    #   ------------------------------------------------------------------------
    def InitializeBitmaps(self, basedir):
    #   ------------------------------------------------------------------------
        self.bitmaps = {}
        basedir = os.path.join(basedir, "bitmaps")
        if not os.path.isdir(basedir):
            return
        sizes = os.listdir(basedir)
        for size in sizes:
            sizedir = os.path.join(basedir, size)
            if not os.path.isdir(sizedir):
                continue
            self.bitmaps[size] = {}
            bitmaps = os.listdir(sizedir)
            for bitmap in bitmaps:
                if not bitmap.endswith(".png"):
                    continue
                bitkey = os.path.splitext(bitmap)[0]
                bitfile = os.path.join(sizedir, bitmap)
                self.bitmaps[size][bitkey] = wx.Bitmap(
                    bitfile, wx.BITMAP_TYPE_ANY)

    #   ------------------------------------------------------------------------
    def Bitmap(self, size, name):
    #   ------------------------------------------------------------------------
        try:
            return self.bitmaps[size][name]
        except:
            print "Bitmap(\"%s\", \"%s\"): No such thing!" % (size, name)
        return None

    #   ------------------------------------------------------------------------
    def Icon(self, size, name):
    #   ------------------------------------------------------------------------
        bitmap = self.Bitmap(size, name)
        if not bitmap:
            return None
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(bitmap)
        return icon


#   ============================================================================
if __name__ == "__main__":
#   ============================================================================
    app = wx.App()
    manager = ResourceManager("/home/develop/gnuradio/python/resources")
    print manager.Bitmap("64x64", "radio")
    print manager.Bitmap("0x0", "dummy")

