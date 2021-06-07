"""
Requests for the Code:
the code should have an power Output on the Voltagesource VDD=5V /VAD=5V
the code should build a Masterclock with a frequency inbetween 0.8 to 4 MHz, typical 2 MHz. The Voltagerange of the Clock 
shall be 0-4V
The Sensor will be run in the Shutter Mode, so the SH-Clock and the ICG-Clock must be working as following:
The SH is a squarewave with a high level of typical 4V and indicates the integration_time, due to the oscilloscope in the triggermode the integration must be at least 1µs.
Tha Datasheet says, that the integrationtime in shuttermode must be at least 10µs.
The ICG is a squarewave that indicates the 'read out time' of the sample, so it has to be 3694*integration_time*samples_per_element
The integrationtime is started with the falling flank of the SH and and lasts till the next falling flank.
The analog input of the sensor shall be read by the the osilloscope.
The analog voltage signal shall be saved over the time and be integrated to get a digital signal.
the algotithims still needs to be definded.

"""

import numpy as np
import time
import math
from pslab.instrument.waveform_generator import PWMGenerator
from pslab.instrument.oscilloscope import Oscilloscope
from pslab.serial_handler import SerialHandler
from pslab.instrument.logic_analyzer import LogicAnalyzer
from pslab.instrument.power_supply import PowerSupply

frequency_master_clock = 2e6 # no need to specify the variable type (float). frequency_master_clock = float(2e6) turns into frequency_master_clock = 2e6. Same for integration_time variable. Im Datentyp float werden reele Zahlen in Exponentialdarstellung geschrieben (also Gleitkommazahlen). float(2e6) turns 2e6 which is already a float into a float. In other words, it does nothing; However f.e. 280,7 would have also been linked to float instead of int
integration_elements = 3694 # according to timing requests
integration_time =  10e-6   #  time in seconds
oscillator_frequency = 128e6 #frequency of the oscilliator in Mhz
microseconds_in_second = 1e6
min_voltage_output = 2.0 # defines the minimum voltage output of the sensor. The oscilloscope gets enabled by the trigger over that Voltage. range must be verified
max_voltage_output = 4.0 # maximum voltage output of the sensor. must be verified
samples_per_element = 2
read_out_time = integration_time*integration_elements

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
        self.scope = Oscilloscope ()
        
        
    def power_source ():        # puts a voltage of 4V on PV1
        ps = PowerSupply()
        ps.pv1 = 4
        ps.pv1
    
    def analog_signal_read (self, block:False):
        self.scope = Oscilloscope()
        self.scope.select_range('CH1', max_voltage_output)   # voltagerange should be fitted to the sensors output for better resolution. sensor otput is between 2V-3V due to datasheet
        self.scope.configure_trigger(channel = 'CH1', voltage = min_voltage_output ) # starts recording , when voltage is over a certain level
        self.scope.capture(channels=1, samples=integration_elements*samples_per_element, timegap=integration_time/samples_per_element)
        y1, y2 = self.scope.fetch_data()
        diff = abs(y1,y2[1, 0] - min_voltage_output )
        analog_measurement = np.ndarray ()
        return analog_measurement  # this should put the Measurements and timestamps in an array
    
    
    def master_clock (self):        # puts PWM with frequency of 2MHz on SQ1; masterclock is the fastest clock
       prescaler = int(math.log(oscillator_frequency / frequency_master_clock) / math.log(2))   # When setting a frequency by mapping the reference clock directly to a PWM output, only frequencies which are even factors of 128 MHz (the frequency of the PSLab's main oscillator) are available. The frequency is therefore not set by specifying the frequency itself, but by setting a prescaler.
       self.pwmgen.map_reference_clock(["SQ1"], prescaler)    
    
    def sh_clock (self):           #  on SQ2 sets pulse for the integrationtime. Running the Sensor in shutter mode try with tint (min) = 10µs
        self.pwmgen.generate(["SQ2"], 1/integration_time, [0.5] ) 


    def icg_clock (self):           #  on SQ3 starts and stops the reading of the sensor; this third clock is the slowest clock
        self.pwmgen.set_state()
        for pulse in range(integration_elements):
            self.pwmgen.set_state(sq3=True)
            time.sleep(read_out_time / 2)
            self.pwmgen.set_state(sq3=False)
            time.sleep(read_out_time / 2)
        
    
   