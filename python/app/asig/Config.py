#!  /usr/bin/env python

import xml.etree.ElementTree as ET

import wx

#   ============================================================================
class Config(object):
#   ============================================================================

    #   ------------------------------------------------------------------------
    def __init__(self, frame):
    #   ------------------------------------------------------------------------
        self.frame = frame

    #   ------------------------------------------------------------------------
    def LoadConfig(self, filename):
    #    -----------------------------------------------------------------------
        wx.GetApp().generator.StopAllSinks()
        wx.GetApp().frame.sinks.StopAll()
        try:
            config = ET.parse(filename).getroot()
            for item in config:
                if item.tag == "signals":
                    self.LoadConfigSignals(item)
                if item.tag == "sinks":
                    self.LoadConfigSinks(item)
        except:
            wx.GetApp().PostStatus(
                "Unable to load configuration \"%s\"" % filename)
            return
        wx.GetApp().PostStatus("Loaded configuration \"%s\"" % filename)
            

    #   ------------------------------------------------------------------------
    def LoadConfigSignals(self, signals):
    #   ------------------------------------------------------------------------
        for signal in signals:
            config = signal.attrib
            self.frame.signals.SetConfig(config)
            self.frame.generator.SetSourceConfig(config)
  
        
    #   ------------------------------------------------------------------------
    def LoadConfigSinks(self, sinks):
    #   ------------------------------------------------------------------------
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
        asig = ET.Element("asig")
        asig.append(self.SaveConfigSignals())
        asig.append(self.SaveConfigSinks())
        
        outfile = open(filename, "w")
        self.WriteXmlDeclaration(outfile)
        self.WriteXmlElement(outfile, asig, 0)
        outfile.close()
        wx.GetApp().PostStatus("Saved configuration \"%s\"" % filename)
            

    #   ------------------------------------------------------------------------
    def SaveConfigSignals(self):
    #   ------------------------------------------------------------------------
        config = self.frame.signals.GetConfig()
        element = ET.Element("signals")
        for item in config:
            child = ET.Element("signal",
                attrib={key: item[key] for key in item})
            element.append(child)
        return element
    
    
    #   ------------------------------------------------------------------------
    def SaveConfigSinks(self):
    #   ------------------------------------------------------------------------
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
    def WriteXmlDeclaration(self, outfile):
    #   ------------------------------------------------------------------------
        outfile.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n")

    #   ------------------------------------------------------------------------
    def WriteXmlElement(self, outfile, element, level=0):
    #   ------------------------------------------------------------------------
        indent = "  "*level
        opentag = element.tag
        for key in element.keys():
            opentag += " " + key + "=\"" + str(element.get(key)) + "\""
        children = element.getchildren()
        if children:
            outfile.write("%s<%s>\n" % (indent, opentag))
            for child in children:
                self.WriteXmlElement(outfile, child, level+1)
            outfile.write("%s</%s>\n" % (indent, element.tag))
        else:
            outfile.write("%s<%s/>\n" % (indent, opentag))


