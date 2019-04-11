import pandas as pd
import numpy as np

d = {'ID': [ "A1","A1", "A2","A2","A3","A3","B1","B1","B2","B2","B3","B3","C1",
             "C1","C2","C2","C3","C3"],

     'value': [11,11,12,12,13,13,21,21,22,22,23,23,31,31,32,32,33,33]}

df = pd.DataFrame(data=d)

# df = df.iloc[1::2]
# df = df.iloc[np.repeat(np.arange(len(df)),2)]

# def shifty(d):
#     return d.iloc[(np.arange(len(d)) % 2).argsort(kind='mergesort')]
#
# df = df.groupby(df.ID.str[0], group_keys=False).apply(shifty)

df['key1']=np.arange(len(df))%2

df['key2']=np.arange(len(df))//6

df = df.sort_values(['key2','key1'])
print(df)