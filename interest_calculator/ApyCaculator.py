"""
ApyCaculator.py

@ author: 코드장인
@ home page: https://blog.naver.com/shawgibal
"""

from F1DailySavings import *


def calculateApy( principal, duration, interest):
    apy = (interest/principal)*(365/duration)*100
    return round(apy, 2)


def getF1DailySavingsApy():
    f1DailySavings = [F1DailySavings100(), F1DailySavings150()]

    print("수익률 연이자 환산 결과")
    dailyDepositAmount = 50000
    for f1DailySaving in f1DailySavings:
        f1DailySaving.setDailyDepositAmount(dailyDepositAmount)
        interest = f1DailySaving.calculateInterestAmount()
        principal = f1DailySaving.getTotalPricipal()
        duration = f1DailySaving.getDuration()
        apy = calculateApy(principal, duration, interest)
        print("{}: {}%".format(f1DailySaving.getName(), apy))

if __name__ == "__main__":
    getF1DailySavingsApy()
