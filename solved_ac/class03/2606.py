# 바이러스
N = int(input())
T = int(input())
virus = {}
for _ in range(T):
    a, b = map(int, input().split())
    if virus.get(a, None):
        virus[a].append(b)
    else:
        virus[a] = [b]
    if virus.get(b, None):
        virus[b].append(a)
    else:
        virus[b] = [a]
    
visited = [False for _ in range(N+1)]
visited[0] = True
for key, values in virus.items():
    q = []
    q.append(key)
    visited[key] = True
    count = 1
    for i in values:
        q.append()
