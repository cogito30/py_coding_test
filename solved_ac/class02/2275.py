# 부녀회장이 될테야
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            people[j] += people[j-1]
    print(people[n])
