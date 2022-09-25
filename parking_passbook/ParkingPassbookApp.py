"""
Module name
- ParkingPassbookApp

Author
- 코드장인
- https://blog.naver.com/shawgibal
"""

from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용
import webbrowser
from ParkingBank import ParkingBank
from Version import getVersion

def calculateInterest(depositAmount, depositDuration):
    parkingBank = ParkingBank()

    parkingBank.setDepositAmount(depositAmount)
    parkingBank.setDepositDuration(depositDuration)

    interestResultList = parkingBank.getInterestList()

    interestResultStr = ""
    for interestResult in interestResultList:
        interestResultStr += "{:25s}: {:12.2f}".format(interestResult.getName(), interestResult.getInterest())
        interestResultStr += "\n"

    interestResultStr = interestResultStr[:-1]

    print('-'*40)
    print(interestResultStr)
    print('-'*40)

    return interestResultStr


def openweb():
    url = "https://blog.naver.com/shawgibal"
    webbrowser.open(url,new=1)


def main():
    window = Tk()                              # 창을 생성
    window.geometry("800x500")                 # 창 크기설정
    window.title("파킹통장 계산기 by 코드장인 Ver{}".format(getVersion()))   # 창 제목설정
    window.option_add("*Font","맑은고딕 15")    # 폰트설정
    window.resizable(False, False)             # x, y 창 크기 변경 불가

    def btnpress():                            # 함수 btnpress() 정의
        try:
            url = depositAmountEntry.get()
            # 상태 업데이트
            label.configure(text = '계산 시작')
            # 예치 금액 받아오기
            depositAmount = int(depositAmountEntry.get())
            # 예치 기간 받아오기
            depositDuration = int(depositDurationEntry.get())
            # 이자 계산
            interestResultStr = calculateInterest(depositAmount, depositDuration)
            # 상태 업데이트
            label.configure(text = '계산 완료')
            # 결과 출력
            resultLabel.configure(text=interestResultStr)
        except Exception as e:
            print(e)

    message = Label(window, text = '예치 금액', height=3)
    message.pack()

    depositAmountEntry = Entry(window, width=50)           # window라는 창에 입력창 생성
    depositAmountEntry.pack()                               # 입력창 배치

    message = Label(window, text = '예치 기간', height=3)
    message.pack()

    depositDurationEntry = Entry(window, width=50)           # window라는 창에 입력창 생성
    depositDurationEntry.pack()                               # 입력창 배치

    btn = Button(window)                       # window라는 창에 버튼 생성
    btn.config(text= "이자 계산")               # 버튼 내용 
    btn.config(width=10)              # 버튼 크기
    btn.config(command=btnpress)               # 버튼 기능 (btnpree() 함수 호출)
    btn.pack(pady=10)                                 # 버튼 배치

    label = Label(window, text = '진행 상태', height=2)
    label.pack()

    resultLabel = Label(window, text = '계산 결과', height=5)
    resultLabel.pack()

    Btn = Button(window, text = "코드장인의 코딩해우소 홈페이지",command=openweb)
    Btn.pack(side=BOTTOM, pady=10)


    window.mainloop()

if __name__ == "__main__":
    main()