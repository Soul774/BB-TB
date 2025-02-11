import pyautogui
import keyboard
import numpy as np
import cv2

tolerance = 90
scan_range = 30
target_color = (0, 255, 0)

toggle = False

def isColor(pixel, target_color, tolerance):
    diff = np.abs(np.array(pixel) - np.array(target_color))
    return np.all(diff <= tolerance)

def toggleTB():
    global toggle
    toggle = not toggle
    print(f"TB {'ON' if toggle else 'OFF'}")

keyboard.add_hotkey('v', toggleTB)

print("Press 'V' to toggle, 'Esc' to exit.")

while True:
    if toggle:
        x, y = pyautogui.position()  # cursor pos
        region = (x - scan_range, y - scan_range, scan_range * 2 + 1, scan_range * 2 + 1) # region defining

        screenshot = pyautogui.screenshot(region=region)
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        foundColor = False
        for dx in range(screenshot.shape[0]):
            for dy in range(screenshot.shape[1]):
                pixel_color = screenshot[dx, dy]
                if isColor(pixel_color, target_color, tolerance):
                    foundColor = True
                    break
            if foundColor:
                break
        if foundColor:
            pyautogui.click()
            print("Parried.")

    if keyboard.is_pressed('esc'):
        print("Exiting..")
        break
