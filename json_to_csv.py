import pandas as pd
import json

with open("汐止.json", "r", encoding = "utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_csv("汐止.csv", encoding = "utf-8", index=False)