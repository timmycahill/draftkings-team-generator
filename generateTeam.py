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

for index, row in dstDf.iterrows():
	dsts.append(Player(row["Name"], row["Position"], row["AvgPointsPerGame"], row["Salary"]))

bestTeam = Team()

for qb in qbs:
	currentTeam = Team()
	currentTeam.draft_qb(qb)