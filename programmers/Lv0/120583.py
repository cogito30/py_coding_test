# 중복된 숫자 개수
def solution(array, n):
    answer = 0
    for i in array:
        if n == i:
            answer += 1
    return answer