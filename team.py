from player import Player

MAX_QBS = 1
MAX_RBS = 2
MAX_WRS = 3
MAX_TE = 1
MAX_FLEX = 1
MAX_DST = 1

class Team:
	def __init__(self):
		self.remainingSalary = 50000
		self.qb = []
		self.rbs = []
		self.wrs = []
		self.te = []
		self.flex = []
		self.dst = []

	def draft_qb(self, qb):
		if qb.get_salary() <= self.remainingSalary:
			self.qb.append(qb)
			self.remainingSalary -= qb.get_salary()

	def get_qb_rem(self):
		return MAX_QBS - len(self.qb)

	def draft_rb(self, rb):
		if rb.get_salary() <= self.remainingSalary:
			self.rbs.append(rb)
			self.remainingSalary -= rb.get_salary()

	def get_rb_rem(self):
		return MAX_RBS - len(self.rbs)

	def draft_wr(self, wr):
		if wr.get_salary() <= self.remainingSalary:
			self.wrs.append(wr)
			self.remainingSalary -= wr.get_salary()

	def get_wr_rem(self):
		return MAX_WRS - len(self.wrs)

	def draft_te(self, te):
		if te.get_salary() <= self.remainingSalary:
			self.te.append(te)
			self.remainingSalary -= te.get_salary()

	def get_te_rem(self):
		return MAX_TE - len(self.te)

	def draft_flex(self, flex):
		if flex.get_salary() <= self.remainingSalary:
			self.flex.append(flex)
			self.remainingSalary -= flex.get_salary()

	def get_flex_rem(self):
		return MAX_FLEX - len(self.flex)

	def draft_dst(self, dst):
		if dst.get_salary() <= self.remainingSalary:
			self.dst.append(dst)
			self.remainingSalary -= dst.get_salary()

	def get_dst_rem(self):
		return MAX_DST - len(self.dst)

	def get_lineup(self):
		lineup = "      Player                        Price       Points\n"
		lineup += "----------------------------------------------------------\n"

		for player in self.qb:
			lineup += "  QB: {0:<30s}${1:<10} {2:<}\n".format(player.get_name(), player.get_salary(), player.get_ppg())
		for player in self.rbs:
			lineup += "  RB: {0:<30s}${1:<10} {2:<}\n".format(player.get_name(), player.get_salary(), player.get_ppg())
		for player in self.wrs:
			lineup += "  WR: {0:<30s}${1:<10} {2:<}\n".format(player.get_name(), player.get_salary(), player.get_ppg())
		for player in self.te:
			lineup += "  TE: {0:<30s}${1:<10} {2:<}\n".format(player.get_name(), player.get_salary(), player.get_ppg())
		for player in self.flex:
			lineup += "FLEX: {0:<30s}${1:<10} {2:<}\n".format(player.get_name(), player.get_salary(), player.get_ppg())
		for player in self.dst:
			lineup += " DST: {0:<30s}${1:<10} {2:<}\n".format(player.get_name(), player.get_salary(), player.get_ppg())

		return lineup

	def get_projected_points(self):
		points = 0

		for player in self.qb:
			points += player.get_ppg()
		for player in self.rbs:
			points += player.get_ppg()
		for player in self.wrs:
			points += player.get_ppg()
		for player in self.te:
			points += player.get_ppg()
		for player in self.flex:
			points += player.get_ppg()
		for player in self.dst:
			points += player.get_ppg()

		return points

	def get_remaining_salary(self):
		return self.remainingSalary

	def is_full(self):
		return self.get_qb_rem() == 0 and self.get_rb_rem() == 0 and self.get_wr_rem() == 0 and self.get_te_rem() == 0 and self.get_flex_rem() == 0 and self.get_dst_rem() == 0