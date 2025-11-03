import pandas as pd
import replace
import cn2an

df = pd.read_csv('汐止.csv')

mask = ~df["f"].str.match(r"(.+)層/(.+)層")
mask2 = df["f"].str.contains(r",")
mask3 = df["f"].str.contains(r"地")

print(mask.value_counts())
df = df[~mask]
df = df[~mask2]
df = df[~mask3]
#此段過濾不符合標準格式的資料以方便處理

df[["f", "tf"]] = df["f"].str.extract(r"(.+)層/(.+)層")

df["f"] = df["f"].apply(cn2an.cn2an)
df["tf"] = df["tf"].apply(cn2an.cn2an)

df["bs"] = df["bs"].astype(str).str.replace('"', '', regex=False).str.replace(",", "", regex=False).str.replace("%", "", regex=False)
df["bs"] = pd.to_numeric(df["bs"], errors="coerce") / 100

df["p"] = df["p"].astype(str).str.replace('"', '', regex=False).str.replace(",", "", regex=False)
df["p"] = pd.to_numeric(df["p"], errors="coerce")
#過濾f、bs、p的資料

df[["room","living","toilet"]] = df["v"].str.extract(r"(?:(\d+)房)?(?:(\d+)廳)?(?:(\d+)衛)?")
df[["room","living","toilet"]] = df[["room","living","toilet"]].astype("Int64")
#將房屋內部資訊切割

df[["b"]] = df[["b"]].replace(
    { 
        "住宅大樓(11層含以上有電梯)": "1",
        "公寓(5樓含以下無電梯)": "2",
        "透天厝": "3",
        "華廈(10層含以下有電梯)": "4",
    }
)
#轉換b的資料成為數字

df[["el"]] = df[["el"]].replace(
    {
        "有": "1",
        "無": "0",
    }
)
#轉換el的資料成為數字

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
#轉換AA的資料成為數字

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
#刪除多餘的column   

id_column = df.pop("id")
df.insert(0, "id", id_column)

p_column = df.pop("p")
df.insert(14, "p", p_column)

if df.isna().any(axis = 1).sum() > 0:
    df = df.dropna()

print(df.isnull().sum())
print(df.duplicated().sum())

df.to_csv("汐止_clean.csv", encoding = "utf-8", index = False)