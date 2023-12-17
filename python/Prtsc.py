import time
import os
#from PIL import ImageGrab
import pyautogui as pag
#import tkinter
ut = str(time.time())[::-1]
new_dir_path = "/home/gf1cg8to/Pictures/" + ut
os.mkdir(new_dir_path)
time.sleep(4)
# scr = pag.screenshot(region=(1160, 0, 1525, 2160))
# scr.save(new_dir_path + "/" + str(999) +".jpg")
# pag.press('right')
# time.sleep(1.5)
# scr = pag.screenshot(region=(1160, 0, 1525, 2160))
# scr.save(new_dir_path + "/" + str(1000) +".jpg")
# pag.press('right')
time.sleep(1.5)
for i in range(1000,1600,2):
  scr = pag.screenshot(region=(0, 0, 1920, 2160))
  scr.save(new_dir_path + "/" + str(i) +".jpg")
  scr = pag.screenshot(region=(1920, 0, 1920, 2160))
  scr.save(new_dir_path + "/" + str(i+1) +".jpg")
  pag.press('right')
  time.sleep(1.5)
