from collections import defaultdict

def dfs(G, i, visited):
    visited[i] = True
    for nbr in G[i]:
        if not visited[nbr]:
            dfs(G, nbr, visited)

def friendCircles(friends):
    if not friends: return 0

    G = defaultdict(list)
    n = len(friends)
    for i in xrange(n):
        for j in xrange(n):
            if friends[i][j] == "Y":
                G[i].append(j)
                G[j].append(i)

    visited = [False for _ in xrange(n)]
    cnt = 0
    for i in xrange(n):
        if not visited[i]:
            cnt += 1
            dfs(G, i, visited)

    return cnt

if __name__ == "__main__":
    friends = [
        "YYNN",
        "YYYN",
        "NYYN",
        "NNNY"
    ]
    assert friendCircles(friends) == 2

    friends2 = [
        "YNNNN",
        "NYNNN",
        "NNYNN",
        "NNNYN",
        "NNNNY"
    ]
    assert friendCircles(friends2) == 5