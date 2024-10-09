
from pynput import keyboard

# Function to be called when a key is pressed
def on_press(key):
    try:
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

# Function to be called when a key is released
def on_release(key):
    print(f'Key {key} released')
    # Stop listener if the 'esc' key is pressed
    if key == keyboard.Key.esc:
        return False

# Main function to start the listener
def main():
    print("Starting key capture. Press 'esc' to stop.")
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
