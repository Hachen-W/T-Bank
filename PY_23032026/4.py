from collections import deque


def bfs(start, graph, n, best_answer):
    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)

    queue = deque([start])
    dist[start] = 0

    best = best_answer

    while queue:
        vertex = queue.popleft()

        if dist[vertex] * 2 + 1 >= best:
            continue

        for to in graph[vertex]:
            if dist[to] == -1:
                dist[to] = dist[vertex] + 1
                parent[to] = vertex
                queue.append(to)
            elif parent[vertex] != to:
                cycle_len = dist[vertex] + dist[to] + 1
                if cycle_len < best:
                    best = cycle_len

    return best


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = 10**9

    for start in range(1, n + 1):
        answer = bfs(start, graph, n, answer)
        if answer == 3:
            break

    if answer == 10**9:
        print(-1)
    else:
        print(answer)


if __name__ == '__main__':
    main()
