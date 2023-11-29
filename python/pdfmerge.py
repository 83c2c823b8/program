import pypdf

print(pypdf.__version__)
# 3.7.1

merger = pypdf.PdfMerger()
m1 = input("1つ目のpdfファイル名 : ")
m2 = input("2つ目のpdfファイル名 : ")

merger.append("./" +  m1 + ".pdf")
merger.append("./" + m2 + ".pdf")

merger.write("./" + m1 + "_" + m2 +  "_merged.pdf")
merger.close