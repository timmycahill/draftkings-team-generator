import pandas as pd
import numpy as np
import copy
from player import Player
from team import Team


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


# Read in inactive players
INACTIVES = []
f = open("inactivePlayers.txt", "r")
for player in f:
	print(player[0:len(player) - 1])
	INACTIVES.append(player[0:len(player) -1])
f.close()

# Do teams to ignore
BAD_TEAMS = ["NYJ"]


# Read in player data
df = pd.read_csv("C:/Users/tcahi/Downloads/DKSalaries.csv")


# Clean up dataframe
df = df[["Name", "Position", "AvgPointsPerGame", "Salary", "TeamAbbrev"]]


# Filter out inactives
df = df[~df.Name.isin(INACTIVES)]
df = df[~df.TeamAbbrev.isin(BAD_TEAMS)]

# Create a dataframe for each position
qbDf = df[df.Position == "QB"]
rbDf = df[df.Position == "RB"]
wrDf = df[df.Position == "WR"]
teDf = df[df.Position == "TE"]
dstDf = df[df.Position == "DST"]


# Filter skill positions by price
qbDf = qbDf[qbDf.AvgPointsPerGame >= 15]
rbDf = rbDf[rbDf.AvgPointsPerGame >= 15]
wrDf = wrDf[wrDf.AvgPointsPerGame >= 15]
teDf = teDf[teDf.AvgPointsPerGame >= 10]
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

for index, row in dstDf.iterrows():
	dsts.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))


# Print list lengths
print("QBS: " + str(len(qbs)))
print("RBS: " + str(len(rbs)))
print("WRS: " + str(len(wrs)))
print("TES: " + str(len(tes)))
print("FLEXS: " + str(len(rbs) + len(wrs) + len(tes)))
print("DSTS: " + str(len(dsts)))

totalPossibilities = len(qbs) * len(rbs) * len(wrs) * len(tes) * (len(rbs) + len(wrs) + len(tes)) * len(dsts)
print("Total possibile teams: " + str(totalPossibilities))


# Generate team
bestTeam = Team()

# Draft qb
for qb in qbs:
	qb1 = Team()
	qb1.draft_qb(qb)
	print("Checking teams with QB " + qb.get_name() + "...")

	# Draft RB1
	for i in range(len(rbs)):
		rb1 = copy.deepcopy(qb1)
		rb1.draft_rb(rbs[i])
		print("Checking teams with RB1 " + rbs[i].get_name() + "...")

		# Draft RB2
		for j in range(i + 1, len(rbs)):
			rb2 = copy.deepcopy(rb1)
			rb2.draft_rb(rbs[j])
			print("Checking teams with RB2 " + rbs[j].get_name() + "...")

			# Draft WR1
			for k in range(len(wrs)):
				wr1 = copy.deepcopy(rb2)
				wr1.draft_wr(wrs[k])

				# Draft WR2
				for l in range(k + 1, len(wrs)):
					wr2 = copy.deepcopy(wr1)
					wr2.draft_wr(wrs[l])

					# Draft WR3
					if wr2.get_remaining_salary() > WR_FILTER_PRICE:
						for m in range(l + 1, len(wrs)):
							if wrs[m].get_salary() < wr2.get_remaining_salary():
								wr3 = copy.deepcopy(wr2)
								wr3.draft_wr(wrs[m])

								# Draft TE
								if wr3.get_remaining_salary() > TE_FILTER_PRICE:
									for n in range(len(tes)):
										if tes[n].get_salary() < wr3.get_remaining_salary():
											te1 = copy.deepcopy(wr3)
											te1.draft_te(tes[n])

											# Draft Flex WR
											if te1.get_remaining_salary() > WR_FILTER_PRICE:
												for o in range(m + 1, len(wrs)):
													if wrs[o].get_salary() < te1.get_remaining_salary():
														flex1 = copy.deepcopy(te1)
														flex1.draft_flex(wrs[o])

														# Draft DST
														for dst in dsts:
															dst1 = copy.deepcopy(flex1)
															dst1.draft_dst(dst)

															# Compare team with best team
															if dst1.is_full() and dst1.get_projected_points() > bestTeam.get_projected_points():
																bestTeam = copy.deepcopy(dst1)

																# Print lineup and projected points of best team
																print("\n\nNew Best Team Found!\n")
																print("Lineup:\n" + bestTeam.get_lineup())
																print("Projected points: " + str(bestTeam.get_projected_points()))
																print("Remaining Salary: $" + str(bestTeam.get_remaining_salary()))

											# Draft Flex RB
											if te1.get_remaining_salary() > RB_FILTER_PRICE:
												for p in range(j + 1, len(rbs)):
													if rbs[p].get_salary() < te1.get_remaining_salary():
														flex1 = copy.deepcopy(te1)
														flex1.draft_flex(rbs[p])

														# Draft DST
														for dst in dsts:
															dst1 = copy.deepcopy(flex1)
															dst1.draft_dst(dst)

															# Compare team with best team
															if dst1.is_full() and dst1.get_projected_points() > bestTeam.get_projected_points():
																bestTeam = copy.deepcopy(dst1)

																# Print lineup and projected points of best team
																print("\n\nNew Best Team Found!\n")
																print("Lineup:\n" + bestTeam.get_lineup())
																print("Projected points: " + str(bestTeam.get_projected_points()))
																print("Remaining Salary: $" + str(bestTeam.get_remaining_salary()))

											# Draft Flex TE
											if te1.get_remaining_salary() > TE_FILTER_PRICE:
												for q in range(n + 1, len(tes)):
													if tes[q].get_salary() < te1.get_remaining_salary():
														flex1 = copy.deepcopy(te1)
														flex1.draft_flex(tes[q])

														# Draft DST
														for dst in dsts:
															dst1 = copy.deepcopy(flex1)
															dst1.draft_dst(dst)

															# Compare team with best team
															if dst1.is_full() and dst1.get_projected_points() > bestTeam.get_projected_points():
																bestTeam = copy.deepcopy(dst1)

																# Print lineup and projected points of best team
																print("\n\nNew Best Team Found!\n")
																print("Lineup:\n" + bestTeam.get_lineup())
																print("Projected points: " + str(bestTeam.get_projected_points()))
																print("Remaining Salary: $" + str(bestTeam.get_remaining_salary()))
		# Print lineup and projected points of best team
		print("\n\nCurrent Best Team:\n")
		print(bestTeam.get_lineup())
		print("Projected points: " + str(bestTeam.get_projected_points()))
		print("Remaining Salary: $" + str(bestTeam.get_remaining_salary()))
									

# Print lineup and projected points of best team
print("\n\nBest team:\n")
print(bestTeam.get_lineup())
print("Projected points: " + str(bestTeam.get_projected_points()))
print("Remaining Salary: $" + str(bestTeam.get_remaining_salary()))