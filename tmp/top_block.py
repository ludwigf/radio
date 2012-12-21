#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Dec 12 17:12:55 2012
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 1536e3
		self.cfreq = cfreq = 100.3e6

		##################################################
		# Blocks
		##################################################
		self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
			self.GetWin(),
			baseband_freq=cfreq,
			dynamic_range=100,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=512,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="Waterfall Plot",
		)
		self.Add(self.wxgui_waterfallsink2_0.win)
		def wxgui_waterfallsink2_0_callback(x, y):
			self.set_cfreq(x)
		
		self.wxgui_waterfallsink2_0.set_callback(wxgui_waterfallsink2_0_callback)
		self.osmosdr_source_c_0 = osmosdr.source_c( args="nchan=" + str(1) + " " + "" )
		self.osmosdr_source_c_0.set_sample_rate(samp_rate)
		self.osmosdr_source_c_0.set_center_freq(cfreq, 0)
		self.osmosdr_source_c_0.set_freq_corr(0, 0)
		self.osmosdr_source_c_0.set_gain_mode(0, 0)
		self.osmosdr_source_c_0.set_gain(20, 0)
		self.osmosdr_source_c_0.set_if_gain(30, 0)
			
		self.low_pass_filter_0 = gr.fir_filter_ccf(8, firdes.low_pass(
			1, 1536000, 50e3, 1e3, firdes.WIN_HAMMING, 0))
		self.blks2_fm_demod_cf_0 = blks2.fm_demod_cf(
			channel_rate=192e3,
			audio_decim=4,
			deviation=75000,
			audio_pass=3000,
			audio_stop=4000,
			gain=2,
			tau=100e-6,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.osmosdr_source_c_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.blks2_fm_demod_cf_0, 0))
		self.connect((self.blks2_fm_demod_cf_0, 0), (self.audio_sink_0, 0))
		self.connect((self.osmosdr_source_c_0, 0), (self.wxgui_waterfallsink2_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.osmosdr_source_c_0.set_sample_rate(self.samp_rate)
		self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)

	def get_cfreq(self):
		return self.cfreq

	def set_cfreq(self, cfreq):
		self.cfreq = cfreq
		self.osmosdr_source_c_0.set_center_freq(self.cfreq, 0)
		self.wxgui_waterfallsink2_0.set_baseband_freq(self.cfreq)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

