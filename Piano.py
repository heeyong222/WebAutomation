import pyautogui as pg
import time
from PIL import ImageGrab
import keyboard

taps = [(1279, 790), (1384, 790), (1470, 790), (1567, 790)]
state = False # 게임 실행중 확인 변수

width, height = pg.size()
box = (0, 0, width/2, height)

def play():
    #print(pg.position())
    #time.sleep(.5)

    screen = ImageGrab.grab()
    for tap in taps:
        if (0, 0, 0) == screen.getpixel(tap):
            pg.click(*tap)# 언패킹 작업


while True:
    if not state and keyboard.is_pressed('a'):
        state = True
    elif state and keyboard.is_pressed('s'):
        state = False
        print('stop!')

    if state:
        play()