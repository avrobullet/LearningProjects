import os
import csv
import pandas as pd

path = "D:/mutualaid.csv"
df = pd.read_csv(path)
#print(df)

with open(path, 'r', newline='', encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile, quotechar='|')
    print("CSV data row: %s", len(csv_reader))
    #print("CSV data column: %s", % len(csv_reader))