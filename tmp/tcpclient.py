#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Tcpclient
# Generated: Tue Dec 18 16:11:04 2012
##################################################

from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class tcpclient(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Tcpclient")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 48000

		##################################################
		# Blocks
		##################################################
		self.gr_noise_source_x_0 = gr.noise_source_f(gr.GR_IMPULSE, 1, 0)
		self.gr_file_sink_0 = gr.file_sink(gr.sizeof_float*1, "/home/frank/noise.raw")
		self.gr_file_sink_0.set_unbuffered(False)
		self.audio_sink_0 = audio.sink(samp_rate, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_noise_source_x_0, 0), (self.audio_sink_0, 0))
		self.connect((self.gr_noise_source_x_0, 0), (self.gr_file_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = tcpclient()
	tb.Run(True)

