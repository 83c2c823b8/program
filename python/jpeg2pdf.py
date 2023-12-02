import os
from PIL import Image
from reportlab.pdfgen import canvas

def convert_jpg_to_pdf(input_files, output_pdf):
    images = [Image.open(file) for file in input_files]

    if images:
        pdf_path = output_pdf + ".pdf"
        images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        print(f"PDFファイル {pdf_path} が作成されました。")
    else:
        print("変換する画像が見つかりませんでした。")

if __name__ == "__main__":
    # 100.jpgから始まる連番のJPEGファイルを読み込む
    input_files = sorted([file for file in os.listdir() if file.lower().endswith('.jpg')])

    # 出力するPDFファイルの名前
    output_pdf = input("PDFファイル名: ")

    # JPEGをPDFに変換
    convert_jpg_to_pdf(input_files, output_pdf)
