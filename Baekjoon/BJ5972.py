import sys
sys.stdin = open('input.txt', 'r')


# 다익스트라 너무 오랜만에 해서 고생 좀 했다;;
from heapq import heappop, heappush

N, M = map(int, input().split())
roads = [[] for _ in range(N)]
visited = [1001 * N] * N
heap = []
visited[0] = 0
# 출발지점은 heap에 따로 저장
for _ in range(M):
    a, b, c = map(int, input().split())
    if a - 1 == 0:
        heappush(heap, (c, b-1))
    else:
        roads[a-1].append((c, b - 1))
    if b - 1 == 0:
        heappush(heap, (c, a - 1))
    else:
        roads[b-1].append((c, a - 1))
# 최종 도착지까지 필요한 여물이 갱신될 때까지
while visited[N-1] == 1001 * N:
    # 이동 가능한 지점 중 여물이 제일 적게 필요한 곳으로 이동
    feed, e = heappop(heap)
    # 기존 visited 값보다 작으면 업데이트
    if visited[e] > feed:
        visited[e] = feed
        # 해당 지점에서 이동할 수 있는 다른 지점 옵션으로 추가
        # 현재까지 소비한 여물은 계속 더해가면서
        for nfeed, ne in roads[e]:
            heappush(heap,(nfeed+visited[e], ne))
print(visited[N-1])
