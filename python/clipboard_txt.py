from time import sleep
import pyperclip

previous_text = pyperclip.paste()

while True:
  if pyperclip.paste() != previous_text:
    # クリップボードの値が更新されている場合
    copied_text = pyperclip.paste()
    previous_text = copied_text
    new_text = copied_text.replace("\r\n", "").replace("\n", "").replace(" ", "")
    print(new_text, "\n")

    with open('output.txt', 'a', encoding='utf-8') as f:
      f.write(new_text + "\n")

  sleep(0.1)