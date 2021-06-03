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

frequency_master_clock = 2e6 # no need to specify the variable type (float). frequency_master_clock = float(2e6) turns into frequency_master_clock = 2e6. Same for integration_time variable. Im Datentyp float werden reele Zahlen in Exponentialdarstellung geschrieben (also Gleitkommazahlen). float(2e6) turns 2e6 which is already a float into a float. In other words, it does nothing; However f.e. 280,7 would have also been linked to float instead of int
integration_time = 1.85e-3 # time in seconds
oscillator_frequency = 128e6 #frequency of the oscilliator in Mhz

class TCD1304():
    def __init__(
        self, #Initializing; self is always first parameter of methods located inside a class and is not limited to the __init__ method but to most methods. A method is a function that belongs to a class
        min_masterclock_frequency = 0.8e6, # no need to specify the variable type (float).  View comment in L37
        max_masterclock_frequency = 4e6, # no need to specify the variable type (float). View comment in L37
        frequency = frequency_master_clock, #default frequency of masterclock 2 MHz; # no need to specify the variable type (float). View comment in L37
        min_voltagerange_clock: float = 0, #it says that min_voltagerange_clock should (!) be a float. Otherwise it would not turn into a float automatically. Output on float will be 0.0 V and on int 0 V.
        max_voltagerange_clock: float = 4,
        pwmgen = ... # not sure if pwmgen needs to be assigned to a value ??
        ): 

        self.min_masterclock_frequency = min_masterclock_frequency #initializing starts from here (? Not sure though)
        self.max_masterclock_frequency = max_masterclock_frequency
        self.frequency = frequency
        self.min_voltagerange_clock = min_voltagerange_clock
        self.max_voltagerange_clock = max_voltagerange_clock
        self.pwmgen = PWMGenerator() #once assigned in __init__ self.pwmgen can be used in other methods
        
    def power_source ():        # puts a voltage of 4V on PV1
        ps = PowerSupply()
        ps.pv1 = 4
        ps.pv1
    
    def master_clock (self):        # puts PWM with frequency of 2MHz on SQ1; masterclock is the fastest clock
        prescaler = int(math.log(oscillator_frequency / frequency_master_clock) / math.log(2))   # When setting a frequency by mapping the reference clock directly to a PWM output, only frequencies which are even factors of 128 MHz (the frequency of the PSLab's main oscillator) are available. The frequency is therefore not set by specifying the frequency itself, but by setting a prescaler.
        self.pwmgen.map_reference_clock(["SQ1"], prescaler)    
    
    def sh_clock (self):           #  on SQ2 sets pulse for the integrationtime
        return self.pwmgen.generate() #is the return attribute the one to choose in order to set a second clock?

        ''' 
        integrationtime is started by the falling flank of voltageoutput. 
        the time for integration must be longer than 3_694 Elements of fmc.
        sh clock is started before icg is started. normal state of sh is a low
        level. high level can be quite short
        '''

    def icg_clock ():           #  on SQ3 starts and stops the reading of the sensor; this third clock is the slowest clock
        '''
        normal state of icg is a high level. Start of the reading is on the rising
        flank of the voltage. To start the reading voltage shall drop to low and rise 
        to high again.
        '''
