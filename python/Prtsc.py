import time
import os
#from PIL import ImageGrab
import pyautogui as pag
#import tkinter
ut = time.time()
new_dir_path = "/home/gf1cg8to/Pictures/" + str(ut)
os.mkdir(new_dir_path)
time.sleep(4)
for i in range(293):
  scr = pag.screenshot(region=(0, 0, 3840, 2160))
  scr.save(new_dir_path + "/" + str(i + 100) +".jpg")
  pag.press('right')
  time.sleep(1.5)