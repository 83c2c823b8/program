import time 
import os
#from PIL import ImageGrab
import pyautogui as pag
#import tkinter
def scr_book():
    ut = str(time.time())[::-1]
    new_dir_path = "." 
    s = int(input("Next page Number  : "))
    pag.click(1080,1920)
    pag.moveTo(3240,5760)
    time.sleep(1)
    pag.click(1080,1920)
    pag.moveTo(3240,5760)
    time.sleep(3)
    for i in range(s,5000,2):
      scr = pag.screenshot(region=(400, 0, 1520, 2160))
      scr.save(new_dir_path + "/" + str(i) +".jpg")
      scr = pag.screenshot(region=(1920, 0, 1520, 2160))
      scr.save(new_dir_path + "/" + str(i+1) +".jpg")
      pag.press('right')
      time.sleep(1.5)

if __name__ == "__main__":
    scr_book()

