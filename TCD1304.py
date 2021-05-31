'''
Requests for the Code:
the code should have an power Output on the Voltagesource VDD=5V /VAD=5V
the code should build a Masterclock with a frequency inbetween 0.8 to 4 MHz, typical 2 MHz. The Voltagerange of the Clock 
shall be 0-4V
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


import time
import math
from pslab.instrument.waveform_generator import PWMGenerator
from pslab.instrument.oscilloscope import Oscilloscope
from pslab.serial_handler import SerialHandler
from pslab.instrument.logic_analyzer import LogicAnalyzer
from pslab.instrument.power_supply import PowerSupply

frequency_master_clock = fmc
fmc = float (2e6)
integration_time = intti
intti = float (1.85e-3) # time in seconds

class tcd1304():
    def __init__(
        self, #steht Standartmäßig bei __init__funktionen an erster Stelle
        min_masterclock_frequency: int = 0.8e6,
        max_masterclock_frequency: int = 4e6,
        frequency: float = 2e6, #Standart Frequenz der Masterclock sind 2 MHz
        min_volatagerange_clock: int = 0,
        max_volatagerange_clock: int = 4,
        ): 

        self.min_masterclock_frequency = min_masterclock_frequency #Hier wird initialisiert, wenn mich nicht alles täsucht
        self.max_masterclock_frequency = max_masterclock_frequency
        self.frequency = frequency
        self.min_volatagerange_clock = min_volatagerange_clock
        self.max_volatagerange_clock = max_volatagerange_clock

    def power_source ():        # puts a voltage of 4V on PV1
        ps = PowerSupply()
        ps.pv1 = 4
        ps.pv1
    
    def master_clock ():        # puts PWM with frequency of 2MHz on SQ1
        pwmgen = PWMGenerator()
        pwmgen.generate(["SQ1"], fmc, [0.5])       
    
    def sh_clock ():            #  on SQ2 sets pulse for the integrationtime
        ''' 
        integrationtime is started by the falling flank of voltageoutput. 
        the time for integration must be longer than 3_694 Elements of fmc.
        sh clock is started before icg is started. normal state of sh is a low
        level. high level can be quite short
        '''

    def icg_clock ():           #  on SQ3 starts and stops the reading of the sensor
        '''
        normal state of icg is a high level. Start of the reading is on the rising
        flank of the voltage. To start the reading voltage shall drop to low and rise 
        to high again.
        '''
