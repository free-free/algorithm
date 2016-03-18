#-*- coding:utf-8 -*-


class QuickFind(object):
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
class QuickUnion(object):
	def __init__(self,objnum):
		self.id=[i for i in range(0,objnum)]
	def _root(self,obj):
		i=obj
		while i!=self.id[i]:
			i=self.id[i]
		return i
	def union(self,p,q):
		qroot=self._root(q)
		proot=self._root(p)
		self.id[proot]=qroot
	def connected(self,q,p):
		return self._root(q)==self._root(p) 	
class QuickUnionWithWeighted(object):
	r'''
		quick union with weighted tree
	'''
	def __init__(self,objnum):
		self.id=[i for i in range(0,objnum)]
		self.sz=[0 for i in range(0,objnum)]
	def _root(self,obj):
		i=obj
		while i!=self.id[i]:
			i=self.id[i]
		return i
	def union(self,p,q):
		qroot=self._root(q)
		proot=self._root(p)
		if self.sz[q]>=self.sz[p]:
			self.id[proot]=qroot
			self.sz[qroot]=self.sz[qroot]+self.sz[proot]
		else:
			self.id[qroot]=proot
			self.sz[proot]+=self.sz[qroot]
	def connected(self,q,p):
		return self._root(q)==self._root(p)
if __name__=='__main__':
	#uf=QuickFind(10)	
	#uf=QuickUnion(20)
	uf=QuickUnionWithWeighted(20)
	uf.union(1,4)
	uf.union(0,9)
	print('1 connected 4',uf.connected(1,4))
	print('0 connected 9',uf.connected(0,9))
	print('4 connected 3',uf.connected(4,3))
	print(uf.id)
	print('union 4 to 3')
	uf.union(4,3)
	print(uf.id)
	print('4 connected 3',uf.connected(4,3))
	print('1 connected 3',uf.connected(3,1))
	
