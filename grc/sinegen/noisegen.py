#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Noisegen
# Generated: Thu Dec 20 16:02:30 2012
##################################################

from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class noisegen(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Noisegen")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 48000

		##################################################
		# Blocks
		##################################################
		self.gr_file_source_0 = gr.file_source(gr.sizeof_float*1, "/home/frank/noise.raw", True)
		self.audio_sink_0 = audio.sink(samp_rate, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_file_source_0, 0), (self.audio_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = noisegen()
	tb.Run(True)

