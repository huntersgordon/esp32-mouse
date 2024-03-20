

import serial
import pyautogui
import json

# Special characters mapping
special_chars = {
    '<SP>': 'space',  # Space character
    '<BK>': 'backspace',  # Backspace character
    # Add more mappings here if needed
}


# Configuration
serial_port = '/dev/cu.usbserial-0001'
baud_rate = 115200
movement_scale = 2  # Scale the movement by this factor to increase speed
movement_duration = 0.01  # Duration of the mouse movement in seconds

pyautogui.PAUSE = 0  # Remove delay after each pyautogui call

def main():

    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    with ser:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                try:
                    data = json.loads(line)
                    if data['x'] != -1 and data['y'] != -1:
                        # Scale the x and y values to increase tracking speed
                        scaled_x = data['x'] * movement_scale
                        scaled_y = data['y'] * movement_scale
                        move_mouse(scaled_x, scaled_y)
                except json.JSONDecodeError:
                    pass  # Ignore invalid JSON for speed

def move_mouse(x, y):
    # Move mouse quickly to the new scaled position
    pyautogui.moveTo(x, y, duration=movement_duration, _pause=False)

if __name__ == '__main__':
    main()