#!  /usr/bin/env python

import wx
import os
import os.path

#   ============================================================================
class Resources(object):
#   ============================================================================
    """
    Minimalist resource manager, currently only supporting bitmaps.
    Works off a resource base directory which must have the following layout:
    -   bitmaps     - 16x16     - bitmap1.png
                                - bitmap2.pnp
                                  ...
                    - 32x32     - bitmapA.png
                                - bitmapB.png
                                  ...
                    - 64x64       ...
    The bitmap's base name may be anything but their extension must be png.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, basedir=None):
    #   ------------------------------------------------------------------------
        """
        Trigger resource index creation.
        """
        super(Resources, self).__init__()
        self.xInitialize(basedir or "resources")


    #   ------------------------------------------------------------------------
    def xInitialize(self, basedir):
    #   ------------------------------------------------------------------------
        """
        Index available resources.
        """
        self.xInitializeBitmaps(basedir)


    #   ------------------------------------------------------------------------
    def xInitializeBitmaps(self, basedir):
    #   ------------------------------------------------------------------------
        """
        Index available PNG bitmaps.
        """
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
        """
        Return wx.Bitmap object based on file basename and bitmap size.
        """
        try:
            return self.bitmaps[size][name]
        except:
            print "Bitmap(\"%s\", \"%s\"): No such thing!" % (size, name)
        return None

    #   ------------------------------------------------------------------------
    def Icon(self, size, name):
    #   ------------------------------------------------------------------------
        """
        Return wx.Icon object based on file basename and bitmap size.
        """
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

