# -*- coding:utf-8 -*-


from collections import deque
from graph import Undigraph


def bfs(graph, s, t):
    if s == t:
        return 
    queue = deque()
    pre = [ -1 ] * len(graph)
    visited = [False] * len(graph)
    visited[s] = True
    queue.append(s)
    while len(queue) > 0:
        vertex = queue.popleft()
        for adj_v in graph[vertex]:
            if not visited[adj_v]:
                pre[adj_v] = vertex
                if adj_v == t:
                    return pre
                visited[adj_v] = True
                queue.append(adj_v)
    return pre

def print_vertex_trace(prev, s, t, level=1):
    if prev[t] != -1 and t != s:
        print_vertex_trace(prev, s, prev[t], level+1)
    if level == 1:
        print("%d" % t)
    else:
        print("%d -> " % t, end="")

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
    pre = bfs(g, 0, 7)
    print_vertex_trace(pre, 0, 7)
