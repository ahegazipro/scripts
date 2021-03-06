import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block Envelope Detector """

    def __init__(self, threshold=0.0, mode=0, coeff=0.15):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Envelope Detector',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

        self.ry = 0
        self.threshold = threshold
        self.mode = mode
        self.coeff = coeff

    def work(self, input_items, output_items):
        """Envelope Detect with Half/Full Wave Rectifier"""
        buf = [0] * len(output_items[0])
        a0 = self.coeff
        b1 = 1 - a0
        # Rectify the signal. Mode 0 is half-wave, Mode 1 is full-wave
        for i in range (0, len(input_items[0])) :
            if self.mode == 1:
                buf[i] = abs(input_items[0][i])
            else:
                if input_items[0][i] > self.threshold:
                    buf[i] = input_items[0][i]
                else:
                    buf[i] = 0
        # Simulate simple RC filter with a variable decay coefficient
        for i in range(0, len(output_items[0])):
            if i==0:
                output_items[0][i] = a0*buf[i] + b1*self.ry
            else:
                output_items[0][i] = a0*buf[i] + b1*output_items[0][i-1]

        i = len(output_items[0])-1
        self.ry = output_items[0][i]

        return len(output_items[0])
