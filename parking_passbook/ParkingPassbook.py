"""
Module name
- ParkingPassbook

Author
- 코드장인
- https://blog.naver.com/shawgibal
"""


"""
Definitions
"""
ONE_YEAR_DAY = 365


"""
ParkingPassbook (Parent Class)
"""
class ParkingPassbook:
    def __init__(self):
        self.name = "Parking Passbook"
        self.interest_rate = 0      # 기본 금리
        self.low_interest_rate = 0  # 한도액 초과시 금리
        self.max_amount = 0         # 기본 금리 적용되는 액수

    # 예금 액수 입력
    def set_deposit(self, amount):
        #print("deposit amount = {}".format(amount))
        self.deposit_amount = amount

    # 예치 기간 입력
    def set_duration(self, day):
        #print("duration day = {}".format(day))
        self.duration_day = day

    # 통장 이름 리턴
    def get_name(self):
        return self.name

    # 이자 계산 & 결과 리턴
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
            return int(interest + low_interest)

    # Private Methods
    # 단리 계산 
    def __calculate_interest__(self, deposit_amount, interest_rate, duration_day):
        return deposit_amount * interest_rate * \
                        duration_day / ONE_YEAR_DAY


"""
Child Class
"""

"""
케이뱅크 플러스 박스
"""
class kbank_plusbox(ParkingPassbook):
    def __init__(self):
        self.name = "Kbank Plus Box"
        self.interest_rate = 0.023
        self.low_interest_rate = 0
        self.max_amount = 300000000

"""
OK 세컨드 통장
"""
class ok_second(ParkingPassbook):
    def __init__(self):
        self.name = "OK Second Passbook"
        self.interest_rate = 0.033
        self.low_interest_rate = 0.01
        self.max_amount = 10000000

"""
페퍼스 파킹 통장
"""
class peppers(ParkingPassbook):
    def __init__(self):
        self.name = "Peppers Parking Passbook"
        self.interest_rate = 0.032
        self.low_interest_rate = 0.01
        self.max_amount = 50000000

