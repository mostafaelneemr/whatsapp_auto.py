import random
import pyautogui as pg
import time

message = (' let message !')

time.sleep(10)

for i in range(100):
    a = random.choice(message)
    pg.write('message')
    pg.press('enter')