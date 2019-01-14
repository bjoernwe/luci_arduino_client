import getkey
import numpy as np
import serial
import sys
import time

import luci_presets


def main():

    hz = 10
    brightness = 5
    brightness_color = np.array([-1, -1, -1, -1])
    darkness = 0
    darkness_color = np.array([-1, -1, -1, -1])
    duty_cycle = 50
    phase_shift = 1

    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

    try:
        while True:

            key = getkey.getkey(blocking=True)

            #
            # Frequency(Hz) UP
            #
            if key == getkey.keys.UP:

                if hz < 100:
                    hz = hz + 1
                arduino.write('H%d\n' % hz)
                print arduino.readline()

            #
            # Frequency(Hz) DOWN
            #
            elif key == getkey.keys.DOWN:

                if hz > 1:
                    hz = hz - 1
                arduino.write('H%d\n' % hz)
                print arduino.readline()

            #
            #
            #
            elif key == getkey.keys.LEFT:
                print 'LEFT'

            #
            #
            #
            elif key == getkey.keys.RIGHT:
                print 'RIGHT'

            #
            # Brightness UP
            #
            elif key == getkey.keys.PAGE_UP:

                if brightness >= 0:
                    brightness *= 2
                    brightness = min(brightness, 255)
                    arduino.write(b'B%d\n' % brightness)
                else:
                    brightness_color *= 2
                    brightness_color = np.clip(brightness_color, -1, 255)
                    arduino.write(b'C%d,%d,%d,%d\n' % (brightness_color[0], brightness_color[1], brightness_color[2], brightness_color[3]))

                print arduino.readline()

            #
            #
            #
            elif key == getkey.keys.PAGE_DOWN:

                if brightness >= 0:
                    brightness //= 2
                    brightness = max(brightness, 1)
                    arduino.write(b'B%d\n' % brightness)
                else:
                    brightness_color //= 2
                    brightness_color[:3] = np.clip(brightness_color[:3], -1, 0)
                    brightness_color[3] = np.clip(brightness_color[3], 1, 255)
                    arduino.write(b'C%d,%d,%d,%d\n' % (brightness_color[0], brightness_color[1], brightness_color[2], brightness_color[3]))

                print arduino.readline()

            #
            #
            #
            elif key == getkey.keys.SPACE:
                if darkness < .75 * brightness:
                    while darkness < .75 * brightness:
                        darkness += 2
                        arduino.write('b%d\n' % darkness)
                        print arduino.readline()
                        time.sleep(0.1)
                else:
                    darkness = 0
                    arduino.write('b%d\n' % darkness)
                    print arduino.readline()

            #
            #
            #
            elif key == getkey.keys.ENTER:
                pass

            #
            #
            #
            elif key == getkey.keys.PLUS:
                if duty_cycle < 100:
                    duty_cycle += 1
                arduino.write('D%d\n' % duty_cycle)
                print arduino.readline()

            #
            #
            #
            elif key == getkey.keys.MINUS:
                if duty_cycle > 1:
                    duty_cycle -= 1
                arduino.write('D%d\n' % duty_cycle)
                print arduino.readline()

            #
            # Toggle RGB (ignoring white)
            #
            elif key == getkey.keys.W:

                if brightness >= 0:
                    brightness_color = [0, 0, 0, brightness]
                    brightness = -1
                    arduino.write(b'C%d,%d,%d,%d\n' % (
                    brightness_color[0], brightness_color[1], brightness_color[2], brightness_color[3]))
                else:
                    brightness = brightness_color[3]
                    brightness_color = [-1, -1, -1, -1]
                    arduino.write(b'B%d\n' % brightness)

                print arduino.readline()

            #
            # Toggle Phase Shift
            #
            elif key == getkey.keys.X:
                phase_shift = 1 - phase_shift
                arduino.write(b'X%d\n' % phase_shift)
                print arduino.readline()

            #
            #
            #
            elif key == getkey.keys.DIGIT_ONE:
                luci_presets.presets[0].apply(arduino)
            elif key == getkey.keys.DIGIT_TWO:
                luci_presets.presets[1].apply(arduino)
            elif key == getkey.keys.DIGIT_THREE:
                luci_presets.presets[2].apply(arduino)
            elif key == getkey.keys.DIGIT_FOUR:
                luci_presets.presets[3].apply(arduino)
            elif key == getkey.keys.DIGIT_FIVE:
                luci_presets.presets[4].apply(arduino)
            elif key == getkey.keys.DIGIT_SIX:
                luci_presets.presets[5].apply(arduino)
            elif key == getkey.keys.DIGIT_SEVEN:
                luci_presets.presets[6].apply(arduino)
            elif key == getkey.keys.DIGIT_EIGHT:
                luci_presets.presets[7].apply(arduino)

            else:
                print key
            #time.sleep(0.01)
            arduino.flushInput()
            arduino.flushOutput()


    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
