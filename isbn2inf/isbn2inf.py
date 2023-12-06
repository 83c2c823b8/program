import requests
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
from time import sleep

def main() :
    get_isbn_image(input("ISBNを入力してくだい : "))

def get_isbn_image(isbn):
    isbn = isbn.replace("ISBN", "").replace("-", "")
    url = f'https://iss.ndl.go.jp/thumbnail/{isbn}'
    response = requests.get(url)

    if response.status_code == 200:
        # バイナリデータから画像を取得
        image_data = BytesIO(response.content)
        image = Image.open(image_data)

        # Tkinterのウィンドウを作成して画像を表示
        root = tk.Tk()
        root.title("ISBN Image")

        tk_image = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=tk_image)
        label.pack()

        root.after(5000, root.destroy)

        root.mainloop()
    else:
        print(f"Failed to fetch image. Status code: {response.status_code}")

if __name__  == "__main__" :
    main()
