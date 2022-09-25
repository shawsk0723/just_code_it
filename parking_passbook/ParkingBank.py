"""
parking_bank.py

https://blog.naver.com/shawgibal
"""


from ParkingPassbook import *


PB_NAME = "name"
PB_INTEREST = "interest"

class ParkingBank:
    def __init__(self):
        self.parking_passbook_list = []
        self.parking_passbook_list.append(kbank_plusbox())
        self.parking_passbook_list.append(ok_second())
        self.parking_passbook_list.append(peppers())
        print(self.parking_passbook_list)

    def setDepositAmount(self, deposit_amount):
        for parkingpassbook in self.parking_passbook_list:
            parkingpassbook.set_deposit(deposit_amount)

    def setDepositDuration(self,deposit_duration):
        for parkingpassbook in self.parking_passbook_list:
            parkingpassbook.set_duration(deposit_duration)

    def getInterestList(self):
        interestResultList = []
        for parkingpassbook in self.parking_passbook_list:
            name = parkingpassbook.get_name()
            interest = parkingpassbook.calculate_interest()

            interestResult = InterestResult(name, interest)
            interestResultList.append(interestResult)

        return interestResultList


class InterestResult:
    def __init__(self, name, interest):
        self.name = name
        self.interest = interest

    def getName(self):
        return self.name

    def getInterest(self):
        return self.interest

def main():
    parkingBank = ParkingBank()

    parkingBank.setDepositAmount(int(20000000))
    parkingBank.setDepositDuration(int(365))

    interestResultList = parkingBank.getInterestList()
    print('-'*40)
    for interestResult in interestResultList:
        print("{:25s}: {:12.2f}".format(interestResult.getName(), interestResult.getInterest()))
    print('-'*40)


if __name__ == "__main__":
    main()