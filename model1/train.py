import os, time
import numpy as np
import pandas as pd
from baseconv import base2, base16, base36, base56, base58, base62, base64
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout,Input,BatchNormalization,LeakyReLU, ReLU
from random import randint
import requests 
from bitcoinaddress import Wallet
import tensorflow as tf
from matplotlib import pyplot
from keras import backend as K
import random
from bcomm.bcomm  import SeqIn58, SeqIn10


#https://ru.stackoverflow.com/questions/1334955/python-array-create-function

"""
pip install python-baseconv  requests  bitcoinaddress requests

%cd drive/MyDrive/btcpredict/model1

!python train.py
"""

def Load_Data_FromTxt(c): 
    df = pd.read_csv(c, delimiter=';', header=None)
    return np.array(df)
	
	
def GetXYStr(data_text):  #то что вернула модель yhat1 ,  вроде как правильный приватный ключ y_test,  номер символа  i
    return data_text[:, 0],	data_text[:, 1]
	
	
	
def generate_dataInt(XtrainStr):
    v = list()
    for vs in XtrainStr:
        v.append([int(base58.decode(res)) for res in np.array(list(vs))])
    return np.array(v)
	
	
def human_convert(yhat):
    v = list()
    yhatD = np.rint(yhat).astype(int)
    for vs in yhatD:
        tmp = ''.join(map(base58.encode, vs))
        v.append('5'+tmp[1:])  
    return np.array(v)	
	
	 
 	
def btcWalletCheck(realkey, privatkey):	
    start = time.time()  
#    print(realkey)
#    print(len(privatkey))
    filename = "!good.txt"	  
    pubaddr = []
    privatkeyTemp = []
    for i in privatkey:
        if len(i) == 51  :
            privatkeyTemp.append(i)
			
    print('Try research in ',len(privatkeyTemp), time.ctime() )			
			

#    print(len(privatkeyTemp))
    i=0
    for prkey in privatkeyTemp:
        wallet = Wallet(prkey)
        pubaddr.append(wallet.address.__dict__['mainnet'].__dict__['pubaddr1'])      
        pubaddr.append(wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']) 
#    pubaddr.append('1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ') 
		
    end = time.time()
#    print(len(pubaddr))	
#    print(pubaddr)		
    apples = [index for index, f in enumerate(realkey) if f in pubaddr]
#    print(len(apples)) 	
    print("Search Find Time :{:3.2f} ".format( (end-start)/60 ))
	
	
    if len(apples)>0:
       print("!!!!!!!!!!  GOOOD")

	
       mf = open(filename, 'a')
       for a in privatkeyTemp:
           mf.write(a+"\n")	
       mf.close()	
	   
       bbbbbbbb   
	   
    return 1	

def custom_activation(x):
    res = []
    xn = x.tolist()
    cdn = SeqIn10.tolist();
    for i in range(0, len(xn)):
        tmp = [];
        for n in range(0, len(xn[i])):
            if (int(round(xn[i][n])) in cdn[n]):
                tmp.append(xn[i][n]);
            else:
                tmp.append(cdn[n][randrange(0, len(cdn[n]))])
        res.append(tmp)
    print(res)		
    return res

def newModel():
# модель можно и нужно переработать, возможно кто то подскажет лучшее решение    @ddnitecry
# the model can and should be reworked, maybe someone will tell you the best solution    @ddnitecry


    act ='relu'
    model = Sequential()
#    model.add(BatchNormalization()) 
    model.add(Dense(34*2, activation=act, input_dim=34))
#        model.add(Dropout(0.2)) 
    model.add(Dense(34*100, activation=act))   #160 000 
#        model.add(Dropout(0.2)) 
#    model.add(Dense(51, activation=btcActAbg))
    model.add(Dense(51, activation=custom_activation))
    model.compile( optimizer='adam',loss='mse',metrics=['acc'], run_eagerly=True,)
    return model





#######################



file_train= "data/train.txt"   # файл с теренировочными данными
file_predict= "data/realkey.txt"   #файл с публичными ключами !! размерность 34 символа

# так как данные довольно большие рекомендовано не менее 100 000 то желательно их 1 раз создать а потом использавать подготовленные 
#  если нужно пересобрать данные то достаточно удальть любой из етих файлов
# since the data is quite large, at least 100,000 is recommended, it is advisable to create them 1 time and then use the prepared
# if you need to rebuild the data, then it is enough to delete any of these files 

if os.path.isfile("data/Xtrain.npy") and os.path.isfile("data/Ytrain.npy") and os.path.isfile("data/Xpredict.npy") and os.path.isfile("data/XpredictStr.npy"):
   Xtrain = np.load("data/Xtrain.npy")	
   Ytrain = np.load("data/Ytrain.npy")		
   Xpredict = np.load("data/Xpredict.npy")		
   XpredictStr = np.load("data/XpredictStr.npy",allow_pickle=True)		
else: 
   data_text = Load_Data_FromTxt(file_train)
   data_predict = Load_Data_FromTxt(file_predict)
   XpredictStr = np.array(data_predict[:, 0])
   Xpredict = generate_dataInt(XpredictStr).astype(np.float32)
   XtrainStr , YtrainStr = GetXYStr(data_text)
   Xtrain = generate_dataInt(XtrainStr).astype(np.float32)
   Ytrain = generate_dataInt(YtrainStr).astype(np.float32)
   np.save("data/Xtrain.npy", Xtrain)    
   np.save("data/Ytrain.npy", Ytrain)    
   np.save("data/Xpredict.npy", Xpredict)   
   np.save("data/XpredictStr.npy", XpredictStr)   
   
#print(Xtrain)    вход модели
#print(Ytrain)    выход модели


for i in range(1, 2):  	# типа бесконечно крутим
	start = time.time()  	
	batch_size = 100
	idx = np.random.randint(0,Xtrain.shape[0], batch_size)
#        print(idx)	
#        idx = np.random.randint(0,Xtrain.shape[0], 13000)
#        print(Xtrain[idx])
#        print(Ytrain[idx]) 
#        ssssssss  
#        model.fit(Xtrain[idx], Ytrain[idx], epochs=2000, batch_size=13000, validation_split=0.1,verbose=1,   shuffle=False)
	print("Start Train ", time.ctime() )	
	model = newModel()
	md = model.fit(Xtrain[idx], Ytrain[idx], epochs=3, batch_size=batch_size, verbose=0,   shuffle=False)
	model.reset_states()
	
	end = time.time()

#    model.save(model_name)  
	print("End Train & save model ",time.ctime()," train :{:3.2f} ".format( (end-start)/60 ),  "  loss " , md.history['loss'][-1], "acc ",md.history['acc'][-1] )	
	yhat = model.predict(Xpredict).astype(int)
	yhatD = human_convert(yhat)
	print(yhatD)

	btcWalletCheck(XpredictStr,yhatD)
