import numpy as np
import random
import pandas as pd
from pandas_datareader import data as wb
from datetime import date
import matplotlib.pyplot as plt
############################################

today = date.today()
#a = np.array([[0,1,2,3,4],[5,6,7,8,9]])
#ser = pd.Series(np.random.random(5), name = "column 01")

Company_array = ["PG","T","F"]
new_data = pd.DataFrame()
#for t in Company_array:
    #new_data[t] = wb.DataReader(t, data_source = "yahoo", start="2000-1-1", end="2001-1-10")["Close"]

PG = wb.DataReader("PG", data_source = "yahoo", start="2010-1-1", end=today)


########################
#PG.to_csv("PG.csv")
#mydata = pd.read_csv("PG.csv", index_col= "Date")
#print(mydata)

##########

PG["simple return"]=(PG["Adj Close"]/PG["Adj Close"].shift(1))-1
#print(PG["simple return"])
PG["simple return"].to_csv("PG_Simple.csv")
PG["simple return"].plot(figsize=(8,5))

#################
PG["log return"]=np.log((PG["Adj Close"]/PG["Adj Close"].shift(1)))
#PG["log return"].plot(figsize=(8,5))
#plt.show()
#log return by year
#log_return_a = PG["log return"].mean()*250


#####################
Company_array = ["PG","MSFT","F","GE"]
for t in Company_array:
    new_data[t] = wb.DataReader(t, data_source = "yahoo", start="2000-1-1", end="2020-1-10")["Close"]
print(new_data)
#get first row
print(new_data/new_data.iloc[0]*100)
returns = (new_data/new_data.shift(-1))-1
annual_returns = returns.mean()*250
weights = np.array([0.25,0.25,0.25,0.25])
print(returns)
np.dot(annual_returns,weights)
print(np.dot(annual_returns,weights))

#(new_data/new_data.iloc[0]*100).plot(figsize=(8,5))
#((new_data["PG"]/new_data["PG"].shift(-1))-1).plot(figsize=(8,5))

plt.show()