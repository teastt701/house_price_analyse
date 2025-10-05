import pandas as pd
import replace
import cn2an

df = pd.read_csv('汐止.csv')


df[["f", "tf"]] = df["f"].str.extract(r"(\s+)層/(\s+)層")
print(df[["f", "tf"]])

"""
id_column = df.pop("id")
df.insert(0, "id", id_column)

df[["room","living","toilet"]] = df["v"].str.extract(r"(?:(\d+)房)?(?:(\d+)廳)?(?:(\d+)衛)?")
df[["room","living","toilet"]] = df[["room","living","toilet"]].astype("Int64")

df[["b"]] = df[["b"]].replace(
    { 
        "住宅大樓(11層含以上有電梯)": "1",
        "公寓(5樓含以下無電梯)": "2",
        "透天厝": "3",
        "華廈(10層含以下有電梯)": "4",
    }
)

df[["el"]] = df[["el"]].replace(
    {
        "有": "1",
        "無": "0",
    }
)

df["AA"] = df["AA11"].combine_first(df["AA12"])
df[["AA"]] = df[["AA"]].replace(
    {
        "住": "1",
        "6": "1",
        "其他": "1",
        "商": "2",
        "農": "3",
        "工": "4",
        "丙種建築用地": "5",
        "乙種建築用地": "5",
    }
).fillna(0)

AA_column = df.pop("AA")
df.insert(1, "AA", AA_column)

df.drop(
    [
        "AA11", "AA12", "a", "bn", "city", "commid", 
        "cp", "e", "es", "fi",
        "lat", "lon", "m", "mark",
        "msg", "note", "parkmain", "pimg",
        "pu", "punit", "r", "reid",
        "s", "sq", "t", "town", "tp", 
        "tunit", "type", "unit", "v"
    ], 
    axis = 1, inplace = True)

df.to_csv("汐止_clean.csv", encoding = "utf-8", index = False)
"""