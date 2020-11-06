import keyboard
from time import sleep

#script = open('script.txt').read().split()
script = open('script.txt').read().split('.')

sleep(5)
for i in range(len(script)):
    # print(script[i])
    for j in range(len(script[i])):
        # print(script[i][j])
        keyboard.write(script[i][j])
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.25)
