import sys
import ast
import collections
import heapq


def main():
    data = sys.stdin.readlines()
    n, m, q = map(int, data[0].strip().split())

    graph = collections.defaultdict(list)
    for i in range(1, m + 1):
        u, v, w = map(int, data[i].strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    sends = list(map(int, data[m + 1].strip().split()))

    visited = set()
    heap = [(0, 1)]
    dist = {node: float("inf") for node in range(1, n + 1)}
    dist[1] = 0

    while heap:
        _, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    output = 0
    for send in sends:
        output += 2 * dist[send]

    print(output)
    return


if __name__ == "__main__":
    main()
