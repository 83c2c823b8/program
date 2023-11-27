import pyautogui as pag
import time
try :
  while True :
    x, y = pag.position()
    print(x, y)
    time.sleep(0.1)
  end
except KeyboardInterrupt:
  raise