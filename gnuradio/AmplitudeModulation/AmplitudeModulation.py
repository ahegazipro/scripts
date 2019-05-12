#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Amplitude Modulation DSBSC_DSBTC
# Author: Ahmad Hegazy <ahegazy.github.io>
# Description: Simulation of AM, Coherent and Non Coherent Detection
# Generated: Sun May 12 13:30:43 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import EnvelopeDetector
import wx


class AmplitudeModulation(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Amplitude Modulation DSBSC_DSBTC")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.carrierFreq = carrierFreq = 20050
        self.vol = vol = 0.1
        self.source = source = 0
        self.samp_rate = samp_rate = 44100
        self.play = play = 1
        self.noise = noise = 0
        self.msgfreq = msgfreq = 1000
        self.lvl = lvl = 0.1
        self.carr_samprate = carr_samprate = carrierFreq*2+10000
        self.A = A = 0

        ##################################################
        # Blocks
        ##################################################
        _vol_sizer = wx.BoxSizer(wx.VERTICAL)
        self._vol_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_vol_sizer,
        	value=self.vol,
        	callback=self.set_vol,
        	label='Demod Amp',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._vol_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_vol_sizer,
        	value=self.vol,
        	callback=self.set_vol,
        	minimum=0,
        	maximum=10,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_vol_sizer, 1, 10, 1, 10)
        self.tabs = self.tabs = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.tabs.AddPage(grc_wxgui.Panel(self.tabs), "Message_Carrier_Mod Time")
        self.tabs.AddPage(grc_wxgui.Panel(self.tabs), "Modulated FFT")
        self.tabs.AddPage(grc_wxgui.Panel(self.tabs), "Demodulated Time ")
        self.tabs.AddPage(grc_wxgui.Panel(self.tabs), "Demodulated FFT ")
        self.Add(self.tabs)
        self._source_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.source,
        	callback=self.set_source,
        	label='Source',
        	choices=[0, 1],
        	labels=['Tone', 'Music'],
        	style=wx.RA_HORIZONTAL,
        )
        self.GridAdd(self._source_chooser, 0, 30, 1, 10)
        self._play_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.play,
        	callback=self.set_play,
        	label='Play source',
        	choices=[0, 1,2],
        	labels=['Origianl audio', 'Coherent Det.', 'Non-Coh.'],
        	style=wx.RA_VERTICAL,
        )
        self.GridAdd(self._play_chooser, 0, 40, 3, 10)
        _noise_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	label='Noise Amp',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	minimum=0,
        	maximum=1,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_noise_sizer, 1, 20, 1, 10)
        _msgfreq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._msgfreq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_msgfreq_sizer,
        	value=self.msgfreq,
        	callback=self.set_msgfreq,
        	label='Message Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._msgfreq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_msgfreq_sizer,
        	value=self.msgfreq,
        	callback=self.set_msgfreq,
        	minimum=0,
        	maximum=10000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_msgfreq_sizer, 0, 0, 1, 10)
        _lvl_sizer = wx.BoxSizer(wx.VERTICAL)
        self._lvl_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_lvl_sizer,
        	value=self.lvl,
        	callback=self.set_lvl,
        	label='Msg Amp',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._lvl_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_lvl_sizer,
        	value=self.lvl,
        	callback=self.set_lvl,
        	minimum=0,
        	maximum=10,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_lvl_sizer, 1, 0, 1, 10)
        _carrierFreq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._carrierFreq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_carrierFreq_sizer,
        	value=self.carrierFreq,
        	callback=self.set_carrierFreq,
        	label='Carrier Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._carrierFreq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_carrierFreq_sizer,
        	value=self.carrierFreq,
        	callback=self.set_carrierFreq,
        	minimum=20050,
        	maximum=100000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_carrierFreq_sizer, 0, 10, 1, 10)
        _A_sizer = wx.BoxSizer(wx.VERTICAL)
        self._A_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_A_sizer,
        	value=self.A,
        	callback=self.set_A,
        	label='Constat A',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._A_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_A_sizer,
        	value=self.A,
        	callback=self.set_A,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_A_sizer, 0, 20, 1, 10)
        self.wxgui_scopesink2_1_0 = scopesink2.scope_sink_f(
        	self.tabs.GetPage(2).GetWin(),
        	title='Non Coherent Detection TIME Dem',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Amplitude',
        )
        self.tabs.GetPage(2).Add(self.wxgui_scopesink2_1_0.win)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
        	self.tabs.GetPage(2).GetWin(),
        	title='Coherent Detection TIME Dem',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Amplitude',
        )
        self.tabs.GetPage(2).Add(self.wxgui_scopesink2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.tabs.GetPage(0).GetWin(),
        	title='Message_Carrier_Modulated',
        	sample_rate=carr_samprate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=3,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Amplitude',
        )
        self.tabs.GetPage(0).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_f(
        	self.tabs.GetPage(3).GetWin(),
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
        	title='Non Coherent FFT Plot',
        	peak_hold=False,
        	win=window.flattop,
        )
        self.tabs.GetPage(3).Add(self.wxgui_fftsink2_0_0_0.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_f(
        	self.tabs.GetPage(3).GetWin(),
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
        	title='Coherent FFT Plot',
        	peak_hold=False,
        	win=window.flattop,
        )
        self.tabs.GetPage(3).Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.tabs.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=carr_samprate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Modulated FFT Plot',
        	peak_hold=False,
        )
        self.tabs.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, msgfreq, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, msgfreq, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.dc_blocker_xx_0_0 = filter.dc_blocker_ff(32, True)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(32, True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/ahmad/Downloads/Yamaha-V50-Rock-Beat-120bpm.wav', True)
        self.blocks_throttle_0_2_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_2 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_float*1, carr_samprate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, carr_samprate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, carr_samprate,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_vff((vol, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((vol, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((lvl*5, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((A, ))
        self.blks2_selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=play,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=source,
        	output_index=0,
        )
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, carr_samprate, carrierFreq-2*msgfreq, carrierFreq+2*msgfreq, 500, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0_0_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, carrierFreq, 1, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, carrierFreq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, msgfreq, lvl, 0)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_f(analog.GR_GAUSSIAN, noise, 0, 8192)
        self.EnvelopeDetector = EnvelopeDetector.blk(threshold=0.0, mode=1, coeff=0.15)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.EnvelopeDetector, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blks2_selector_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.band_pass_filter_0, 0), (self.EnvelopeDetector, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.blks2_selector_0, 0), (self.blks2_selector_1, 0))    
        self.connect((self.blks2_selector_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blks2_selector_1, 0), (self.rational_resampler_xxx_0_0_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_throttle_0_1, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blks2_selector_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blks2_selector_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_throttle_0_2, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.blks2_selector_1, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.blocks_throttle_0_2_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0, 2))    
        self.connect((self.blocks_throttle_0_0, 0), (self.wxgui_scopesink2_0, 1))    
        self.connect((self.blocks_throttle_0_1, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_throttle_0_2, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.blocks_throttle_0_2, 0), (self.wxgui_scopesink2_1, 0))    
        self.connect((self.blocks_throttle_0_2_0, 0), (self.wxgui_fftsink2_0_0_0, 0))    
        self.connect((self.blocks_throttle_0_2_0, 0), (self.wxgui_scopesink2_1_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))    
        self.connect((self.dc_blocker_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.dc_blocker_xx_0_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.dc_blocker_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.audio_sink_0_0_0, 0))    

    def get_carrierFreq(self):
        return self.carrierFreq

    def set_carrierFreq(self, carrierFreq):
        self.carrierFreq = carrierFreq
        self._carrierFreq_slider.set_value(self.carrierFreq)
        self._carrierFreq_text_box.set_value(self.carrierFreq)
        self.set_carr_samprate(self.carrierFreq*2+10000)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.carr_samprate, self.carrierFreq-2*self.msgfreq, self.carrierFreq+2*self.msgfreq, 500, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1_0.set_frequency(self.carrierFreq)
        self.analog_sig_source_x_1.set_frequency(self.carrierFreq)

    def get_vol(self):
        return self.vol

    def set_vol(self, vol):
        self.vol = vol
        self._vol_slider.set_value(self.vol)
        self._vol_text_box.set_value(self.vol)
        self.blocks_multiply_const_vxx_0_0_1.set_k((self.vol, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.vol, ))

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source
        self._source_chooser.set_value(self.source)
        self.blks2_selector_0.set_input_index(int(self.source))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_1_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.msgfreq, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.msgfreq, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.blocks_throttle_0_2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_2.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_play(self):
        return self.play

    def set_play(self, play):
        self.play = play
        self._play_chooser.set_value(self.play)
        self.blks2_selector_1.set_input_index(int(self.play))

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self._noise_slider.set_value(self.noise)
        self._noise_text_box.set_value(self.noise)
        self.analog_fastnoise_source_x_0.set_amplitude(self.noise)

    def get_msgfreq(self):
        return self.msgfreq

    def set_msgfreq(self, msgfreq):
        self.msgfreq = msgfreq
        self._msgfreq_slider.set_value(self.msgfreq)
        self._msgfreq_text_box.set_value(self.msgfreq)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.msgfreq, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.msgfreq, 10, firdes.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.carr_samprate, self.carrierFreq-2*self.msgfreq, self.carrierFreq+2*self.msgfreq, 500, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_frequency(self.msgfreq)

    def get_lvl(self):
        return self.lvl

    def set_lvl(self, lvl):
        self.lvl = lvl
        self._lvl_slider.set_value(self.lvl)
        self._lvl_text_box.set_value(self.lvl)
        self.blocks_multiply_const_vxx_0.set_k((self.lvl*5, ))
        self.analog_sig_source_x_0.set_amplitude(self.lvl)

    def get_carr_samprate(self):
        return self.carr_samprate

    def set_carr_samprate(self, carr_samprate):
        self.carr_samprate = carr_samprate
        self.wxgui_scopesink2_0.set_sample_rate(self.carr_samprate)
        self.wxgui_fftsink2_0.set_sample_rate(self.carr_samprate)
        self.blocks_throttle_0_1.set_sample_rate(self.carr_samprate)
        self.blocks_throttle_0_0.set_sample_rate(self.carr_samprate)
        self.blocks_throttle_0.set_sample_rate(self.carr_samprate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.carr_samprate, self.carrierFreq-2*self.msgfreq, self.carrierFreq+2*self.msgfreq, 500, firdes.WIN_HAMMING, 6.76))

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self._A_slider.set_value(self.A)
        self._A_text_box.set_value(self.A)
        self.blocks_add_const_vxx_0.set_k((self.A, ))


def main(top_block_cls=AmplitudeModulation, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
