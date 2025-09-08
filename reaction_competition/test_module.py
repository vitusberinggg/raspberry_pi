
# --- Imports ---

import RPi.GPIO as GPIO # Imports the RPi.GPIO library which allows control of the GPIO pins on a Raspberry Pi
import time
from RPLCD.i2c import CharLCD
from pygame import mixer # Imports the mixer module from the pygame library for audio playback

# --- Setup ---

GPIO.setmode(GPIO.BOARD) # Sets the pin numbering scheme to BOARD mode
GPIO.setwarnings(False) # Disables the warnings that the "RPi.GPIO" library might generate

# --- Definitions ---

led_pins = [7, 13,
            15, 18,
            29, 32,
            33, 37,
            22] # Define a list of GPIO pins connected to the LEDs

button_pins = [12, 16, 31, 36] # Define a list of GPIO pins connected to the buttons

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
        mixer.init() # Initialize the audio mixer
        test_sound = mixer.Sound("assets/sounds/test_sound2.wav") # Load the sound file for the test sound
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

    try:
        for pin in button_pins:

            GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
            
            print(f"Press the button connected to physical pin {pin}...")
            
            edge = GPIO.wait_for_edge(pin, GPIO.RISING, timeout = 20000)

            if edge is None:
                print(f"TIMEOUT: No button press detected on physical pin {pin}.")
                return # Stop the test if one button fails
            
            else:
                print(f"SUCCESS: Button on physical pin {pin} was pressed!")
            
            time.sleep(0.5)

        print("\n--- Button test completed successfully! ---")

    except Exception as e:
        print(f"An error occurred during the test: {e}")

if __name__ == "__main__":
    test_speaker()
    test_display()
    test_leds()
    test_buttons()
    GPIO.cleanup() # Clean up the GPIO settings