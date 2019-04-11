import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

sample = pd.read_csv("D:/KDD2018/sampleAQ.csv")
print(sample.shape)

# print(sample.shape,sample.head())
sample['utc_time'] =  pd.to_datetime(sample['utc_time'])
sample = sample.drop_duplicates(['utc_time'])
print(sample.shape)

sample = sample.set_index('utc_time').resample('H').fillna(method=None)
sample[['stationId']]= sample[['stationId']].ffill()
sample = sample.reset_index()
print(sample.head(),sample.shape)

print(sample.isnull().sum())

sample = sample.interpolate(method='linear')
print(sample.shape)
# plt.plot(sample['utc_time'],sample['PM2.5'],label = "PM2.5")
# plt.legend()
# plt.show()

sample['utc_time'] = sample['utc_time'].dt.strftime("%Y-%m-%d %H:%M:%S")
datetime = pd.DataFrame(sample.utc_time.str.split(' ',1).tolist(),columns=['date','time'])
sample = sample.join(datetime)
cols = sample.columns.tolist()
print(cols)

sample = sample[['stationId',  'date', 'time', 'PM2.5', 'PM10', 'NO2', 'CO', 'O3', 'SO2','utc_time']]
del sample['utc_time']
# print(sample.head(),sample.shape)

sample['date'] =  pd.to_datetime(sample['date'])

sample = sample.drop_duplicates(['date','time'])

#
# print(sample.shape)
# print(sample.isnull().sum())




#####################################################################################################################

# PM2.5


df1 = sample[['stationId',  'date', 'time', 'PM2.5']].copy()

print(df1.shape)

df1 = df1.iloc[10:9466].reset_index(drop=True)
# print(df1.head(),df1.tail())


# print(df1.drop_duplicates(['date','time']))
# print(df1.head(),df1.shape)
print(df1.shape)
df2 = df1.set_index(['stationId','time','date'])['PM2.5']\
  .unstack([0,1])\
  .rolling(len(df1),min_periods=1)\
  .mean().shift(1).bfill()\
  .unstack().rename('avgPM2.5')\
  .to_frame()\
  .join(df1.set_index(['stationId','time','date']))\
  .reset_index().sort_values(['stationId','date','time'])

df2 = df2.reset_index(drop=True)
# df2['utc_time']= pd.to_datetime(df2['date'].apply(str) + ' ' + df2['time'])    # combine 'date' and 'time'

# print(df2.head(),df2.shape)

df2 = df2.iloc[np.repeat(np.arange(len(df2)),2)].reset_index()
# df2['avgPM2.5']=df2['avgPM2.5'].shift(1)
# df2=df2[1:11]

df2['key1']=np.arange(len(df2))%2

df2['key2']=np.arange(len(df2))//48

df2 = df2.sort_values(['key2','key1'])
df2 = df2.reset_index()

# print(df2.tail(),df2.shape)

df2['avgPM2.5']=df2['avgPM2.5'].shift(24)
df2 = df2[24:18888]

del df2['level_0']
del df2['index']
del df2['key1']
del df2['key2']

df2 = df2.reset_index(drop=True)

finduPM25 = df2['PM2.5']
print(df2.head(),df2.shape)
time = pd.get_dummies(df2['time'])
time.columns = ['AggPM2.5 0','AggPM2.5 1','AggPM2.5 2','AggPM2.5 3','AggPM2.5 4','AggPM2.5 5','AggPM2.5 6','AggPM2.5 7',
                'AggPM2.5 8','AggPM2.5 9','AggPM2.5 10','AggPM2.5 11','AggPM2.5 12','AggPM2.5 13','AggPM2.5 14',
                'AggPM2.5 15','AggPM2.5 16','AggPM2.5 17','AggPM2.5 18','AggPM2.5 19','AggPM2.5 20','AggPM2.5 21',
                'AggPM2.5 22','AggPM2.5 23']
time = time.multiply(df2['avgPM2.5'], axis="index")

# print(time.head(),time.shape)
aq1 = df2.join(time)
del aq1['avgPM2.5']
del aq1['time']

print(aq1.head(),aq1.shape)
# df2['utc_time']= pd.to_datetime(df2['date'].apply(str) + ' ' + df2['time'])    # combine 'date' and 'time'

# # 先补齐日期，计算avg，合并datetime排序，计算PM10、O3,合并  可以完成
# #怎么复制交错开， 可以完成     完了就可以给每两天标记48，展开0~23，for col(i) 0~23 = 1, col(i) = pm2.5

#######################################################################################################################
# PM10


df1 = sample[['stationId',  'date', 'time', 'PM10']].copy()                                                      # 1

print(df1.shape)

df1 = df1.iloc[10:9466].reset_index(drop=True)
# print(df1.head(),df1.tail())


# print(df1.drop_duplicates(['date','time']))
# print(df1.head(),df1.shape)
print(df1.shape)                                                                                                  # 2
df2 = df1.set_index(['stationId','time','date'])['PM10']\
  .unstack([0,1])\
  .rolling(len(df1),min_periods=1)\
  .mean().shift(1).bfill()\
  .unstack().rename('avgPM10')\
  .to_frame()\
  .join(df1.set_index(['stationId','time','date']))\
  .reset_index().sort_values(['stationId','date','time'])                                                         # 3

df2 = df2.reset_index(drop=True)
# df2['utc_time']= pd.to_datetime(df2['date'].apply(str) + ' ' + df2['time'])    # combine 'date' and 'time'

# print(df2.head(),df2.shape)

df2 = df2.iloc[np.repeat(np.arange(len(df2)),2)].reset_index()
# df2['avgPM2.5']=df2['avgPM2.5'].shift(1)
# df2=df2[1:11]

df2['key1']=np.arange(len(df2))%2

df2['key2']=np.arange(len(df2))//48

df2 = df2.sort_values(['key2','key1'])
df2 = df2.reset_index()

# print(df2.tail(),df2.shape)

df2['avgPM10']=df2['avgPM10'].shift(24)                                                                           # 4
df2 = df2[24:18888]

del df2['level_0']
del df2['index']
del df2['key1']
del df2['key2']

df2 = df2.reset_index(drop=True)


finduPM10 = df2['PM10']
print(df2.head(),df2.shape)
time = pd.get_dummies(df2['time'])
time.columns = ['AggPM10 0','AggPM10 1','AggPM10 2','AggPM10 3','AggPM10 4','AggPM10 5',
                'AggPM10 6','AggPM10 7','AggPM10 8','AggPM10 9','AggPM10 10','AggPM10 11','AggPM10 12',            # 5
                'AggPM10 13','AggPM10 14','AggPM10 15','AggPM10 16','AggPM10 17','AggPM10 18',
                'AggPM10 19','AggPM10 20','AggPM10 21','AggPM10 22','AggPM10 23']
timePM10 = time.multiply(df2['avgPM10'], axis="index")                                                             # 6

# print(time.head(),time.shape)
aq2 = df2.join(time)                                                                                               # 7
del aq2['avgPM10']                                                                                                 # 8
del aq2['time']                                                                                                    # 9

print(aq2.head(),aq2.shape)                                                                                        # 10

#######################################################################################################################
# O3


df1 = sample[['stationId',  'date', 'time', 'O3']].copy()                                                      # 1

print(df1.shape)

df1 = df1.iloc[10:9466].reset_index(drop=True)
# print(df1.head(),df1.tail())


# print(df1.drop_duplicates(['date','time']))
# print(df1.head(),df1.shape)
print(df1.shape)                                                                                                  # 2
df2 = df1.set_index(['stationId','time','date'])['O3']\
  .unstack([0,1])\
  .rolling(len(df1),min_periods=1)\
  .mean().shift(1).bfill()\
  .unstack().rename('avgO3')\
  .to_frame()\
  .join(df1.set_index(['stationId','time','date']))\
  .reset_index().sort_values(['stationId','date','time'])                                                         # 3

df2 = df2.reset_index(drop=True)
# df2['utc_time']= pd.to_datetime(df2['date'].apply(str) + ' ' + df2['time'])    # combine 'date' and 'time'

# print(df2.head(),df2.shape)

df2 = df2.iloc[np.repeat(np.arange(len(df2)),2)].reset_index()
# df2['avgPM2.5']=df2['avgPM2.5'].shift(1)
# df2=df2[1:11]

df2['key1']=np.arange(len(df2))%2

df2['key2']=np.arange(len(df2))//48

df2 = df2.sort_values(['key2','key1'])
df2 = df2.reset_index()

# print(df2.tail(),df2.shape)

df2['avgO3']=df2['avgO3'].shift(24)                                                                           # 4
df2 = df2[24:18888]

del df2['level_0']
del df2['index']
del df2['key1']
del df2['key2']

df2 = df2.reset_index(drop=True)


finduO3 = df2['O3']
print(df2.head(),df2.shape)
time = pd.get_dummies(df2['time'])
time.columns = ['AggO3 0','AggO3 1','AggO3 2','AggO3 3','AggO3 4','AggO3 5','AggO3 6','AggO3 7',
                'AggO3 8','AggO3 9','AggO3 10','AggO3 11','AggO3 12',                                    # 5
                'AggO3 13','AggO3 14','AggO3 15','AggO3 16','AggO3 17',
                'AggO3 18','AggO3 19','AggO3 20','AggO3 21','AggO3 22','AggO3 23']
timeO3 = time.multiply(df2['avgO3'], axis="index")                                                                 # 6

# print(time.head(),time.shape)
aq3 = df2.join(time)                                                                                               # 7
del aq3['avgO3']                                                                                                 # 8
del aq3['time']                                                                                                    # 9

print(aq3.head(),aq3.shape)                                                                                        # 10




##############################################################################################################
# finduPM25 = df2['PM2.5']
# finduO3 = df2['O3']
# finduPM10 = df2['PM10']
# Merge PM10, O3 to PM2.5

del aq1['PM2.5']

aq1 = aq1.join(timePM10)
aq1 = aq1.join(timeO3)
# Need to add 0~47
s = pd.Series(np.arange(48))
aq1['48'] = pd.concat([s] * 393).reset_index(drop=True)
twodays = pd.get_dummies(aq1['48'])
print(twodays.head())
del aq1['48']
aq1 = aq1.join(twodays)
# this is the Y


aq1 = aq1.join(finduPM25)
aq1 = aq1.join(finduPM10)
aq1 = aq1.join(finduO3)
# print(aq1.tail(),aq1.shape)

# print(aq1[240:].head(),aq1[240:].shape)
final1 = aq1[240:].reset_index(drop=True)

print(final1.head(60),final1.shape)


final1.to_csv("D:/KDD2018/dongsiDF.csv", index=False)