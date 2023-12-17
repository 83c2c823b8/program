import time
import os
#from PIL import ImageGrab
import pyautogui as pag
#import tkinter
ut = str(time.time())[::-1]
init = int(input("次にはじめるファイル番号名 : "))
pag.click(1080,1920)
pag.moveTo(3240,5760)
time.sleep(5)
for i in range(init , init + 500 , 2):
    scr = pag.screenshot(region=(400, 0, 1520, 2160))
    scr.save("./" + str(i) +".jpg")
    scr = pag.screenshot(region=(1920, 0, 1520, 2160))
    scr.save("./" + str(i + 1) +".jpg")
    pag.press('right')
    time.sleep(1.5)

