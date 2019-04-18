# -*- coding:utf-8 -*-


from collections import deque
from graph import Undigraph


def bfs(graph, s, t):
    if s == t:
        return 
    queue = deque()
    prev = [ -1 ] * len(graph)
    visited = [False] * len(graph)
    visited[s] = True
    queue.append(s)
    while len(queue) > 0:
        vertex = queue.popleft()
        for adj_v in graph[vertex]:
            if not visited[adj_v]:
                prev[adj_v] = vertex
                if adj_v == t:
                    return prev
                visited[adj_v] = True
                queue.append(adj_v)
    return prev

def print_vertex_trace(prev, s, t, level=1):
    if prev[t] != -1 and t != s:
        print_vertex_trace(prev, s, prev[t], level+1)
    if level == 1:
        print("%d" % t)
    else:
        print("%d -> " % t, end="")



def recursive_dfs(graph, s, t):
    prev = [-1] * len(graph)
    visited = [False] * len(graph)
    found = False
    def rdfs(s, t):
        nonlocal found
        if s == t:
            found = True
            return 
        for v in graph[s]:
            if not visited[v]:
                visited[v] = True
                prev[v] = s
                rdfs(v, t)
    rdfs(s, t)
    return prev
        

if __name__ == '__main__':
    g = Undigraph(8)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 7)
    print(g)
    bfs_prev = bfs(g, 0, 7)
    print_vertex_trace(bfs_prev, 0, 7)
    dfs_prev = recursive_dfs(g, 0, 6)
    print_vertex_trace(dfs_prev, 0, 6) 
