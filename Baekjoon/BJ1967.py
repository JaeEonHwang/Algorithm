    import sys
    sys.stdin = open('input.txt', 'r')


    N = int(input())
    tree = [(1, 0, 1) for _ in range(10001)]
    leaf = []
    for i in range(N-1):
        parent, child, value = map(int, input().split())
        tree[child] = (parent, value, child)
        leaf.append(child)
        if parent in leaf:
            leaf.remove(parent)
        if i == 0:
            leaf.append(parent)
    leaf2 = []
    # 리프 노드 찾아내기
    for i in leaf:
        road = []
        while i != 1:
            road.insert(0, tree[i])
            i = tree[i][0]
        leaf2.append(road)
    leafs = len(leaf2)
    ans = 0
    # 각 리프노드끼리 이어지는 거리 찾기
    # 리프1-루트 + 리프2+루트 - 두 리트가 루트로 갈 때 겹치는 동선
    for i in range(leafs - 1):
        for j in range(i + 1, leafs):
            diameter = 0
            idx = 0
            while leaf2[i][idx] == leaf2[j][idx]:
                idx += 1
                if idx == len(leaf2[i]) or idx == len(leaf2[j]):
                    break
            for k in range(idx, len(leaf2[i])):
                diameter += leaf2[i][k][1]
            for k in range(idx, len(leaf2[j])):
                diameter += leaf2[j][k][1]
            if diameter > ans:
                ans = diameter
    # 루트가 리프가 될 수도 있어서 더블체크
    for roads in leaf2:
        leafto1 = 0
        for road in roads:
            leafto1 += road[1]
        if leafto1 > ans:
            ans = leafto1
    print(ans)
