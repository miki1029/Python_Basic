#===============================================================================
# 제 13 장 클래스
#===============================================================================

#===============================================================================
# 13.1 파이썬 클래스란
#===============================================================================

# 클래스와 이름공간, 상속, 연산자 중복, 용어

#===============================================================================
# 13.2 클래스 정의와 인스턴스 객체의 생성
#===============================================================================

#------------------------------------------------------------------------------ 
class Simple:
	pass

print(Simple)
#__main__.Simple
#<class '__main__.Simple'>

print(Simple.__bases__)
#()
#(<class 'object'>,)
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# 동적으로 외부에서 멤버를 생성할 수 있다.(인스턴스 멤버)
s1 = Simple()
s2 = Simple()
print(s1)
#<__main__.Simple instance at 0x7fad18785ef0>
#<__main__.Simple object at 0x7fad18785ef0>

s1.stack = []
s1.stack.append(1)
s1.stack.append(2)
s1.stack.append(3)
print(s1.stack)
#[1, 2, 3]
print(s1.stack.pop())
#3
print(s1.stack.pop())
#2
print(s1.stack)
#[1]
#print(s2.stack)
#AttributeError: Simple instance has no attribute 'stack'
del s1.stack
#------------------------------------------------------------------------------ 

#===============================================================================
# 13.3 메소드의 정의와 호출
#===============================================================================

#------------------------------------------------------------------------------ 
class MyClass:
	def set(self, v):
		self.value = v;
	def get(self):
		return self.value

# 언바운드 메소드 호출(Unbound Method Call)
c = MyClass()
print(MyClass.set)
#<unbound method MyClass.set>
#<function set at 0x1bde958>
MyClass.set(c, 'egg')
print(MyClass.get(c))
#egg

# 바운드 메소드 호출(Bound Method Call)
c = MyClass()
print(c.set)
#<bound method MyClass.set of <__main__.MyClass instance at 0x7fb658294440>>
#<bound method MyClass.set of <__main__.MyClass object at 0x7fb658294440>>
c.set('egg')
print(c.get())
#egg
#------------------------------------------------------------------------------ 


#===============================================================================
# 13.4 클래스 멤버와 인스턴스 멤버
#===============================================================================

#------------------------------------------------------------------------------ 
# 클래스 멤버는 클래스 이름 공간에 생성된다.
# 인스턴스 멤버는 인스턴스 객체의 이름 공간에 생성된다.
# 클래스 멤버는 모든 인스턴스 객체에 의해서 공유될 수 있다.
# 인스턴스 멤버는 각각의 인스턴스 객체 내에서만 참조된다.
class Var:
	c_mem = 100			# 클래스 멤버 : Var.c_mem 혹은 instance.c_mem
	def f(self):
		self.i_mem = 200	# 인스턴스 멤버 : instance.i_mem
	def g(self):
		return self.i_mem, self.c_mem

# 클래스 멤버 접근 : 클래서.멤버, 인스턴스.멤버
print(Var.c_mem)
#100
v1 = Var()
print(v1.c_mem)
#100

# 멤버 접근 순서 : 먼저 인스턴스 멤버를 참조한 후 존재하지 않으면 클래스 멤버를 참조한다.
v2 = Var()
print(v1.c_mem)
#100
print(v2.c_mem)
#100
v1.c_mem = 50; # **멤버접근순서**에 의해서 인스턴스 멤버 c_mem을 생성한다.
print(v1.c_mem)
#50
print(v2.c_mem)
#100
print(Var.c_mem)
#100
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# Python3
# 사용 가능한 멤버 고정하기 : __slots__
class Person:
	__slots__ = ['name', 'tel']

m1 = Person()
m1.name = '이강성'
m1.tel = '5284'
#m1.address = '서울'
#AttributeError: 'Person' object has no attribute 'address'
# Python3 : __slots__에 있는 속성만 사용할 수 있다.
#------------------------------------------------------------------------------ 