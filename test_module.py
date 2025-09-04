
# --- Imports ---

import time
import Rpi.GPIO as GPIO # Imports the RPi.GPIO library which allows control of the GPIO pins on a Raspberry Pi
from luma.core.interface.serial import i2c # 
from luma.oled.device import ssd1306 # 
from luma.core.render import canvas #
from PIL import ImageFont # Imports ImageFont from PIL
from pygame import mixer # Imports the mixer module from the pygame library for audio playback

# --- Setup ---

GPIO.setmode(GPIO.BCM) # Sets the pin numbering scheme to BCM (Broadcom) mode
GPIO.setwarnings(False) # Disables the warnings that the "RPi.GPIO" library might generate

# --- Functions ---

def test_speaker():

    """
    Tests the speaker by playing a test sound.

    Arguments:
        None

    Returns:
        None
    
    """

    print("Testing speaker...") # Print a message indicating that the speaker is being tested

    try: # Try to:
        mixer.init() # Initialize the audio mixer
        test_sound = mixer.Sound("") # Load the sound file for the test sound
        test_sound.play() # Play the test sound
        print("Speaker test suceeded!") # Print a success message

    except Exception as e: # If that doesn't work
        print(f"Speaker test failed: {e}") # Print an error message

def test_display():

    """
    Tests the OLED display by showing a test message.

    Arguments:
        None

    Returns:
        None

    """

    print("Testing display...") # Print a message indicating that the display is being tested

    try: # Try to:
        serial = i2c(port = 1, address = 0x3C) # Create an I2C serial interface
        device = ssd1306(serial) # Create an SSD1306 OLED display device
        display_font = ImageFont.load_default() # Load the default font for the display

        with canvas(device) as draw: # Create a drawing canvas on the device
            draw.text((0, 0), "Testing display...", font = display_font, fill = "white") # Draw the test message on the canvas

        print("Display test succeeded!") # Print a success message

    except Exception as e: # If that doesn't work
        print(f"Display test failed: {e}") # Print an error message

def test_leds():

    """
    Tests the LEDs by turning them on and off in sequence.

    Arguments:
        None

    Returns:
        None
    
    """

    print("Testing LEDs...") # Print a message indicating that the LEDs are being tested

    try: # Try to:
        led_pins = [] # Define a list of GPIO pins connected to the LEDs

        for pin in led_pins: # For each pin in the list
            GPIO.setup(pin, GPIO.OUT) # Set the pin as an output

        for pin in led_pins: # For each pin in the list
            GPIO.output(pin, GPIO.HIGH) # Turn on the LED
            time.sleep(0.5) # Wait for 0.5 seconds
            GPIO.output(pin, GPIO.LOW) # Turn off the LED

        print("LED test succeeded!") # Print a success message

    except Exception as e: # If that doesn't work
        print(f"LED test failed: {e}") # Print an error message

def test_buttons():

    """
    Tests the buttons.

    Arguments:
        None

    Returns:
        None
    
    """

    print("Testing buttons...") # Print a message indicating that the buttons are being tested

    try: # Try to:
        button_pins = [] # Define a list of GPIO pins connected to the buttons

        for pin in button_pins: # For each pin in the list
            GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set the pin as an input with a pull-up resistor

        for pin in button_pins: # For each pin in the list
            print(f"Press button connected to pin {pin}...") # Prompt the user to press the button
            GPIO.wait_for_edge(pin, GPIO.FALLING) # Wait for the button to be pressed
            print(f"Button on pin {pin} pressed") # Print a message indicating that the button was pressed

        print("Button test succeeded!") # Print a success message

    except Exception as e: # If that doesn't work
        print(f"Button test failed: {e}") # Print an error message

if __name__ == "__main__":
    test_speaker()
    test_display()
    test_leds()
    test_buttons()
    GPIO.cleanup() # Clean up the GPIO settings