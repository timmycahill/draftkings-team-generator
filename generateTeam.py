import pandas as pd
import numpy as np
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
	flexs.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))

flexs = rbs + wrs + tes

for index, row in dstDf.iterrows():
	dsts.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))

bestTeam = Team()
currentTeam = Team()

for qb in qbs:
	if currentTeam.get_qb_rem() <= 0 or currentTeam.get_remaining_salary() < QB_FILTER_PRICE:
		break
	currentTeam.draft_qb(qb)

for rb in rbs:
	if currentTeam.get_rb_rem() <= 0 or currentTeam.get_remaining_salary() < RB_FILTER_PRICE:
		break
	currentTeam.draft_rb(rb)

for wr in wrs:
	if currentTeam.get_wr_rem() <= 0 or currentTeam.get_remaining_salary() < WR_FILTER_PRICE:
		break
	currentTeam.draft_wr(wr)

for te in tes:
	if currentTeam.get_te_rem() <= 0 or currentTeam.get_remaining_salary() < TE_FILTER_PRICE:
		break
	currentTeam.draft_te(te)

for flex in flexs:
	if currentTeam.get_flex_rem() <= 0 or currentTeam.get_remaining_salary() < FLEX_FILTER_PRICE:
		break
	currentTeam.draft_flex(flex)

for dst in dsts:
	if currentTeam.get_dst_rem() <= 0 or currentTeam.get_remaining_salary() < DST_FILTER_PRICE:
		break
	currentTeam.draft_dst(dst)

# Print lineup and projected points
print("Lineup:\n" + currentTeam.get_lineup())
print("Projected points: " + str(currentTeam.get_projected_points()))
print("Remaining Salary: $" + str(currentTeam.get_remaining_salary()))