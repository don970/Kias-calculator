class Factor:

	def __init__(self, mode, factor):
		self.i = None
		self.complete = None
		if mode == 0:
			self.factor(factor, 0)

	def factor(self, a0, mode):
		self.i = []
		if mode == 0:
			a0 = int(a0)
			for i in range(1, a0 + 1):
				if a0 % i == 0:
					b = a0 % i
					answer = f"{str(a0)} % {str(i)} = {str(b)}"
					self.i.append(i)
					self.complete = True
		return self.i

