# 체스판 다시 칠하기
N, M = map(int, input().split())
board = [[i for i in input()] for _ in range(N)]

result = []
for row in range(N):
    for col in range(1, M):
        result.append(check(row, col))