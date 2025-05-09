# 동전 0
N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0
for i in range(N-1, -1, -1):
    count += K // coins[i]
    K %= coins[i]
    if K <= 0:
        break
print(count)