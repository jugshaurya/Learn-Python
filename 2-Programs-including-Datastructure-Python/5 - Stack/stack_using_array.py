class StackArr :

	def __init__(self):
		self.arr = []

	def push(self ,data):
		self.arr.append(data)

	def pop(self):
		if self.arr == []:
			return None

		data = self.arr[-1]
		self.arr.pop()
		return data

	def top(self):
		if self.arr == []:
			return None
		return self.arr[-1]

	def size(self):
		return len(self.arr)

	def isEmpty(self):
		return self.arr == []

