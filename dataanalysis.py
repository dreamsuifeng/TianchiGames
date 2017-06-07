import pandas as pd
import numpy as np

dateparse = lambda dates: pd.datetime.strptime(dates, '%YYYY/%M/%DD')
dataAll = pd.read_csv(
    'Tianchi_power.csv',
    index_col=None,
    sep=',',
    parse_dates=[0],
    infer_datetime_format=True)
dataAll=dataAll.set_index('record_date')
idset=set(dataAll['user_id'].tolist())
for id in idset:
    dataId=dataAll[dataAll['user_id']==id]['2016-08-01':'2016-08-30']
    dataId.index=pd.date_range('20160901',periods=30,freq='D')
    try:
        result=pd.concat([result,dataId])
    except:
        result=dataId
        