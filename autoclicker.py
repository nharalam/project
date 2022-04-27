# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()
break_program = False


def begin():
    mouse.position = (1281, 44)
    time.sleep(.2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(.2)
    mouse.position = (1247, 227)
    time.sleep(.2)
    mouse.scroll(0, -2)
    mouse.position = (991, 708)
    time.sleep(.2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(.2)


def click():
    # mouse.position = (721, 299)
    for i in range(1, 201):
        while not break_program:
            mouse.press(Button.left)
            mouse.release(Button.left)
            # time.sleep(.005)
            time.sleep(.05)


def on_press(key):
    global break_program
    print(key)
    if key == keyboard.Key.f2:
        print('end pressed')
        break_program = True
        return False


time.sleep(3)
click()


with keyboard.Listener(on_press=on_press) as listener:
    while not break_program:
        print('program running')
        time.sleep(5)
    listener.join()


# print(format(mouse.position))
# begin()
