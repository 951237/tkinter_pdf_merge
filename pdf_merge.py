from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

win = Tk()
win.title("Pdf Merger")
win.geometry("500x600")


def get_file_path():
    first_file_path = filedialog.askopenfilename(initialdir="/",
                                                 title="Select file",
                                                 filetypes=(
                                                     ("PDF files", "*.pdf"),
                                                     ("all files", "*.*")
                                                 )
                                                 )
    return first_file_path


def merge_pdf():
    pdf_first = get_file_path()
    pdf_second = get_file_path()
    result = filedialog.asksaveasfile(initialdir="/Users/mac/Documents/", title="Select file",
                                      filetypes=(("PDF files", "*.pdf"),
                                                 ("all files", "*.*")))
    output = PdfFileWriter()
    # pdf파일의 총 페이지
    page_num = pdf_first.getNumPages()

    # 두개의 파일 번갈아가며 합치기
    for i in range(page_num):
        output.addPage(pdf_first.getPage(0+i))
        output.addPage(pdf_second.getPage(((page_num-1))-i))

    outputStream = open(result, "wb")
    output.write(outputStream)
    outputStream.close()


btn = Button(win, text="PDF Merge", command=merge_pdf)
btn.grid(row=1, column=1)
win.mainloop()
