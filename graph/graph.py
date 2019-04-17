# -*- coding:utf-8 -*-


class UndirectedGraph(object):


    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_table = []
        for i in range(self.v_num + 1):
            self.adj_table.append([])

    def add_edge(self, s, t):
        if s > self.v_num or t > self.v_num:
            return False
        self.adj_table[s].append(t)
        self.adj_table[t].append(s)
        return True


if __name__ == '__main__':
    g = UndirectedGraph(10)
    g.add_edge(1, 9)
    g.add_edge(1, 3)
    g.add_edge(3, 2)
    g.add_edge(3, 2)
    g.add_edge(3, 2)
    g.add_edge(3, 2)
    print(g.adj_table)
        
