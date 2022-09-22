"""
parking_passbook.py

https://blog.naver.com/shawgibal
"""

ONE_YEAR_DAY = 365


class parking_passbook:
    def __init__(self):
        self.name = "파킹 통장"
        self.interest_rate = 0      # 기본 금리
        self.low_interest_rate = 0  # 한도액 초과시 금리
        self.max_amount = 0         # 기본 금리 적용되는 액수

    # 예금 액수
    def set_deposit(self, amount):
        #print("deposit amount = {}".format(amount))
        self.deposit_amount = amount

    # 예치 기간
    def set_duration(self, day):
        #print("duration day = {}".format(day))
        self.duration_day = day

    def get_name(self):
        return self.name

    # 이자 계산
    def calculate_interest(self):
        # 예치금이 기본 금리가 적용되는 최대 금액 이하일 경우
        if self.deposit_amount <= self.max_amount:
            return self.__calculate_interest__(self.deposit_amount,
                        self.interest_rate, self.duration_day)
        # 예치금이 기본 금리가 적용되는 최대 금액 초과할 경우
        else:
            interest = self.__calculate_interest__(self.max_amount,
                        self.interest_rate, self.duration_day)
            low_interest = self.__calculate_interest__(self.deposit_amount - self.max_amount,
                        self.low_interest_rate, self.duration_day)
            return interest + low_interest

    def __calculate_interest__(self, deposit_amount, interest_rate, duration_day):
        return deposit_amount * interest_rate * \
                        duration_day / ONE_YEAR_DAY

"""
케이뱅크 플러스 박스
"""
class kbank_plusbox(parking_passbook):
    def __init__(self):
        self.name = "케이뱅크 플러스 박스"
        self.interest_rate = 0.023
        self.low_interest_rate = 0
        self.max_amount = 300000000

"""
OK 세컨드 통장
"""
class ok_second(parking_passbook):
    def __init__(self):
        self.name = "오케이 세컨드 통장"
        self.interest_rate = 0.033
        self.low_interest_rate = 0.01
        self.max_amount = 10000000

"""
페퍼스 파킹 통장
"""
class peppers(parking_passbook):
    def __init__(self):
        self.name = "페퍼스 파킹 통장"
        self.interest_rate = 0.032
        self.low_interest_rate = 0.01
        self.max_amount = 50000000

