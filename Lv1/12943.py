# 콜라츠 추측
def solution(num):
    answer = 0
    if num == 1:
        return 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        elif num % 2 == 1:
            num = num * 3 + 1
        answer += 1
        if answer >= 500:
            answer = -1
            break
    return answer