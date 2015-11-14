#!/usr/bin/python

class QU:
	arr=[]
	def __init__(self,n):
		for i in range(0,n):
			self.arr.append(i)	
	def root(self,e):
		i=e
		while i!=self.arr[i]:
			i=self.arr[i]
		return i
	def connected(self,p,q):
		return self.root(q)==self.root(p)
	def union(self,p,q):
		qroot=self.root(q)
		proot=self.root(p)
		self.arr[proot]=qroot

l=int(raw_input("please input length of object:"))
obj=QU(l)
flag=1
while flag==1:
	cmd=raw_input('please enter command(union||1 or connected||2): ')
	if cmd=='exit':
		print 'exit'
		flag=0
		continue
	z=raw_input('please input p and q:')
	z=z.split(',')
	p=int(z[0])
	q=int(z[1])
	if cmd=='1' or cmd=='union':
		obj.union(p,q)
		print 'union %s and %s' %(p,q)
		print obj.arr
	elif cmd=='2' or cmd=='connected':
		if obj.connected(p,q):
			print 'obj %s is connected to obj %s'%(p,q)
		else:
			print 'obj %s is not conencted to %s'%(p,q)
	else:
		print 'continue'


	
			
