#-*- coding:utf-8 -*-


class UnionFind(object):
	def __init__(self,objnum):
		self.id=[i for i in range(0,objnum)]
	def union(self,p,q):
		qid=self.id[q]
		pid=self.id[p]
		j=0
		for v in self.id:
			if pid==v:
				self.id[j]=qid
			j=j+1
	def connected(self,q,p):
		return self.id[q]==self.id[p]
	
if __name__=='__main__':
	uf=UnionFind(10)
	uf.union(1,4)
	uf.union(0,9)
	print('1 connected 4',uf.connected(1,4))
	print('0 connected 9',uf.connected(0,9))
	print('4 connected 3',uf.connected(4,3))
	print('union 4 to 4')
	print(uf.id)
	uf.union(4,3)
	print(uf.id)
	print('4 connected 3',uf.connected(4,3))
	print('1 connected 3',uf.connected(3,1))
	
