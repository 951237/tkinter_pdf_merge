from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import sys

win = Tk()
win.title("Pdf Merger")
win.geometry("500x600")

# 파일 열어서 경로 추출
def get_file_path():
    first_file_path = filedialog.askopenfilename(initialdir="/",
                    title="Select file",
                    filetypes=(("PDF files", "*.pdf"),("all files", "*.*"))
                    )
    return first_file_path


# PDF파일 합치기
def merge_pdf():
    pdf_first = get_file_path()     # 첫번째 파일
    pdf_second = get_file_path()    # 두번째 파일
    file1 = PdfFileReader(open(pdf_first, 'rb'))    # 파일 열기
    file2 = PdfFileReader(open(pdf_second, 'rb'))   # 파일 열기
    result = "./result.pdf"     # 결과파일 경로 지정하기
    pdf_writer = PdfFileWriter()    # pdf 파일 작성하기
    # pdf파일의 총 페이지
    page_num = file1.getNumPages()  # pdf 파일 전체 쪽수 추출

    # 두개의 파일 번갈아가며 합치기
    for i in range(page_num):   # 페이지 쪽수만큼 반복하기
        pdf_writer.addPage(file1.getPage(0+i))  # 첫번째 파일의 1장부터 시작
        pdf_writer.addPage(file2.getPage((page_num-1)-i))   # 두번째 파일의 역순부터 시작

    result_file = open(result, "wb")
    pdf_writer.write(result_file)
    result_file.close()
    sys.exit()  # 시스템 나가기

# tkinter 화면 설정하기
btn = Button(win, text="PDF Merge", command=merge_pdf)
btn.grid(row=2, column=3)
win.mainloop()
