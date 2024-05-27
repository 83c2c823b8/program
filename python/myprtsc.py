#! /usr/bin/env python3
import time, timeout_decorator
import os,sys
from argparse import ArgumentParser
#from PIL import ImageGrab
import pyautogui as pag
#import tkinter

    
@timeout_decorator.timeout(420)
def scr_book():
    argparser = ArgumentParser()
    argparser.add_argument('--left' , action = 'store_true' ,default = False)
    argparser.add_argument('--large' , action = 'store_true' ,default = False)
    argparser.add_argument('-c' , action = 'store_true' ,default = False)
    argparser.add_argument('-n', type = int ,default = 1)
    args = argparser.parse_args()
    
    lr = 'right'
    a1 = 400
    a2 = 1520
    a3 = 1160
    a4 = 1525
    if args.left:
        lr = 'left'
    if args.large:
        a1 = 0
        a2 = 1920
        a3 = 0
        a4 = 3840    
    if not args.c:
        try:
            ut = str(time.time())[::-1]
            new_dir_path = "/home/gf1cg8to/Pictures/" + ut
            s = args.n
            os.mkdir(new_dir_path)
            pag.click(1080,1920)
            pag.moveTo(3240,5760)
            time.sleep(4)
            # scr = pag.screenshot(region=(1160, 0, 1525, 2160))
            # scr.save(new_dir_path + "/" + str(1000) +".jpg")
            # pag.press('right')
            #time.sleep(1.5)
            for i in range(0,s):
              scr = pag.screenshot(region=(a3, 0, a4 , 2160))
              scr.save(new_dir_path + "/" + str(1001 + i) +".jpg")
              pag.press(lr)
              time.sleep(1.5)
            for i in range(2000,3000,2):
              scr = pag.screenshot(region=(a1 , 0, a2, 2160))
              scr.save(new_dir_path + "/" + str(i) +".jpg")
              scr = pag.screenshot(region=(1920, 0, a2, 2160))
              scr.save(new_dir_path + "/" + str(i+1) +".jpg")
              pag.press(lr)
              time.sleep(1.5)
        except ValueError:
            print("\ninvalid value")
            sys.exit()
        except KeyboardInterrupt:
            print("\ngoodbye")
            sys.exit()
    else:
        try:
            ut = str(time.time())[::-1] new_dir_path = "." 
            s = int(input("Next page Number  : "))
            pag.click(1080,1920)
            pag.moveTo(3240,5760)
            time.sleep(1)
            pag.click(1080,1920)
            pag.moveTo(3240,5760)
            time.sleep(3)
            for i in range(s,5000,2):
              scr = pag.screenshot(region=(a1, 0, a2, 2160))
              scr.save(new_dir_path + "/" + str(i) +".jpg")
              scr = pag.screenshot(region=(1920, 0, a2, 2160))
              scr.save(new_dir_path + "/" + str(i+1) +".jpg")
              pag.press('right')
              time.sleep(1.5)
        except KeyboardInterrupt:
            print("\ngoodbye")



if __name__ == "__main__":
    scr_book()

