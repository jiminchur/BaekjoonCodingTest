N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]

ranks = []

for i in range(N):
    rank = 1  # 기본 등수는 1등
    for j in range(N):
        if i != j:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                rank += 1
    ranks.append(rank)

print(" ".join(map(str, ranks)))