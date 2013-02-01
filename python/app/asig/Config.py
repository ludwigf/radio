#!  /usr/bin/env python

import xml.etree.ElementTree as ET

import wx

#   ============================================================================
class Config(object):
#   ============================================================================
    """
    The application's configuration file manager. It understands the format of
    the config files and calls application frame APIs to apply or retrieve 
    config settings.
    """
    
    #   ------------------------------------------------------------------------
    def __init__(self, frame):
    #   ------------------------------------------------------------------------
        """
        Object initialization.
        """
        self.frame = frame

    #   ------------------------------------------------------------------------
    def LoadConfig(self, filename):
    #    -----------------------------------------------------------------------
        """
        Loads configuration from a given file name.
        """
        wx.GetApp().generator.StopAllSinks()
        wx.GetApp().frame.sinks.StopAll()
        try:
            config = ET.parse(filename).getroot()
            for item in config:
                if item.tag == "signals":
                    self.xLoadConfigSignals(item)
                if item.tag == "sinks":
                    self.xLoadConfigSinks(item)
        except:
            wx.GetApp().PostStatus(
                "Unable to load configuration \"%s\"" % filename)
            return
        wx.GetApp().PostStatus("Loaded configuration \"%s\"" % filename)
            

    #   ------------------------------------------------------------------------
    def xLoadConfigSignals(self, signals):
    #   ------------------------------------------------------------------------
        """
        Retrieves signal configuration from the corresponding XML element 
        stemming from an "asig" configuration file.
        """
        for signal in signals:
            config = signal.attrib
            self.frame.signals.SetConfig(config)
            self.frame.generator.SetSourceConfig(config)
  
        
    #   ------------------------------------------------------------------------
    def xLoadConfigSinks(self, sinks):
    #   ------------------------------------------------------------------------
        """
        Retrieves sink configuration from the corresponding XML element stemming
        from an "asig" configuration file.
        """
        for sink in sinks:
            if sink.tag == "udp":
                self.frame.udpConfig["host"] = sink.attrib["host"]
                self.frame.udpConfig["port"] = int(sink.attrib["port"])
                self.frame.generator.SetUdpConfig(self.frame.udpConfig)
            if sink.tag == "rawfile":
                self.frame.fileConfig["filename"] = sink.attrib["filename"]
                self.frame.generator.SetFileConfig(self.frame.fileConfig)
            if sink.tag == "wavefile":
                self.frame.waveConfig["filename"] = sink.attrib["filename"]
                self.frame.generator.SetWaveConfig(self.frame.waveConfig)
        
        
    #   ------------------------------------------------------------------------
    def SaveConfig(self, filename):
    #   ------------------------------------------------------------------------
        """
        Saves application configuration using the supplied file name.
        """
        asig = ET.Element("asig")
        asig.append(self.xSaveConfigSignals())
        asig.append(self.xSaveConfigSinks())
        
        outfile = open(filename, "w")
        self.xWriteXmlDeclaration(outfile)
        self.xWriteXmlElement(outfile, asig, 0)
        outfile.close()
        wx.GetApp().PostStatus("Saved configuration \"%s\"" % filename)
            

    #   ------------------------------------------------------------------------
    def xSaveConfigSignals(self):
    #   ------------------------------------------------------------------------
        """
        Encodes applicarion signal configuration into an XML element that 
        becomes part of the config file.
        """
        config = self.frame.signals.GetConfig()
        element = ET.Element("signals")
        for item in config:
            child = ET.Element("signal",
                attrib={key: item[key] for key in item})
            element.append(child)
        return element
    
    
    #   ------------------------------------------------------------------------
    def xSaveConfigSinks(self):
    #   ------------------------------------------------------------------------
        """
        Encodes applicarion sink configuration into an XML element that becomes 
        part of the config file.
        """
        element = ET.Element("sinks")
        item = self.frame.fileConfig
        item["type"] = "filesink"
        child = ET.Element("rawfile", attrib={key: item[key] for key in item})
        element.append(child)
        item = self.frame.waveConfig
        item["type"] = "wavesink"
        child = ET.Element("wavefile", attrib={key: item[key] for key in item})
        element.append(child)
        item = self.frame.udpConfig
        item["type"] = "udpsink"
        child = ET.Element("udp", attrib={key: item[key] for key in item})
        element.append(child)
        return element
        
    #   ------------------------------------------------------------------------
    def xWriteXmlDeclaration(self, outfile):
    #   ------------------------------------------------------------------------
        """
        Writes a generic XML declaration.
        """
        outfile.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n")

    #   ------------------------------------------------------------------------
    def xWriteXmlElement(self, outfile, element, level=0):
    #   ------------------------------------------------------------------------
        """
        Writes a given XML element to the given output file. Applies some pretty
        formatting while doing so.
        """
        indent = "  "*level
        opentag = element.tag
        for key in element.keys():
            opentag += " " + key + "=\"" + str(element.get(key)) + "\""
        children = element.getchildren()
        if children:
            outfile.write("%s<%s>\n" % (indent, opentag))
            for child in children:
                self.xWriteXmlElement(outfile, child, level+1)
            outfile.write("%s</%s>\n" % (indent, element.tag))
        else:
            outfile.write("%s<%s/>\n" % (indent, opentag))


