import time
import os
from PIL import ImageGrab
import pyautogui as pag
import tkinter
ut = time.time()
new_dir_path = R"c:\Users\gf1cg\Pictures\scr"+ str(ut) 
os.mkdir(new_dir_path)
time.sleep(5)
for i in range(120):
  scr = pag.screenshot()
  scr.save(r"c:\Users\gf1cg\Pictures\scr"  + str(ut) + "\ " + str(i + 100) +".jpg")
  pag.press('right')
  time.sleep(1.5)
pag.press('esc')
pag.keyDown('ctrl')
pag.keyDown('w')
pag.keyUp('ctrl')
pag.keyUp('w')