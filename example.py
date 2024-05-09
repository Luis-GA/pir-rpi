from rpi_pir import PIR


# Action to perform when the PIR detects something
def dummy_function(name):
    print("I have detected {}".format(name))


# Arguments for the action
args = ("Juan",)

# Instantiate the class
sensor = PIR(gpio_pin=23, time_lapse=1, action=dummy_function, action_args=args)

# Monitoring for just one action
sensor.one_action()
# Continuous monitoring
# sensor.start()
# Stop continuous monitoring
# sensor.stop()
