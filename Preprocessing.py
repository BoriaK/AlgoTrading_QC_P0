import pandas as pd
import re
import os

# Import .csv to pandas dataframe
dataset = r'./DataSet'
df = pd.read_csv(os.path.join(dataset, "data_elonmusk.csv"), encoding='latin1')  # encoding='iso-8859-1' or
# encoding='cp1252'
# Select time and tweet columns
df = df[["Time", "Tweet"]]
# Reverse order
df = df[::-1].reset_index(drop=True)
# Remove all URLs (replace with {URL} placeholder
for i in range(0, len(df)):
    if "http" in df["Tweet"][i]:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F]))+', df["Tweet"][i])
        for url in urls:
            df["Tweet"][i] = df["Tweet"][i].replace(url, '{URL}')

df.head()

# Export dataframe to csv
df.to_csv(os.path.join(dataset, "MuskTweetsPreProcessed.csv"), index=False)
