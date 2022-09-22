"""
parking_passbook.py

https://blog.naver.com/shawgibal
"""

from inspect import Traceback
import traceback
from parking_bank import *

def main():

    parkingBank = ParkingBank()

    while True:
        try:
            print("프로그램을 종료하려면 x를 누르세요 ~")

            print("예치 금액을 원 단위로 입력하세요 ~")
            deposit_amount = input()

            if deposit_amount == "x":
                print("프로그램을 종료합니다.")
                break

            print("예치 기간을 일 단위로 입력하세요 ~")
            deposit_duration = input()

            if deposit_amount == "x":
                print("프로그램을 종료합니다.")
                break

            print("예치 금액 = {}원".format(deposit_amount))
            print("예치 기간 = {}원".format(deposit_duration))

            parkingBank.setDepositAmount(int(deposit_amount))
            parkingBank.setDepositDuration(int(deposit_duration))

            interestResultList = parkingBank.getInterestList()
            print('-'*40)
            for interestResult in interestResultList:
                print("{}: {:12.2f}".format(interestResult.getName(), interestResult.getInterest()))
            print('-'*40)

        except Exception as e:
            print('Exception happens')
            print(traceback.format_exc())

if __name__ == "__main__":
    main()