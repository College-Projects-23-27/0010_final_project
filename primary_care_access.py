import pandas as pd
import fpsnippets

data = pd.read_csv("data-primary-care-access-facilities.csv")

neigherhoods = {}

for i in range(len(data)):
    print(data[i])