import numpy as np


class LuciPreset(object):

    hz = None
    brightness = None
    brightness_colors = None
    darkness = None
    darkness_colors = None
    phase_shift = None
    duty_cycle = None

    def __init__(self, hz=15, brightness=255, brightness_colors=-np.ones(4), darkness=0, darkness_colors=-np.ones(4), phase_shift=0, duty_cycle=50):
        self.hz = hz
        self.brightness = brightness
        self.brightness_colors = brightness_colors
        self.darkness = darkness
        self.darkness_colors = darkness_colors
        self.phase_shift = phase_shift
        self.duty_cycle = duty_cycle

    def apply(self, arduino):
        #
        arduino.write('H%d\n' % self.hz)
        print arduino.readline()
        #
        if self.brightness >= 0:
            arduino.write(b'B%d\n' % self.brightness)
        else:
            arduino.write(b'C%d,%d,%d,%d\n' % (self.brightness_color[0], self.brightness_color[1], self.brightness_color[2], self.brightness_color[3]))
        print arduino.readline()
        #
        arduino.write('b%d\n' % self.darkness)
        print arduino.readline()
        #
        arduino.write('D%d\n' % self.duty_cycle)
        print arduino.readline()
        #
        arduino.write(b'X%d\n' % self.phase_shift)
        print arduino.readline()


presets = []
presets.append(LuciPreset(hz=12))
presets.append(LuciPreset(hz=14))
presets.append(LuciPreset(hz=16))
presets.append(LuciPreset(hz=18))
presets.append(LuciPreset(hz=12, phase_shift=1))
presets.append(LuciPreset(hz=14, phase_shift=1))
presets.append(LuciPreset(hz=16, phase_shift=1))
presets.append(LuciPreset(hz=18, phase_shift=1))
