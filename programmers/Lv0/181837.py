# 커피 심부름
def solution(order):
    answer = 0
    for drink in order:
        if drink == "anything":
            answer += 4500
        elif "cafelatte" in drink:
            answer += 5000
        elif "americano" in drink:
            answer += 4500
    
    return answer