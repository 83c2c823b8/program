import time
import os
#from PIL import ImageGrab
import pyautogui as pag
#import tkinter
ut = time.time()
reg0 = (1180,0,1580,2160)
reg1 = (245,0,3348,2160)
new_dir_path = "/home/gf1cg8to/Pictures/" + str(ut)
os.mkdir(new_dir_path)
time.sleep(4)
scr = pag.screenshot(region=reg0)
scr.save(new_dir_path + "/" + str(100) +".jpg")
pag.press('right')
time.sleep(1.5)
for i in range(293):
  scr = pag.screenshot(region=(reg1[0], reg1[1], int(reg1[2]*0.5), reg1[3]))
  scr.save(new_dir_path + "/" + str(2*i + 101) +".jpg")
  scr = pag.screenshot(region=(reg1[0] + int(reg1[2]*0.5) , reg1[1], int(reg1[2]*0.5), reg1[3]))
  scr.save(new_dir_path + "/" + str(2*i + 102) +".jpg")
  pag.press('right')
  time.sleep(1.5)