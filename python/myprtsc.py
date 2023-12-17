import time
import os
import pyautogui as pag
s = int(input("真ん中の枚数 : "))
def picturedir():
    ut = str(time.time())[::-1]
    new_dir_path = "/home/gf1cg8to/Pictures/" + ut
    os.mkdir(new_dir_path)
    pag.click(1080,1920)
    pag.moveTo(3240,5760)
    time.sleep(4)
# scr = pag.screenshot(region=(1160, 0, 1525, 2160))
# scr.save(new_dir_path + "/" + str(1000) +".jpg")
# pag.press('right')
#time.sleep(1.5)
for i in range(0,s):
  scr = pag.screenshot(region=(1160, 0, 1525, 2160))
  scr.save(new_dir_path + "/" + str(1001 + i) +".jpg")
  pag.press('right')
  time.sleep(1.5)
for i in range(2000,3000,2):
  scr = pag.screenshot(region=(400, 0, 1520, 2160))
  scr.save(new_dir_path + "/" + str(i) +".jpg")
  scr = pag.screenshot(region=(1920, 0, 1520, 2160))
  scr.save(new_dir_path + "/" + str(i+1) +".jpg")
  pag.press('right')
  time.sleep(1.5)
