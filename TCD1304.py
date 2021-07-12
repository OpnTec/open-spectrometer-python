"""TCD1304 linear CCD driver for Open Spectrometer.

The sensor shall be connected to the PSLab as following:
Pin 1 of the sensorboard: master_clock --> SQ1 on PSLab
Pin 2: sh_clock --> SQ2
Pin 3: icg_clock --> SQ3
Pin 4: +5V --> PV1
Pin 5: GND --> GND
Pin 6: OS --> CH1
"""

import math
import time

from pslab.serial_handler import SerialHandler
from pslab.instrument.oscilloscope import Oscilloscope
from pslab.instrument.power_supply import PowerSupply
from pslab.instrument.waveform_generator import PWMGenerator

_FREQUENCY_MASTER_CLOCK = 2e6
_INTEGRATION_ELEMENTS = 3694
_INTEGRATION_TIME = 10e-6
_OSCILLATOR_FREQUENCY = 128e6
_MICROSECONDS = 1e6
_MIN_VOLTAGE_OUTPUT = 2.0
_MAX_VOLTAGE_OUTPUT = 4.0
_SAMPLES_PER_ELEMENT = 2
_READ_OUT_TIME = _INTEGRATION_TIME * _INTEGRATION_ELEMENTS


class TCD1304:
    """The TCD1304 is a linear CCD suitable for visible spectrum analysis."""

    def __init__(self, device: SerialHandler = None):
        self._device = SerialHandler() if device is None else device
        self._pwmgen = PWMGenerator(self._device)
        self._scope = Oscilloscope(self._device)
        self._ps = PowerSupply(self._device)
        self.poweron()
        self._start_master_clock()
        self._start_sh_clock()

    def poweron(self):
        """Turn TCD1304 on."""
        self._ps.pv1 = 5

    def poweroff(self):
        """Turn TCD1304 off."""
        self._ps.pv1 = 0

    def _start_icg_clock(self):
        self._pwmgen.set_state(sq3=True)
        time.sleep(_READ_OUT_TIME)
        self._pwmgen.set_state(sq3=False)

    def _start_master_clock(self):
        prescaler = int(
            math.log(_OSCILLATOR_FREQUENCY / _FREQUENCY_MASTER_CLOCK) / math.log(2)
        )
        self._pwmgen.map_reference_clock(["SQ1"], prescaler)

    def _start_sh_clock(self):
        self._pwmgen.generate(["SQ2"], 1 / _INTEGRATION_TIME, [0.5])

    def read_signal(self):
        """Start the ICG clock and read the analog output from the TCD1304."""
        self._scope.select_range("CH1", _MAX_VOLTAGE_OUTPUT)
        self._scope.configure_trigger(channel="CH1", voltage=_MIN_VOLTAGE_OUTPUT)
        self._scope.capture(
            channels=1,
            samples=_INTEGRATION_ELEMENTS * _SAMPLES_PER_ELEMENT,
            timegap=_INTEGRATION_TIME / _SAMPLES_PER_ELEMENT * _MICROSECONDS,
            block=False,
        )
        self._start_icg_clock()
        (y,) = self._scope.fetch_data()
        return y
