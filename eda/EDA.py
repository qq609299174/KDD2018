import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

ap = pd.read_csv("D:/KDD2018/beijing_17_18_aq.csv")

# print(ap.shape, ap.head(5),ap.tail(5),ap.isnull().sum())
#    (311010, 8)
# stationId             utc_time  PM2.5   PM10    NO2   CO   O3  SO2
print(ap['utc_time'].dtypes)   # object
print(ap['stationId'].unique())  # 35

df1 = ap.loc[ap['stationId']=="dongsi_aq"].copy()
df1['utc_time'] =  pd.to_datetime(df1['utc_time'])
print(df1.shape,df1.head(5))
print(df1['utc_time'].dtypes)   #  datetime64[ns]


plt.plot(df1['utc_time'][-600:],df1['PM2.5'][-600:],label = "PM2.5")
# plt.plot(df1['utc_time'][100:1000],df1['PM10'][100:1000],label = "PM10")
# plt.plot(df1['utc_time'][100:1000],df1['O3'][100:1000],label = "O3")
# plt.plot(df1['utc_time'][100:1000],df1['NO2'][100:1000],label = "NO2")
# plt.plot(df1['utc_time'][100:1000],df1['SO2'][100:1000],label = "SO2")
# plt.plot(df1['utc_time'][100:1000],df1['CO'][100:1000],label = "CO")
plt.legend()
plt.show()

# df1.to_csv("D:/KDD2018/sampleAQ.csv")
meo = pd.read_csv("D:/KDD2018/beijing_17_18_meo.csv")
# print(meo.head())
# print(meo['station_id'].unique())
# print(ap['stationId'].unique())
meostation = meo.drop_duplicates(subset=['station_id'],keep='first').reset_index(drop=True)
aqstation = pd.read_csv("D:/KDD2018/Beijing_AirQuality_Stations_copy.csv")
# print(aqstation.head(5))    # 35 stations    Station ID
# print(meostation.head(5))   # 18 stations     station_id


l = []
# Classify meostation into aqstation...

for i in range(len(aqstation)):

 station = meostation['station_id'][(((aqstation['longitude'][i]-meostation['longitude'])**2+(aqstation['latitude'][i]-meostation['latitude'])**2)**(0.5)).idxmin()]
 l.append(station)

# print(len(l))
aqstation['station_id'] = l

del aqstation['longitude']
del aqstation['latitude']
del meostation['longitude']
del meostation['latitude']

aqstation = pd.merge(aqstation, meostation, how='left', on='station_id')
print(aqstation.head(10))
