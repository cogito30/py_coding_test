# 부족한 금액 계산하기
def solution(price, money, count):
    answer = -1
    for i in range(count):
        money -= price * (i + 1)
    if money >= 0:
        answer = 0
    else:
        answer = -money
    return answer