# ad 제거하기
def solution(strArr):
    answer = []
    for i in strArr:
        if "ad" not in i:
            answer.append(i.replace("ad", ""))
    return answer