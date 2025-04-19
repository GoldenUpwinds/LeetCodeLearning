from typing import List
import heapq
import sys
import ast
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nextArray = collections.defaultdict(list)
        for u,v,w in times:
            nextArray[u].append((v,w))
        
        dist = {node:float('inf') for node in range(1,n+1)}
        heap = [(0,k)]
        dist[k] = 0
        visited = set()

        while heap:
            _, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            for v,w in nextArray[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap,(dist[v],v))
        
        max_time = max(dist.values())
        
        return max_time if max_time < float('inf') else -1

def main():
    times = sys.stdin.readline().strip()
    times = ast.literal_eval(times)
    n, k = map(int,input().split())

    Solve = Solution()
    max_time = Solve.networkDelayTime(times,n,k)
    print(max_time)
    return

if __name__ == "__main__":
    main()
    