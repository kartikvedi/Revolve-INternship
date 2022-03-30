import pandas as pd
flight = pd.read_csv("backend-engineer/data/flights.csv") 
airport = pd.read_csv("backend-engineer/data/airports.csv")
plane = pd.read_csv("backend-engineer/data/planes.csv")

## how many total number of days does the flights table cover?
def get_ans1():
    flight["date"] = flight["day"].astype(str) +"-"+flight["month"].astype(str) + "-" + flight["year"].astype(str)
    flight["date"] = pd.to_datetime(flight["date"])
    return flight["date"].nunique()


## how many departure cities (not airports) does the flights database cover?
def get_ans2():
    return pd.merge(flight,airport,left_on = "origin",right_on="IATA_CODE",how="left")["CITY"].nunique()

## which airplane manufacturer incurred the most delays in the analysis period?
def get_ans4():
    d = plane[["tailnum","manufacturer"]].merge(flight,on="tailnum",how="right")
    delays = d.groupby("manufacturer").apply(lambda x : (x["dep_delay"] + x["arr_delay"]).sum())
    return delays.idxmax()

## which are the two most connected cities?
def get_ans5():
    airport_map = dict(zip(airport["IATA_CODE"],airport["CITY"]))
    source = flight["origin"].map(airport_map)
    dest = flight["dest"].map(airport_map)
    path = source+" => "+dest
    return path.value_counts().idxmax()

print(get_ans1())
