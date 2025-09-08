import gpiozero

button = Button(18)

button.wait_for_press()

print("Button was pressed.")