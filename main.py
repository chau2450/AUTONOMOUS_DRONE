import time
import automationhat

# Initialize the Automation HAT
automationhat.enable_auto_lights(True)
automationhat.light.power.write(1)

# Turn on Relay 1 for 5 seconds, then turn it off
automationhat.relay.one.write(1)
time.sleep(5)
automationhat.relay.one.write(0)

# Turn on Relay 2 for 5 seconds, then turn it off
automationhat.relay.two.write(1)
time.sleep(5)
automationhat.relay.two.write(0)

# Turn on Relay 3 for 5 seconds, then turn it off
automationhat.relay.three.write(1)
time.sleep(5)
automationhat.relay.three.write(0)

# Clean up and turn off the power light
automationhat.light.power.write(0)
