"""
F1DailySavings.py

@ author: 코드장인
@ home page: https://blog.naver.com/shawgibal
"""

"""
Parent Class
"""

class F1DailySavings:
    def __init__(self):
        self.name = "F1 Daily Savings"
        self.interest_rate = 0      # 기본 금리
        self.duration = 0         # 기본 금리 적용되는 액수
        self.dailyDepositAmount = 50000 # 일일 적금 액수
        self.totalPrincipal = 0 # 원금 총액

    # 일일 적금 액수 입력
    def setDailyDepositAmount(self, amount):
        #print("deposit amount = {}".format(amount))
        self.dailyDepositAmount = amount

    def calculateInterestAmount(self):
        self.interestAmount = self.dailyDepositAmount * \
                            self.interest_rate * \
                            (self.duration * (self.duration + 1)) / 2 / 365
        return int(self.interestAmount)

    def getName(self):
        return self.name

    def getTotalPricipal(self):
        return self.dailyDepositAmount * self.duration

    def getInterestAmount(self):
        return self.interestAmount

    def getDuration(self):
        return self.duration

"""
Child Class
"""

class F1DailySavings100(F1DailySavings):
    def __init__(self):
        self.name = "F1 Daily Savings 100 Days"
        self.interest_rate = 0.07      # 기본 금리
        self.duration = 100              # 적금 기간


class F1DailySavings150(F1DailySavings):
    def __init__(self):
        self.name = "F1 Daily Savings 150 Days"
        self.interest_rate = 0.09      # 기본 금리
        self.duration = 150              # 적금 기간


def testF1DailySavings100():
    dailyDepositAmount = 50000
    expectedinterestAmount = 48424

    f1DailySavings = F1DailySavings100()
    f1DailySavings.setDailyDepositAmount(dailyDepositAmount)
    interestAmount = f1DailySavings.calculateInterestAmount()

    print("test {}".format(f1DailySavings.getName()))
    print("actual result = {}, expected result = {}".format(
                            interestAmount,expectedinterestAmount))
    
    if interestAmount == expectedinterestAmount:
        print("PASS ~")
    else:
        print("FAIL ~")

def testF1DailySavings150():
    dailyDepositAmount = 50000
    expectedinterestAmount = 139623

    f1DailySavings = F1DailySavings150()
    f1DailySavings.setDailyDepositAmount(dailyDepositAmount)
    interestAmount = f1DailySavings.calculateInterestAmount()

    print("test {}".format(f1DailySavings.getName()))
    print("actual result = {}, expected result = {}".format(
                            interestAmount,expectedinterestAmount))

    if interestAmount == expectedinterestAmount:
        print("PASS ~")
    else:
        print("FAIL ~")

if __name__ == "__main__":
    testF1DailySavings100()
    testF1DailySavings150()
