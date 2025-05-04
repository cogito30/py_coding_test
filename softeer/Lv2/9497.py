# [한양대 HCPC 2023] Recovering the Region
import sys

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    for _ in range(N):
        print(i + 1, end = " ")
    print()