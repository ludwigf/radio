#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: sinegen
# Author: Frank Ludwig <ludwig.frank@gmail.com>
# Description: Minimal GUI sinwave generator
# Generated: Wed Nov 14 16:42:22 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

#   ============================================================================
class top_block(grc_wxgui.top_block_gui):
#   ============================================================================

    #   ------------------------------------------------------------------------
	def __init__(self):
    #   ------------------------------------------------------------------------
		grc_wxgui.top_block_gui.__init__(self, title="sinegen")
		#_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		#self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		# Variables
		self.samp_rate = samp_rate = 48000

		# Blocks
		self.scopesink = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.scopesink.win)

		self.source = gr.sig_source_f(samp_rate, gr.GR_SIN_WAVE, 1000, 1, 0)

		# Connections
		self.connect((self.source, 0), (self.scopesink, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.source.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink.set_sample_rate(self.samp_rate)

#   ============================================================================
if __name__ == '__main__':
#   ============================================================================
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
    try:
	    tb.Run(True)
    except:
        pass


