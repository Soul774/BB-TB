import ctypes
import keyboard
import mouse
import time

# windows api functions
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

hdc = user32.GetDC(0) # get device context

tolerance = 120 # raise if it doesnt dtc
scan_range = 50 # raise if miss in shiftlock
target_color = (0, 255, 0) # green #00FF00v

toggle = False

def pixelColor(x, y):
    pixel = gdi32.GetPixel(hdc, x, y)
    r = pixel & 0xFF
    g = (pixel >> 8) & 0xFF
    b = (pixel >> 16) & 0xFF
    return (r, g, b)

def isColorClose(color1, color2, tolerance):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def toggleTB():
    global toggle
    toggle = not toggle
    print(f"TB {'ON' if toggle else 'OFF'}")

keyboard.add_hotkey('v', toggleTB)

print("TB: Press 'V' to toggle, 'Esc' to exit.")

while True:
    if keyboard.is_pressed('esc'): # kill script
        break

    if toggle:
        x, y = mouse.get_position()
        green_detected = any(
            isColorClose(pixelColor(x + dx, y + dy), target_color, tolerance)
            for dx, dy in [(-scan_range, 0), (scan_range, 0), (0, -scan_range), (0, scan_range)]
        )
        if green_detected:
            mouse.click('left')
            time.sleep(0.1)
            print("Parried.")
