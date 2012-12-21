#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Siggen
# Generated: Sat Dec 15 13:40:02 2012
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import histosink_gl
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class siggen(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Siggen")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 48000
		self.m4 = m4 = True
		self.m3 = m3 = True
		self.m2 = m2 = True
		self.m1 = m1 = True
		self.gain4 = gain4 = 0
		self.gain3 = gain3 = 0
		self.gain2 = gain2 = 0
		self.gain1 = gain1 = 0
		self.freq4 = freq4 = 400
		self.freq3 = freq3 = 400
		self.freq2 = freq2 = 400
		self.freq1 = freq1 = 400
		self.form4 = form4 = gr.GR_SIN_WAVE
		self.form3 = form3 = gr.GR_SIN_WAVE
		self.form2 = form2 = gr.GR_SIN_WAVE
		self.form1 = form1 = gr.GR_SIN_WAVE

		##################################################
		# Blocks
		##################################################
		self.notebook = self.notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Scope")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "FFT")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Histo")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Water")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Number")
		self.Add(self.notebook)
		self._m4_check_box = forms.check_box(
			parent=self.GetWin(),
			value=self.m4,
			callback=self.set_m4,
			label='m4',
			true=True,
			false=False,
		)
		self.GridAdd(self._m4_check_box, 3, 5, 1, 1)
		self._m3_check_box = forms.check_box(
			parent=self.GetWin(),
			value=self.m3,
			callback=self.set_m3,
			label='m3',
			true=True,
			false=False,
		)
		self.GridAdd(self._m3_check_box, 2, 5, 1, 1)
		self._m2_check_box = forms.check_box(
			parent=self.GetWin(),
			value=self.m2,
			callback=self.set_m2,
			label='m2',
			true=True,
			false=False,
		)
		self.GridAdd(self._m2_check_box, 1, 5, 1, 1)
		self._m1_check_box = forms.check_box(
			parent=self.GetWin(),
			value=self.m1,
			callback=self.set_m1,
			label='m1',
			true=True,
			false=False,
		)
		self.GridAdd(self._m1_check_box, 0, 5, 1, 1)
		_gain4_sizer = wx.BoxSizer(wx.VERTICAL)
		self._gain4_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_gain4_sizer,
			value=self.gain4,
			callback=self.set_gain4,
			label='gain4',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._gain4_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_gain4_sizer,
			value=self.gain4,
			callback=self.set_gain4,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_gain4_sizer, 3, 0, 1, 1)
		_gain3_sizer = wx.BoxSizer(wx.VERTICAL)
		self._gain3_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_gain3_sizer,
			value=self.gain3,
			callback=self.set_gain3,
			label='gain3',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._gain3_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_gain3_sizer,
			value=self.gain3,
			callback=self.set_gain3,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_gain3_sizer, 2, 0, 1, 1)
		_gain2_sizer = wx.BoxSizer(wx.VERTICAL)
		self._gain2_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_gain2_sizer,
			value=self.gain2,
			callback=self.set_gain2,
			label='gain2',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._gain2_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_gain2_sizer,
			value=self.gain2,
			callback=self.set_gain2,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_gain2_sizer, 1, 0, 1, 1)
		_gain1_sizer = wx.BoxSizer(wx.VERTICAL)
		self._gain1_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_gain1_sizer,
			value=self.gain1,
			callback=self.set_gain1,
			label='gain1',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._gain1_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_gain1_sizer,
			value=self.gain1,
			callback=self.set_gain1,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_gain1_sizer, 0, 0, 1, 1)
		_freq4_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq4_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_freq4_sizer,
			value=self.freq4,
			callback=self.set_freq4,
			label='freq4',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq4_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_freq4_sizer,
			value=self.freq4,
			callback=self.set_freq4,
			minimum=0,
			maximum=10000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_freq4_sizer, 3, 1, 1, 3)
		_freq3_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq3_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_freq3_sizer,
			value=self.freq3,
			callback=self.set_freq3,
			label='freq3',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq3_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_freq3_sizer,
			value=self.freq3,
			callback=self.set_freq3,
			minimum=0,
			maximum=10000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_freq3_sizer, 2, 1, 1, 3)
		_freq2_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq2_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_freq2_sizer,
			value=self.freq2,
			callback=self.set_freq2,
			label='freq2',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq2_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_freq2_sizer,
			value=self.freq2,
			callback=self.set_freq2,
			minimum=0,
			maximum=10000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_freq2_sizer, 1, 1, 1, 3)
		_freq1_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq1_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_freq1_sizer,
			value=self.freq1,
			callback=self.set_freq1,
			label='freq1',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq1_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_freq1_sizer,
			value=self.freq1,
			callback=self.set_freq1,
			minimum=0,
			maximum=10000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_freq1_sizer, 0, 1, 1, 3)
		self._form4_chooser = forms.radio_buttons(
			parent=self.GetWin(),
			value=self.form4,
			callback=self.set_form4,
			label='form4',
			choices=[gr.GR_SIN_WAVE,gr.GR_SQR_WAVE,gr.GR_TRI_WAVE,gr.GR_SAW_WAVE],
			labels=["Sine", "Square", "Triangle", "Saw"],
			style=wx.RA_HORIZONTAL,
		)
		self.GridAdd(self._form4_chooser, 3, 4, 1, 1)
		self._form3_chooser = forms.radio_buttons(
			parent=self.GetWin(),
			value=self.form3,
			callback=self.set_form3,
			label='form3',
			choices=[gr.GR_SIN_WAVE,gr.GR_SQR_WAVE,gr.GR_TRI_WAVE,gr.GR_SAW_WAVE],
			labels=["Sine", "Square", "Triangle", "Saw"],
			style=wx.RA_HORIZONTAL,
		)
		self.GridAdd(self._form3_chooser, 2, 4, 1, 1)
		self._form2_chooser = forms.radio_buttons(
			parent=self.GetWin(),
			value=self.form2,
			callback=self.set_form2,
			label='form2',
			choices=[gr.GR_SIN_WAVE,gr.GR_SQR_WAVE,gr.GR_TRI_WAVE,gr.GR_SAW_WAVE],
			labels=["Sine", "Square", "Triangle", "Saw"],
			style=wx.RA_HORIZONTAL,
		)
		self.GridAdd(self._form2_chooser, 1, 4, 1, 1)
		self._form1_chooser = forms.radio_buttons(
			parent=self.GetWin(),
			value=self.form1,
			callback=self.set_form1,
			label='form1',
			choices=[gr.GR_SIN_WAVE,gr.GR_SQR_WAVE,gr.GR_TRI_WAVE,gr.GR_SAW_WAVE],
			labels=["Sine", "Square", "Triangle", "Saw"],
			style=wx.RA_HORIZONTAL,
		)
		self.GridAdd(self._form1_chooser, 0, 4, 1, 1)
		self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_f(
			self.notebook.GetPage(3).GetWin(),
			baseband_freq=0,
			dynamic_range=100,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=512,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="Waterfall Plot",
			size=(800,400),
		)
		self.notebook.GetPage(3).Add(self.wxgui_waterfallsink2_0.win)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.notebook.GetPage(0).GetWin(),
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
			size=(800,400),
		)
		self.notebook.GetPage(0).Add(self.wxgui_scopesink2_0.win)
		self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
			self.notebook.GetPage(4).GetWin(),
			unit="Units",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate,
			number_rate=15,
			average=False,
			avg_alpha=None,
			label="Number Plot",
			peak_hold=False,
			show_gauge=True,
		)
		self.notebook.GetPage(4).Add(self.wxgui_numbersink2_0.win)
		self.wxgui_histosink2_0 = histosink_gl.histo_sink_f(
			self.notebook.GetPage(2).GetWin(),
			title="Histogram Plot",
			num_bins=27,
			frame_size=1000,
			size=(800,400),
		)
		self.notebook.GetPage(2).Add(self.wxgui_histosink2_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
			self.notebook.GetPage(1).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
			size=(800,400),
		)
		self.notebook.GetPage(1).Add(self.wxgui_fftsink2_0.win)
		self.signal4 = gr.sig_source_f(samp_rate, form4, freq4, 1, 0)
		self.signal3 = gr.sig_source_f(samp_rate, form3, freq3, 1, 0)
		self.signal2 = gr.sig_source_f(samp_rate, form2, freq2, 1, 0)
		self.signal1 = analog.sig_source_f(samp_rate, form1, freq1, 1, 0)
		self.mute4 = gr.mute_ff(bool(m4))
		self.mute3 = gr.mute_ff(bool(m3))
		self.mute2 = gr.mute_ff(bool(m2))
		self.mute1 = gr.mute_ff(bool(m1))
		self.mult4 = gr.multiply_const_vff((gain4, ))
		self.mult3 = gr.multiply_const_vff((gain3, ))
		self.mult2 = gr.multiply_const_vff((gain2, ))
		self.mult1 = gr.multiply_const_vff((gain1, ))
		self.divide = gr.multiply_const_vff((0.25, ))
		self.audio_sink_0 = audio.sink(samp_rate, "", True)
		self.add = gr.add_vff(1)

		##################################################
		# Connections
		##################################################
		self.connect((self.divide, 0), (self.audio_sink_0, 0))
		self.connect((self.mult4, 0), (self.add, 3))
		self.connect((self.mult3, 0), (self.add, 2))
		self.connect((self.mult2, 0), (self.add, 1))
		self.connect((self.divide, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.divide, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.divide, 0), (self.wxgui_histosink2_0, 0))
		self.connect((self.divide, 0), (self.wxgui_waterfallsink2_0, 0))
		self.connect((self.signal2, 0), (self.mute2, 0))
		self.connect((self.mute2, 0), (self.mult2, 0))
		self.connect((self.signal1, 0), (self.mute1, 0))
		self.connect((self.mute1, 0), (self.mult1, 0))
		self.connect((self.mult1, 0), (self.add, 0))
		self.connect((self.signal4, 0), (self.mute4, 0))
		self.connect((self.mute4, 0), (self.mult4, 0))
		self.connect((self.signal3, 0), (self.mute3, 0))
		self.connect((self.mute3, 0), (self.mult3, 0))
		self.connect((self.add, 0), (self.divide, 0))
		self.connect((self.divide, 0), (self.wxgui_numbersink2_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
		self.signal2.set_sampling_freq(self.samp_rate)
		self.signal1.set_sampling_freq(self.samp_rate)
		self.signal4.set_sampling_freq(self.samp_rate)
		self.signal3.set_sampling_freq(self.samp_rate)

	def get_m4(self):
		return self.m4

	def set_m4(self, m4):
		self.m4 = m4
		self.mute4.set_mute(bool(self.m4))
		self._m4_check_box.set_value(self.m4)

	def get_m3(self):
		return self.m3

	def set_m3(self, m3):
		self.m3 = m3
		self.mute3.set_mute(bool(self.m3))
		self._m3_check_box.set_value(self.m3)

	def get_m2(self):
		return self.m2

	def set_m2(self, m2):
		self.m2 = m2
		self.mute2.set_mute(bool(self.m2))
		self._m2_check_box.set_value(self.m2)

	def get_m1(self):
		return self.m1

	def set_m1(self, m1):
		self.m1 = m1
		self._m1_check_box.set_value(self.m1)
		self.mute1.set_mute(bool(self.m1))

	def get_gain4(self):
		return self.gain4

	def set_gain4(self, gain4):
		self.gain4 = gain4
		self._gain4_slider.set_value(self.gain4)
		self._gain4_text_box.set_value(self.gain4)
		self.mult4.set_k((self.gain4, ))

	def get_gain3(self):
		return self.gain3

	def set_gain3(self, gain3):
		self.gain3 = gain3
		self._gain3_slider.set_value(self.gain3)
		self._gain3_text_box.set_value(self.gain3)
		self.mult3.set_k((self.gain3, ))

	def get_gain2(self):
		return self.gain2

	def set_gain2(self, gain2):
		self.gain2 = gain2
		self._gain2_slider.set_value(self.gain2)
		self._gain2_text_box.set_value(self.gain2)
		self.mult2.set_k((self.gain2, ))

	def get_gain1(self):
		return self.gain1

	def set_gain1(self, gain1):
		self.gain1 = gain1
		self._gain1_slider.set_value(self.gain1)
		self._gain1_text_box.set_value(self.gain1)
		self.mult1.set_k((self.gain1, ))

	def get_freq4(self):
		return self.freq4

	def set_freq4(self, freq4):
		self.freq4 = freq4
		self._freq4_slider.set_value(self.freq4)
		self._freq4_text_box.set_value(self.freq4)
		self.signal4.set_frequency(self.freq4)

	def get_freq3(self):
		return self.freq3

	def set_freq3(self, freq3):
		self.freq3 = freq3
		self._freq3_slider.set_value(self.freq3)
		self._freq3_text_box.set_value(self.freq3)
		self.signal3.set_frequency(self.freq3)

	def get_freq2(self):
		return self.freq2

	def set_freq2(self, freq2):
		self.freq2 = freq2
		self._freq2_slider.set_value(self.freq2)
		self._freq2_text_box.set_value(self.freq2)
		self.signal2.set_frequency(self.freq2)

	def get_freq1(self):
		return self.freq1

	def set_freq1(self, freq1):
		self.freq1 = freq1
		self._freq1_slider.set_value(self.freq1)
		self._freq1_text_box.set_value(self.freq1)
		self.signal1.set_frequency(self.freq1)

	def get_form4(self):
		return self.form4

	def set_form4(self, form4):
		self.form4 = form4
		self._form4_chooser.set_value(self.form4)
		self.signal4.set_waveform(self.form4)

	def get_form3(self):
		return self.form3

	def set_form3(self, form3):
		self.form3 = form3
		self._form3_chooser.set_value(self.form3)
		self.signal3.set_waveform(self.form3)

	def get_form2(self):
		return self.form2

	def set_form2(self, form2):
		self.form2 = form2
		self._form2_chooser.set_value(self.form2)
		self.signal2.set_waveform(self.form2)

	def get_form1(self):
		return self.form1

	def set_form1(self, form1):
		self.form1 = form1
		self._form1_chooser.set_value(self.form1)
		self.signal1.set_waveform(self.form1)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = siggen()
	tb.Run(True)

