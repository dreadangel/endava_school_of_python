class Power:
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, a, b):
		retval = self._arg(a, b)
		return retval ** 2


@Power
def multiply_together(a, b):
	return a * b


@Power
def sum_together(a, b):
	return a + b