#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Dec 13 13:39:01 2012
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
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
		self.samp_rate = samp_rate = 2.048e6

		##################################################
		# Blocks
		##################################################
		self.osmosdr_source_c_0 = osmosdr.source_c( args="nchan=" + str(1) + " " + "" )
		self.osmosdr_source_c_0.set_sample_rate(samp_rate)
		self.osmosdr_source_c_0.set_center_freq(88.5e6, 0)
		self.osmosdr_source_c_0.set_freq_corr(0, 0)
		self.osmosdr_source_c_0.set_gain_mode(0, 0)
		self.osmosdr_source_c_0.set_gain(50, 0)
		self.osmosdr_source_c_0.set_if_gain(2, 0)
			
		self.low_pass_filter_0 = gr.fir_filter_ccf(8, firdes.low_pass(
			8, samp_rate, 150e3, 5e3, firdes.WIN_HAMMING, 6.76))
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_fff(
			interpolation=48000,
			decimation=64000,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_fm_demod_cf_0 = blks2.fm_demod_cf(
			channel_rate=256e3,
			audio_decim=4,
			deviation=5000,
			audio_pass=3000,
			audio_stop=4000,
			gain=1.0,
			tau=75e-6,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.blks2_fm_demod_cf_0, 0), (self.blks2_rational_resampler_xxx_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
		self.connect((self.osmosdr_source_c_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.blks2_fm_demod_cf_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.osmosdr_source_c_0.set_sample_rate(self.samp_rate)
		self.low_pass_filter_0.set_taps(firdes.low_pass(8, self.samp_rate, 150e3, 5e3, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

