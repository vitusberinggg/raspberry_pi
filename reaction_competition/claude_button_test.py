
import RPi.GPIO as GPIO
import time
import signal
import sys

# GPIO pin assignments
LED_PIN = 7
BUTTON_PIN = 12

def setup_gpio():
    """Initialize GPIO settings"""
    GPIO.setmode(GPIO.BOARD)  # Use BCM pin numbering
    GPIO.setup(LED_PIN, GPIO.OUT)  # Set LED pin as output
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # Button with pull-up resistor
    GPIO.output(LED_PIN, GPIO.LOW)  # Start with LED off

def cleanup_gpio(signal_num=None, frame=None):
    """Clean up GPIO on exit"""
    print("\nCleaning up GPIO...")
    GPIO.cleanup()
    sys.exit(0)

def main():
    """Main program loop"""
    print("LED Button Control Starting...")
    print("Press the button to light the LED")
    print("Press Ctrl+C to exit")
    
    setup_gpio()
    
    # Register signal handler for clean exit
    signal.signal(signal.SIGINT, cleanup_gpio)
    
    try:
        while True:
            # Read button state (LOW when pressed due to pull-up resistor)
            button_state = GPIO.input(BUTTON_PIN)
            
            if button_state == GPIO.LOW:  # Button is pressed
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
                print("Button pressed - LED ON")
            else:  # Button is not pressed
                GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off
                
            time.sleep(0.1)  # Small delay to prevent excessive CPU usage
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cleanup_gpio()

if __name__ == "__main__":
    main()