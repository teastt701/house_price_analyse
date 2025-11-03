import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

clean_data = pd.read_csv("汐止_clean.csv")

bins = [0, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, float("inf")]
labels = ["0~19", "20~29", "30~39", "40~49", "50~59", "60~69", "70~79", "80~89", "90~99", "100"]
clean_data["price_range"] = pd.cut(clean_data["p"], bins=bins, labels=labels, right=False)

def normal_distribution(df): #分佈
    sns.displot(df["price_range"])
    plt.xticks(rotation = 45)
    plt.show()
    sns.displot(df["p"], kde = True)
    plt.xticks(rotation = 45)
    plt.show()

def correlation_heatmap(df):    #檢查所有項之間的相關係數
    df = df.drop("price_range", axis = 1)
    correlation_matrix = df.corr().round(2)
    p_corr = correlation_matrix[["p"]].sort_values(by = "p")
    composite_corr = correlation_matrix.loc[:, ["p", "g", "el", "bs", "AA", "room", "toilet", "tf", "k"]]
    p_corr = composite_corr.sort_values(by = "p", ascending = True)
    print(p_corr)
    sns.heatmap(data = correlation_matrix, annot = True)
    plt.show()

def R2(df):
    column = ["g", "el", "bs", "AA", "room", "toilet", "tf", "k"]
    x = df[column]
    y = df["p"]

    x = StandardScaler().fit_transform(x)   #標準化

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 10)
    
    #reg = DecisionTreeRegressor()
    #reg = GradientBoostingRegressor()
    reg = RandomForestRegressor()
    #reg = KNeighborsRegressor()
    #reg = XGBRegressor()

    reg.fit(x_train,y_train)

    reg.predict(x_test)

    print("R2: ", reg.score(x_test, y_test))

normal_distribution(clean_data)
correlation_heatmap(clean_data)
R2(clean_data)
