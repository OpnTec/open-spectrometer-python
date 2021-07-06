"""
The Sensor shall be connected to the PSLab as Following:
Pin 1 of the sensorboard: master_clock --> SQ1 on PSLab
Pin 2: sh_clock --> SQ2
Pin 3: icg_clock --> SQ3
Pin 4: +5V --> PV1
Pin 5: GND --> GND
Pin 6: OS --> CH1
"""

import numpy as np
import time
import math
from pslab.instrument.waveform_generator import PWMGenerator
from pslab.instrument.oscilloscope import Oscilloscope
from pslab.serial_handler import SerialHandler
from pslab.instrument.logic_analyzer import LogicAnalyzer
from pslab.instrument.power_supply import PowerSupply

FREQUENCY_MASTER_CLOCK = 2e6
INTEGRATION_ELEMENTS = 3694 
INTEGRATION_TIME =  10e-6 
OSCILLATOR_FREQUENCY = 128e6 
MICROSECONDS = 1e6
MIN_VOLTAGE_OUTPUT = 2.0
MAX_VOLTAGE_OUTPUT = 4.0 
SAMPLES_PER_ELEMENT = 2
READ_OUT_TIME = INTEGRATION_TIME*INTEGRATION_ELEMENTS

class TCD1304:
    def __init__(
        self,  ): 
        self.pwmgen = PWMGenerator()
        self.scope = Oscilloscope ()
        self.ps = PowerSupply()
        
    def set_power_source():
        self.ps.pv1 = 4

    def start_icg_clock(self):
        self.pwmgen.set_state(sq3=True)
        time.sleep(READ_OUT_TIME)
        self.pwmgen.set_state(sq3=False)

    def start_master_clock(self):       
       prescaler = int(math.log(OSCILLATOR_FREQUENCY / FREQUENCY_MASTER_CLOCK) / math.log(2))  
       self.pwmgen.map_reference_clock(["SQ1"], prescaler)    
    
    def start_sh_clock(self):         
        self.pwmgen.generate(["SQ2"], 1/INTEGRATION_TIME, [0.5] ) 

    def read_signal(self):
        self.scope.select_range('CH1', MAX_VOLTAGE_OUTPUT)   
        self.scope.configure_trigger(channel = 'CH1', voltage = MIN_VOLTAGE_OUTPUT ) 
        self.scope.capture(channels=1, samples=INTEGRATION_ELEMENTS*SAMPLES_PER_ELEMENT, timegap=INTEGRATION_TIME/SAMPLES_PER_ELEMENT, block=False)
        self.icg_clock()
        y, = self.scope.fetch_data() 
        return y 

   