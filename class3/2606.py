# 2026/04/11
# 알고리즘 분류: 그래프 이론, 그래프 탐색, BFS, DFS

import sys
from collections import deque

def bfs(start_node, graph, visited):
    queue = deque([start_node])
    visited[start_node] = True
    
    infected_count = 0 

    while queue:
        current = queue.popleft()
        
        for next_node in graph[current]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                infected_count += 1
                
    return infected_count


def main():
    input = sys.stdin.readline
    
    computer_count = int(input())
    link_count = int(input())
    
    network_map = [[] for _ in range(computer_count + 1)]
    visited = [False] * (computer_count + 1)
    
    for _ in range(link_count):
        u, v = map(int, input().split())
        network_map[u].append(v)
        network_map[v].append(u)
        
    result = bfs(1, network_map, visited)
    
    print(result)

if __name__ == "__main__":
    main()