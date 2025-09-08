
# --- Imports ---

import RPi.GPIO as GPIO # Imports the RPi.GPIO library which allows control of the GPIO pins on a Raspberry Pi
import time
from RPLCD.i2c import CharLCD
import pygame

# --- Setup ---

GPIO.setmode(GPIO.BOARD) # Sets the pin numbering scheme to BOARD mode

# --- Definitions ---

led_pins = [7, 13,
            15, 18,
            29, 32,
            33, 37,
            22] # Define a list of GPIO pins connected to the LEDs

button_pins = [40, 16, 31, 36] # Define a list of GPIO pins connected to the buttons

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

    test_sound = None

    try: # Try to:
        pygame.mixer.init() # Initialize the audio mixer
        pygame.mixer.set_volume(1.0)
        test_sound = pygame.mixer.Sound("assets/sounds/test_sound2.wav") # Load the sound file for the test sound
        test_sound.play() # Play the test sound
        print("Speaker test suceeded!") # Print a success message

    except Exception as e: # If that doesn't work
        print(f"Speaker test failed: {e}") # Print an error message

def test_display():

    """
    Tests the LCD display by showing a test message.

    Arguments:
        None

    Returns:
        None

    """

    print("Testing display...") # Print a message indicating that the display is being tested

    try: # Try to:
        lcd = CharLCD(i2c_expander = 'PCF8574', address = 0x27, port = 1,
                    cols = 16, rows = 1, dotsize = 8) # Initialize the LCD display with the specified parameters
        
        lcd.clear() # Clear the display

        lcd.write_string("DISPLAY TEST") # Write a test message to the display

    except Exception as e: # If that doesn't work
        print(f"Display not found or could not be initialized: {e}") # Print an error message
        lcd = None # Set lcd to None

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

        for pin in led_pins: # For each pin in the list
            GPIO.setup(pin, GPIO.OUT) # Set the pin as an output
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


    for pin in button_pins:

        GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
            
        print(f"Press the button connected to physical pin {pin}...")

        GPIO.wait_for_edge(pin, GPIO.RISING) # Wait for the button to be pressed

        print(f"Button on pin {pin} pressed") # Print a message indicating that the button was pressed


if __name__ == "__main__":
    test_speaker()
    test_display()
    test_leds()
    test_buttons()
    GPIO.cleanup() # Clean up the GPIO settings