# Union-Find 알고리즘 구현
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

# 입력 받기
n, m = map(int, input().split())
truth = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(m)]

# 부모 초기화
parent = [i for i in range(n + 1)]

# 진실을 아는 사람 그룹 처리
truth_set = set()
if truth[0] > 0:
    truth_set = set(truth[1:])

# 각 파티 사람끼리 연결
for party in parties:
    for i in range(1, party[0]):
        union(party[i], party[i+1])

# 진실을 아는 사람의 루트 부모 저장
truth_parents = set(find(person) for person in truth_set)

# 각 파티가 진실 그룹과 연결되어 있지 않은지 확인
result = 0
for party in parties:
    # 파티 내 사람의 부모 중 하나라도 진실 그룹과 연결된 경우 제외
    if not any(find(person) in truth_parents for person in party[1:]):
        result += 1

# 결과 출력
print(result)