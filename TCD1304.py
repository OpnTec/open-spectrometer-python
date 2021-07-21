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

_OSCILLATOR_FREQUENCY = 128e6
_MICROSECONDS = 1e6


class TCD1304:
    """The TCD1304 is a linear CCD suitable for visible spectrum analysis."""

    _INTEGRATION_ELEMENTS = 3694
    _MIN_VOLTAGE_OUTPUT = 2
    _MAX_VOLTAGE_OUTPUT = 4
    _SAMPLES_PER_ELEMENT = 2

    def __init__(
        self,
        device: SerialHandler = None,
        integration_time: float = 10e-6,
        master_clock_frequency: float = 2e6,
    ):
        self._device = SerialHandler() if device is None else device
        self._pwmgen = PWMGenerator(self._device)
        self._scope = Oscilloscope(self._device)
        self._ps = PowerSupply(self._device)
        self.integration_time = integration_time
        self.master_clock_frequency = master_clock_frequency

        self.poweron()
        self._pwmgen.set_state(sq3=True)
        self._start_master_clock()
        self._start_sh_clock()

    def poweron(self):
        """Turn TCD1304 on."""
        self._ps.pv1 = 5

    def poweroff(self):
        """Turn TCD1304 off."""
        self._ps.pv1 = 0

    def _start_icg_clock(self):
        read_out_time = self._INTEGRATION_ELEMENTS * self.integration_time
        self._pwmgen.set_state(sq3=False)
        self._pwmgen.set_state(sq3=True)
        time.sleep(read_out_time)
        self._pwmgen.set_state(sq3=False)
        self._pwmgen.set_state(sq3=True)

    def _start_master_clock(self):
        prescaler = int(
            math.log(_OSCILLATOR_FREQUENCY / self.master_clock_frequency) / math.log(2)
        )
        self._pwmgen.map_reference_clock(["SQ1"], prescaler)

    def _start_sh_clock(self):
        self._pwmgen.generate(["SQ2"], 1 / self.integration_time, [0.5])

    def read_signal(self):
        """Start the ICG clock and read the analog output from the TCD1304."""
        self._scope.select_range("CH1", self._MAX_VOLTAGE_OUTPUT)
        self._scope.configure_trigger(channel="CH1", voltage=self._MIN_VOLTAGE_OUTPUT)
        self._scope.capture(
            channels=1,
            samples=self._INTEGRATION_ELEMENTS * self._SAMPLES_PER_ELEMENT,
            timegap=self.integration_time / self._SAMPLES_PER_ELEMENT * _MICROSECONDS,
            block=False,
        )
        self._start_icg_clock()
        (y,) = self._scope.fetch_data()
        return y
