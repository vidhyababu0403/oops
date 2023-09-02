class C1():
	def m(self):
		print("zaali")
	
class C2(C1):
	def m(self):
		print("kutty")

class C3(C1):
	def m(self):
		print("meee")	
	
class C4(C2, C3):
	def m(self):
		print("upt")
		C2.m(self)
		C3.m(self)
		C1.m(self)

obj = C4()
obj.m()
