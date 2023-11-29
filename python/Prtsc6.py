import time
import os
#from PIL import ImageGrab
import pyautogui as pag
#import tkinter
ut = str(time.time())[::-1]
left_position = int(input("左辺の座標 : "))
right_position = int(input("右辺の座標 : "))
new_dir_path = "/home/gf1cg8to/Pictures/" + ut
os.mkdir(new_dir_path)
time.sleep(4)
for i in range(1000,1600,2):
  scr = pag.screenshot(region=(left_position, 0, int((right_position - left_position)*0.5), 2160))
  scr.save(new_dir_path + "/" + str(i) +".jpg")
  scr = pag.screenshot(region=(left_position + int((right_position - left_position)*0.5), 0,int((right_position - left_position)*0.5), 2160))
  scr.save(new_dir_path + "/" + str(i+1) +".jpg")
  pag.press('right')
  time.sleep(1.5)