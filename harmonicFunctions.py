# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import datetime as dt
from Harmonicpatterns import *
import MetaTrader5 as mt
import time
import config
mt.initialize()


#to login
login=  config.login #your login
password= config.password #your password
server = config.server #your server, you either put them here directly or as named here in the config file.

mt.login(login,password,server)


#settings
pairs=['EURCAD','EURAUD','CADTRY','CADCHF','CADJPY','US30','UK100','EURUSD','USDCHF','NZDJPY','GBPNZD','GBPCAD','GBPAUD','EURJPY','EURCHF','XAUUSD','USDCAD','GBPUSD','NZDUSD','NZDCAD','GBPJPY','EURGBP']

while True:
    for symbol in pairs:
        #request ohlc data and save them in a pandas dataframe
        data=mt.copy_rates_from_pos(symbol, mt.TIMEFRAME_M1, 0, 100)
        df=pd.DataFrame(data)[['time','open','high','low','close']]
        df['time']=pd.to_datetime(df['time'],unit='s')
        df.dropna(inplace=True)
        #data.columns=['Date','open','high','low','close','vol']
        #data.dropna(inplace=True)
        #dt.datetime.fromisoformat(data['Date'])
        #data['Date']=pd.to_datetime(data['time'])
        
        #data.set_index(data.Date,format='%d.%m.%Y %H:%M:%S')
        #data.set_index(data['Date'])
        #data=data[['open','high','low','close','vol']]
        #data.drop_duplicates(keep=False)
        price=data['close'].copy()#.iloc[:500]
        #print(data)
        
        err_allowed=10.0/100
        #finding our relative extrema
        #creating dynamic plot
         
        current_idx,current_pattern,start,end=peak_detect(price)
        
        XA=current_pattern[1]-current_pattern[0]
        AB=current_pattern[2]-current_pattern[1]
        BC=current_pattern[3]-current_pattern[2]
        CD=current_pattern[4]-current_pattern[3]
        moves=[XA,AB,BC,CD]
        gart=is_gartley(moves,err_allowed)
        butt=is_butterfly(moves,err_allowed)
        bat=is_bat(moves,err_allowed)
        crab=is_crab(moves,err_allowed)
        harmonics=np.array([gart,butt,bat,crab])
        if np.any(harmonics==1):
             if  not mt.positions_get(symbol=symbol):
               
                request={
                'action':mt.TRADE_ACTION_DEAL,
                'symbol':symbol,
                'volume':0.20,
                'type':mt.ORDER_TYPE_BUY,#or mt.ORDER_TYPE_BUY, for buy
                'price':mt.symbol_info_tick(symbol).bid,
                'sl':0.0,#float
                'tp':0.0,#float
                'deviation':20,#integer, slippage
                'magic':7629765,#integer, ticket no, or id
                'comment':'python script open',
                'type_time':mt.ORDER_TIME_GTC,#valid until you cancel it
                'type_filling':mt.ORDER_FILLING_IOC,#the max size will be taken if the volume is big
                
                }
            
                order=mt.order_send(request)
                print('BUY Executed on:'+symbol)
            
            
            
        elif np.any(harmonics==-1):
            if not mt.positions_get(symbol=symbol): 
                request={
                'action':mt.TRADE_ACTION_DEAL,
                'symbol':symbol,
                'volume':0.20,
                'type':mt.ORDER_TYPE_SELL,#or mt.ORDER_TYPE_BUY, for buy
                'price':mt.symbol_info_tick(symbol).ask,
                'sl':0.0,#float
                'tp':0.0,#float
                'deviation':20,#integer, slippage
                'magic':7629765,#integer, ticket no, or id
                'comment':'python script open',
                'type_time':mt.ORDER_TIME_GTC,#valid until you cancel it
                'type_filling':mt.ORDER_FILLING_IOC,#the max size will be taken if the volume is big
                }
            
                order=mt.order_send(request)
                print('SELL Executed on:'+symbol)

    time.sleep(5)                
    

      
            
            
            
            
            
            
            
            
            