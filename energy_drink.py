import time

import pyautogui

INTERVAL_IN_SECONDS = 60 * 1

def main():
    while True:
        pyautogui.keyUp('shift')
        # pyautogui.move(0, -1)   # move up one pixel
        # pyautogui.move(0, 1)    # cowardly move back
        time.sleep(INTERVAL_IN_SECONDS)

if __name__ == "__main__":
    main()
