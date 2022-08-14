import pandas as pd

conditions = ["confirmed", "death", "recovered"]

daily_df = pd.read_csv("data/daily_report.csv")

total_df = daily_df[["Confirmed","Deaths","Recovered"]]
total_df = total_df.sum().reset_index(name="sum")
total_df = total_df.rename(columns={"index":"condition"})

country_df = daily_df[["Country_Region", "Confirmed","Deaths", "Recovered"]]
countries_df = country_df.groupby("Country_Region").sum().sort_values(by="Confirmed", ascending=False).reset_index()

#전세계 날짜별 확진, 사망, 완치 데이터
def make_global_df(condition):
    def make_df(condition):
        df = pd.read_csv(f"data/time_{condition}.csv")
        df = df.drop(df.columns[:4], axis =1).sum().reset_index(name=condition)
        df = df.rename(columns={"index":"date"})
        return df
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df

global_df = make_global_df(conditions)

# 나라별 확진, 사망, 완치 데터
def make_country_df(country):
    def make_df(condition):
        df = pd.read_csv(f"data/time_{condition}.csv")
        df = df.loc[df["Country/Region"] == country]
        df = df.drop(df.columns[:4], axis = 1).sum().reset_index(name=condition)
        df = df.rename(columns={"index":"date"})
        return df
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df
