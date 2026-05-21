import keyboard

print("Keyboard Checker - Press ESC to quit")

while True:
    # Wait for a key event
    event = keyboard.read_event()
    
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key pressed: {event.name}")
    
    # Exit if ESC is pressed
    if event.name == "esc":
        print("Exiting Keyboard Checker...")
        break
