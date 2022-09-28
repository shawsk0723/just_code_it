"""
Pdf2ImageApp.py

author: 코드장인
blog: https://blog.naver.com/shawgibal
"""

from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용
from tkinter import filedialog
import os 
from pathlib import Path
from unittest import result
import webbrowser
from Pdf2ImageConverter import Pdf2ImageConverter
import traceback

def openweb():
    url = "https://blog.naver.com/shawgibal"
    webbrowser.open(url,new=1)

def main():
    window = Tk()                              # 창을 생성
    window.geometry("800x400")                 # 창 크기설정
    window.title("유튜브 다운로드 by 걍교쥬")           # 창 제목설정
    window.option_add("*Font","맑은고딕 15")    # 폰트설정
    window.resizable(False, False)             # x, y 창 크기 변경 불가

    # 파일 열기 버튼 클릭시 호출
    def fileOpenDialog():
        window.pdfFilePath = filedialog.askopenfilename(initialdir= os.path.dirname(__file__))    
        pdfFileLabel.configure(text = window.pdfFilePath)

    # 파일 열기 버튼
    button = Button(window, text="PDF 파일 열기", command=fileOpenDialog, width=30)
    button.pack(pady=10)

    # PDF 파일 경로 표시
    pdfFileLabel = Label(window, text="PDF 파일")
    #label.grid(column=0, row=0)
    pdfFileLabel.pack(pady=10)

    # PDF 이미지 변환 버튼 클릭
    pdf2ImageConverter = Pdf2ImageConverter()
    def btnpress():                            # 함수 btnpress() 정의
        try:
            print('button press')

            # 0. 이미지 파일 저장 위치 설정
            pdfFilePath = window.pdfFilePath
            path, pdfFileName = os.path.split(pdfFilePath)             # 경로와 파일 이름 분리
            pdfNameOnly = Path(pdfFileName).stem        # 파일 이름과 확장자 분리
            outputDir = path + '/' + pdfNameOnly + '/image'

            # 1. PDF 이미지 추출 함수 호출
            pdf2ImageConverter.convert(pdfFilePath, outputDir)

            # 2. 결과 출력
            resultlabel.configure(text = "변환 완료")

        except Exception as e:
            resultlabel.configure(text = "변환 실패\n" + str(e))
            print(e)
            traceback.format_exc(e)

    # PDF 이미지 변환 버튼
    btn = Button(window)                       # window라는 창에 버튼 생성
    btn.config(text= "PDF 이미지 변환")               # 버튼 내용 
    btn.config(width=30)                      # 버튼 크기
    btn.config(command=btnpress)               # 버튼 기능 (btnpree() 함수 호출)
    btn.pack(pady=10)                                 # 버튼 배치

    # 변환 결과 (성공, 실패) 출력
    resultlabel = Label(window, text = 'PDF 이미지 변환 결과', height=3)
    resultlabel.pack(pady=10)

    # 블로그 홈페이지 바로가기 버튼
    openWebButton = Button(window, text = "코드장인 블로그 바로가기",command=openweb)
    openWebButton.pack(side=BOTTOM, pady=20)

    window.mainloop()


if __name__ == "__main__":
    main()
