# 문자열 내 p와 y의 개수
def solution(s):
    answer = False
    p_count = 0
    y_count = 0
    for i in s.lower():
        if i == "p":
            p_count += 1
        elif i == "y":
            y_count += 1
    if p_count == y_count:
        answer = True
            
    return answer