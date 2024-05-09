from time import sleep
import RPi.GPIO as GPIO


class PIR:
    GPIO.setmode(GPIO.BCM)
    gpio_pin = None
    action = None
    action_args = None
    time_lapse = None
    stop = False

    def __init__(self, gpio_pin, time_lapse, action, action_args=None):
        GPIO.setup(gpio_pin, GPIO.IN)
        self.gpio_pin = gpio_pin
        self.action = action
        self.action_args = action_args
        self.time_lapse = time_lapse

    def __pir_process__(self, stop=False):
        while not self.stop:
            if GPIO.input(self.gpio_pin):
                if self.action_args:
                    if isinstance(self.action_args, tuple):
                        self.action(*self.action_args)
                    else:
                        self.action(self.action_args)
                else:
                    self.action()

                if stop:
                    self.stop_process()
                else:
                    sleep(self.time_lapse)

    def start(self):
        self.stop = True
        self.__pir_process__(False)

    def stop_process(self):
        self.stop = True

    def one_action(self):
        self.__pir_process__(True)
