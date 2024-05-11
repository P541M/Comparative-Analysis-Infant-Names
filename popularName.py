import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: python3 popularName.py <csv_file>")
    sys.exit(1)
filename = sys.argv[1]

df = pd.read_csv(filename)

name_counts = df.groupby('Name')['Count'].sum()

most_popular_name = name_counts.idxmax()

print("The most popular name overall is:", most_popular_name)
