import time
import pyautogui
import pyperclip
from yt_dlp import YoutubeDL

def youtube2mp3():
    # 設定(mp3形式にするなど）
    ydl_opts = {
        # 'outtmpl': "",
        "format": "mp3/bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }
    rep = int(input("プレイリストの動画数 : "))
    time.sleep(2)
    my_array = []

    for _ in range(rep-1):  
        pyautogui.press('y')
        pyautogui.press('y') #urlのヤンク
        clipboard_content = pyperclip.paste()
        my_array.append(clipboard_content)
        pyautogui.write('i')
        pyautogui.hotkey('shift', 'n')
        pyautogui.press('esc')
        time.sleep(1)  

    for i in my_array :
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.download(i)

if __name__ == '__main__':
    youtube2mp3()