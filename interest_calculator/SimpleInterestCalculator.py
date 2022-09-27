"""
SimpleInterestCalculator.py

@ author: 코드장인
@ home page: https://blog.naver.com/shawgibal
"""

INTEREST_RATE = 0.03

def caculate_simple_interest(deposit_amount, deposit_duration):
    final_amount = deposit_amount * (1 + INTEREST_RATE * deposit_duration)
    return final_amount


def test():
    deposit_amount = 100000000
    deposit_duration = 1
    final_amount = caculate_simple_interest(deposit_amount, deposit_duration)

    expected_final_amount = 103000000
    print("final amount = {}".format(final_amount))
    print("expected final amount = {}".format(expected_final_amount))
    if final_amount == 103000000:
        print("PASS ~")
    else:
        print("FAIL ~")


if __name__ == "__main__":
    test()