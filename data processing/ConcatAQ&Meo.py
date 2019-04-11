import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

aqstation = pd.read_csv("D:/KDD2018/Beijing_AirQuality_Stations_copy.csv")
meo = pd.read_csv("D:/KDD2018/beijing_17_18_meo.csv")
meostation = meo.drop_duplicates(subset=['station_id'],keep='first').reset_index(drop=True)

l = []
# Classify meostation into aqstation...

for i in range(len(aqstation)):

 station = meostation['station_id'][(((aqstation['longitude'][i]-meostation['longitude'])**2+(aqstation['latitude'][i]-meostation['latitude'])**2)**(0.5)).idxmin()]
 l.append(station)

# print(len(l))
aqstation['station_id'] = l

del meostation['longitude']
del meostation['latitude']

aqstation = pd.merge(aqstation, meostation, how='left', on='station_id')
print(aqstation.head(10))
