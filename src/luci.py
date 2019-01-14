import numpy as np
import serial


class Luci(object):

    def __init__(self, dev='/dev/ttyACM0'):
        self._arduino = serial.Serial(dev, 9600, timeout=5)

    def _arduino_write(self, string):
        self._arduino.write(string)
        self._arduino.flushInput()
        self._arduino.flushOutput()

    def set_frequency(self, hz=15):
        hz = np.clip(hz, 1, 100)
        self._arduino_write('H%d\n' % hz)
        return self._arduino.readline()

    def set_brightness(self, b):
        b = np.clip(b, 0, 255)
        self._arduino_write(b'B%d\n' % b)
        return self._arduino.readline()

    def set_darkness(self, d=0):
        d = np.clip(d, 0, 255)
        self._arduino_write('b%d\n' % d)
        return self._arduino.readline()

    def set_duty_cycle(self, dc=50):
        dc = np.clip(dc, 1, 99)
        self._arduino_write('D%d\n' % dc)
        return self._arduino.readline()

    def set_brightness_color(self, rgbw=np.array([255,255,255,255])):
        rgbw = np.clip(rgbw, 0, 255)
        self._arduino_write(b'C%d,%d,%d,%d\n' % (rgbw[0], rgbw[1], rgbw[2], rgbw[3]))
        return self._arduino.readline()

    def set_phase_shift(self, s=0):
        s = np.clip(s, 0, 1)
        self._arduino_write(b'X%d\n' % s)
        return self._arduino.readline()


def main():
    luci = Luci(dev='/dev/ttyACM0')
    print luci.set_brightness(5)
    print luci.set_frequency(2)


if __name__ == '__main__':
    main()
