#!/usr/bin/env python3
class Stack:
	__stack=[]
	top=0
	def __init__(self,num):
		for i in range(0,num):
			self.__stack.append(0)
		self.top=0	
	def pop(self):
		if self.isEmpty():
			return False
		self.top-=1
		num=self.__stack[self.top]
		self.__stack[self.top]=0
		return num
	def push(self,num):
		self.__stack[self.top]=num
		self.top+=1
	def isEmpty(self):
		if self.top==0:
			return True
		return False
	def showStack(self):
		return self.__stack
size=int(input('input your statck size: '))
s=Stack(size)
flag=True
while flag:
	cmd=input('your operation code(1:pop,2:push,3:show,4:exit):')
	if cmd=='push' or cmd=='2':
		num=int(input("input your push value: "))
		s.push(num)
	elif cmd=='pop' or cmd=='1':
		print(s.pop())
	elif cmd=='show' or cmd=='3':
		print(s.showStack())
	elif cmd=='exit' or cmd=='4':
		flag=False
	else:
		print('continue')
	
	
				
		
