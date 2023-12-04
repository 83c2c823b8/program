import time
import os
#from PIL import ImageGrab
import pyautogui as pag
#import tkinter
ut = str(time.time())[::-1]
left_position = 450 #int(input(": "))
right_position = 3400 #int(input(" : "))
new_dir_path = "/home/gf1cg8to/Pictures/" + ut
os.mkdir(new_dir_path)

pag.click(2342,1288)
time.sleep(0.3)
pag.click(3743,1914)
time.sleep(0.3)
pag.click(1080,1920)
pag.moveTo(3240,5760)
time.sleep(4)

for i in range(0,2):
  scr = pag.screenshot(region=(1170, 0, 1510, 2160))
  scr.save(new_dir_path + "/" + str(1001 + i) +".jpg")
  pag.press('right')
  time.sleep(1.5)

time.sleep(2)

for i in range(2000,3000,2):
  scr = pag.screenshot(region=(left_position, 0, int((right_position - left_position)*0.5), 2160))
  scr.save(new_dir_path + "/" + str(i) +".jpg")
  scr = pag.screenshot(region=(left_position + int((right_position - left_position)*0.5), 0,int((right_position - left_position)*0.5), 2160))
  scr.save(new_dir_path + "/" + str(i+1) +".jpg")
  pag.press('right')
  time.sleep(1.5)