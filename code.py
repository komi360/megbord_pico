import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import board
import digitalio
from board import *

btn1_pin = board.GP10
btn2_pin = board.GP11
btn3_pin = board.GP12
btn4_pin = board.GP13

cc = ConsumerControl(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(GP25)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)
        led.value = False
        time.sleep(0.1)
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.E)
        led.value = False
        time.sleep(0.1)
    if btn3.value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        led.value = False
        time.sleep(0.1)
    if btn4.value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        led.value = False
        time.sleep(0.1)
    time.sleep(0.1)
