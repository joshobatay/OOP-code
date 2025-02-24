import pyfirmata

comport = 'COM5'  # Change if needed
board = pyfirmata.Arduino(comport)

# Define LED pins
led_pins = [8, 9, 10, 11, 12]  # Thumb to Pinky
leds = [board.get_pin(f'd:{pin}:o') for pin in led_pins]

def led(fingerUp):
    """Controls LEDs based on finger states"""
    for i in range(5):
        leds[i].write(fingerUp[i])  # Turn LED ON/OFF based on finger state
