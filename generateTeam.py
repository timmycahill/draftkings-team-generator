import pandas as pd
import numpy as np

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
qb = df[df.Position == "QB"]
rb = df[df.Position == "RB"]
wr = df[df.Position == "WR"]
te = df[df.Position == "TE"]
dst = df[df.Position == "DST"]

print(wr.tail())

# Filter skill positions by price
qb = qb[qb.Salary >= QB_FILTER_PRICE]
rb = rb[rb.Salary >= RB_FILTER_PRICE]
wr = wr[wr.Salary >= WR_FILTER_PRICE]
te = te[te.Salary >= TE_FILTER_PRICE]

print(wr.tail())