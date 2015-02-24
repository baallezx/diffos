import json
import pprint

# purely a junk file that I completley forgot the purpose of.

class a(object):
	def __init__(self,b,c,d):
		self.b = b
		self.c = c
		self.d = d

	def mold_d(self):
		self.d = str(self.d) * 89

	def printer(self):
		print self.__dict__

#	def __hash__(self):
#		pass
	def __str__(self):
		return '%s(%r)' % (self.__class__, str(self.b)+str(self.c)+str(self.d))
	def __repr__(self):
		return '%s(%r)' % (self.__class__, str(self.b)+str(self.c)+str(self.d))

class a1(a):
	def __init__(self,e,f,g,this_a=None):
		if this_a == None:
			super(a1,self).__init__(None,None,None)
		else:
			if isinstance(this_a, a):
				super(a1,self).__init__(this_a.b, this_a.c, this_a.d)
		self.e = e
		self.f = f
		self.g = g

	def mold_c(self):
		self.c = str(self.c) * 34

	def mold_e(self):
		self.e = self.e + self.f + self.g

class a2(a):
	def __init__(self,h,i,j,this_a=None):
		if this_a == None:
			super(a2,self).__init__(None,None,None)
		else:
			if isinstance(this_a, a):
				super(a2,self).__init__(this_a.b, this_a.c, this_a.d)
		self.h = h
		self.i = i
		self.j = j

	def mold_b(self):
		self.b = str(self.b) * 22

	def mold_j(self):
		self.j = self.j + self.h + self.i

class a3(a2):
	def __init__(self,a,a1,a2,k,l,m):
		self.a = a
		self.a1 = a1
		self.a2 = a2
		self.k = k
		self.l = l
		self.m = m

def all_strings(d):
	for k,v in d.items():
		dk = str(k)

if __name__ == "__main__":
	pp = pprint.PrettyPrinter(indent=4)
	this_a = a(1, 2, 3)
	this_a1 = a1(45, 56, 67, this_a)
	this_a2 = a2(987, 876, 765, this_a)
	print "\n\n\t-- before --\n\n"
	this_a.printer()
	this_a1.printer()
	this_a2.printer()
	this_a.mold_d()
	this_a1.mold_c()
	this_a1.mold_e()
	this_a2.mold_d()
	this_a2.mold_b()
	this_a2.mold_j()
	print "\n\n\t-- after --\n\n"
	this_a.printer()
	this_a1.printer()
	this_a2.printer()
	print "\n\n\t-- done --\n\n"
	this_a.__repr__()
	this_a
	print this_a
	print "\n\n\t-- redo --\n\n"
	this_a3 = a3(this_a,this_a1,this_a2,range(16),{"#$%":"^%&88786  **","  **  ":{"noob":{1:range(99)}}},"lpoo  <->  oopl")
	print "\n\n\t-- new class --\n\n"
	print this_a3.__dict__
	pp.pprint(this_a3.__dict__)
	print "\n\n\t-- now done --\n\n"
