import pandas as pd
import numpy as np
import copy
from player import Player
from team import Team

# Test function
def print_lineup(t):
	print(t.get_lineup())
	print(t.get_remaining_salary())
	print("\n\n\n")


# Define constants
STARTING_SALARY = 50000
QB_FILTER_PRICE = 5000
RB_FILTER_PRICE = 4100
WR_FILTER_PRICE = 3500
TE_FILTER_PRICE = 3000
if RB_FILTER_PRICE < WR_FILTER_PRICE and RB_FILTER_PRICE < TE_FILTER_PRICE:
	FLEX_FILTER_PRICE = RB_FILTER_PRICE
elif WR_FILTER_PRICE < TE_FILTER_PRICE:
	FLEX_FILTER_PRICE = WR_FILTER_PRICE
else:
	FLEX_FILTER_PRICE = TE_FILTER_PRICE
DST_FILTER_PRICE = 2000


# Read in player data
df = pd.read_csv("C:/Users/tcahi/Downloads/DKSalaries.csv")


# Clean up dataframe
df = df[["Name", "Position", "AvgPointsPerGame", "Salary"]]


# Create a dataframe for each position
qbDf = df[df.Position == "QB"]
rbDf = df[df.Position == "RB"]
wrDf = df[df.Position == "WR"]
teDf = df[df.Position == "TE"]
dstDf = df[df.Position == "DST"]


# Filter skill positions by price
qbDf = qbDf[qbDf.Salary >= QB_FILTER_PRICE]
rbDf = rbDf[rbDf.Salary >= RB_FILTER_PRICE]
wrDf = wrDf[wrDf.Salary >= WR_FILTER_PRICE]
teDf = teDf[teDf.Salary >= TE_FILTER_PRICE]


# Create a list of players objects for each position group
qbs = []
rbs = []
wrs = []
tes = []
flexs = []
dsts = []

for index, row in qbDf.iterrows():
	qbs.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))

for index, row in rbDf.iterrows():
	rbs.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))

for index, row in wrDf.iterrows():
	wrs.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))

for index, row in teDf.iterrows():
	tes.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))

flexs = rbs + wrs + tes

for index, row in dstDf.iterrows():
	dsts.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))


# Generate team
bestTeam = Team()

# Draft qb
for qb in qbs:
	qb1 = Team()
	qb1.draft_qb(qb)

	# Draft RB1
	for i in range(len(rbs)):
		rb1 = copy.deepcopy(qb1)
		rb1.draft_rb(rbs[i])

		# Draft RB2
		for j in range(i + 1, len(rbs)):
			rb2 = copy.deepcopy(rb1)
			rb2.draft_rb(rbs[j])

			# Draft WR1
			for k in range(len(wrs)):
				wr1 = copy.deepcopy(rb2)
				wr1.draft_wr(wrs[k])

				# Draft WR2
				for l in range(k + 1, len(wrs)):
					wr2 = copy.deepcopy(wr1)
					wr2.draft_wr(wrs[l])

					# Draft WR3
					for m in range(l + 1, len(wrs)):
						wr3 = copy.deepcopy(wr2)
						wr3.draft_wr(wrs[m])

						# Draft TE
						for te in tes:
							te1 = copy.deepcopy(wr3)
							te1.draft_te(te)

							# Draft Flex
							for flex in flexs:
								flex1 = copy.deepcopy(te1)
								flex1.draft_flex(flex)

								# Draft DST
								for dst in dsts:
									dst1 = copy.deepcopy(flex1)
									dst1.draft_dst(dst)

									# Compare team with best team
									if dst1.get_projected_points() > bestTeam.get_projected_points():
										bestTeam = copy.deepcopy(dst1)

										# Print lineup and projected points of best team
										print("\n\nNew Best Team Found!\n")
										print("Lineup:\n" + bestTeam.get_lineup())
										print("Projected points: " + str(bestTeam.get_projected_points()))
										print("Remaining Salary: $" + str(bestTeam.get_remaining_salary()))
									

# Print lineup and projected points of best team
print("\n\nBest team:\n")
print(bestTeam.get_lineup())
print("Projected points: " + str(bestTeam.get_projected_points()))
print("Remaining Salary: $" + str(bestTeam.get_remaining_salary()))