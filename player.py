cl ass Player:
	def __init__(self, name, position, ppg, salary):
		self.name = name
		self.position = position
		self.ppg = ppg
		self.salary = salary

	def get_name(self):
		return self.name

	def get_position(self):
		return self.position

	def get_ppg(self):
		return self.ppg

	def get_salary(self):
		return self.salary