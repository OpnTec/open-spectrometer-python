'''
Requests for the Code:
the code should have an power Output on the Voltagesource VDD=5V /VAD=5V
the code should build a Masterclock with a frequency inbetween 0.8 to 4 MHz, typical 2 MHz. The Voltagerange of the Clock shall be 0-4V
The ICG is a squarewave with a high level of typical 4V over the time of 3694 Elements of the Clock.
The SH is a squarewave with a high level of typical 4V and indicates the integrationtime. 
The integrationtime is started with the falling flank of the signal and and lasts till the next falling flank.
The analog input of the sensor shall be read by the the osilloscope.
the analog voltage signal shall be saved over the time and be integrated to get a digital signal.
the algotithims still needs to be definded.

import argparse
import csv
import json
import platform
import os.path
import shutil
import sys
import time
from itertools import zip_longest
from typing import List, Tuple

import numpy as np

'''
'''
HALLO
'''


import time
import math
from pslab.instrument.waveform_generator import PWMGenerator
from pslab.instrument.oscilloscope import Oscilloscope
from pslab.serial_handler import SerialHandler
from pslab.instrument.logic_analyzer import LogicAnalyzer





class tcd1304():
    

    # --------------Parameters--------------------
    # This must be defined in order to let GUIs automatically create menus
    # for changing various options of this sensor
    # It's a dictionary of the string representations of functions matched with an array
    # of options that each one can accept

    




if __name__ == "__main__":
    from PSL import sciencelab

    I = sciencelab.connect()
    O = connect(I.I2C)
    textbgcolor = 0
    textcolor = 1
    O.load('logo')
    O.scroll('topright')
    import time

    time.sleep(2.8)
    O.scroll('stop')
