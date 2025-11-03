import pandas as pd
import numpy as nd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler

df = pd.read_csv('汽車車型資料檔.csv')

df_z = StandardScaler().fit_transform(df[["重量"]])
df_Mm = MinMaxScaler().fit_transform(df[["重量"]])
df_Max = MaxAbsScaler().fit_transform(df[["重量"]])
df_Ro = RobustScaler().fit_transform(df[["重量"]])

df_new = pd.DataFrame(
    {
        "z": df_z.flatten(),
        "Mm": df_Mm.flatten(),
        "Max": df_Max.flatten(),
        "Ro": df_Ro.flatten()
    }
)
df_new["重量"] = df["重量"]
df_new.to_csv("汽車重量.csv", encoding = "utf-8", index = False)
