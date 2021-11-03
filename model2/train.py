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
from numpy import argmax


#https://ru.stackoverflow.com/questions/1334955/python-array-create-function

"""
pip install python-baseconv  requests  bitcoinaddress requests

%cd drive/MyDrive/btcpredict/model2

!python train.py
"""

def Load_Data_FromTxt(c): 
    df = pd.read_csv(c, delimiter=';', header=None)
    return np.array(df)
	
	
def GetXYStr(data_text):  #то что вернула модель yhat1 ,  вроде как правильный приватный ключ y_test,  номер символа  i
    return data_text[:, 0],	data_text[:, 1]
	
def one_hot_encode(sequence, n_unique=58):
    encoding = list()
    for value in sequence:
        vector = [0 for _ in range(n_unique)]
        vector[value] = 1
        encoding.append(vector)
    return encoding	
	
def one_hot_decode(encoded_seq):
    return "".join([base58.encode(argmax(vector)) for vector in encoded_seq])	
	
def one_hot_decodeY(encoded_seq):
    return base58.encode(argmax(encoded_seq))
	
def one_hot_decodeY_row(encoded_seq):
    encoding = []
    for a in encoded_seq:
        encoding.append(one_hot_decodeY(a))
    return encoding
	
	
def generate_dataX(dataset):
    encoding = []
    for value in dataset:
        encoding.append(one_hot_encode([int(base58.decode(char)) for char in value]))
    return np.array(encoding)	


	
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
#https://ru.stackoverflow.com/questions/1334955/python-array-create-function
# autor https://ru.stackoverflow.com/users/330237/guimish
#https://qastack.ru/ai/3850/using-machine-deep-learning-for-guessing-pseudo-random-generator


def newModel(size,model_name):
    if os.path.isfile(model_name):
        model = load_model(model_name) 
    else:
        model = Sequential()
        model.add(LSTM(34, batch_input_shape=(size, 34, 58), stateful=True))    # 986 == 58*34/2
        model.add(Dense(58, activation='softmax'))
#    sgd = tf.keras.optimizers.Adagrad(lr=0.01, epsilon=1e-06)
        model.compile(loss = 'categorical_crossentropy', optimizer = 'adam',metrics=['acc'])
#    model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['acc'])
#    model.compile(loss='mse', optimizer='adam', metrics=['acc'])
    return model
	

def btcWalletCheck(pubaddrRealkey, privatkey):	
    start = time.time() 
    filename = "data/!good.txt"	 
    pubTest = []
    for f in privatkey:
        wallet = Wallet(f)
        pubTest.append(wallet.address.__dict__['mainnet'].__dict__['pubaddr1']) 
        pubTest.append(wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']) 

#    print(pubTest[0])  # 1MPwGpxEXPyiKhruBu3ERBJ4HSeTkuv2Rh
#    print(pubaddrRealkey[0])
	

#    pubTest.append('1Mb2ZehRBCWppsBEaeYm2hroddzhYjc6Gh')
# https://able.bio/rhett/find-items-in-a-python-list--82irtvz	
    apples = [index for index, f in enumerate(pubTest) if f in pubaddrRealkey]
    if len(apples)>0:
        mf = open(filename, 'a')
        for a in privatkey:
            mf.write(a+"\n")	
        mf.close()	
        print("YOOOO good JOB")		
    end = time.time()
    print("Seerch Time :{:3.2f} min... ".format( (end-start)/60 ))
    return 1	 
 	
#######################



file_train= "data/train1000nc.txt"   # файл с теренировочными данными
file_predict= "data/realkey.txt"   #файл с публичными ключами !! размерность 34 символа

# так как данные довольно большие рекомендовано не менее 100 000 то желательно их 1 раз создать а потом использавать подготовленные 
#  если нужно пересобрать данные то достаточно удальть любой из етих файлов
# since the data is quite large, at least 100,000 is recommended, it is advisable to create them 1 time and then use the prepared
# if you need to rebuild the data, then it is enough to delete any of these files 

if os.path.isfile("data/data_text.npy")  and os.path.isfile("data/Xpredict58.npy") and os.path.isfile("data/Xpredict.npy"):
   data_text = np.load("data/data_text.npy",allow_pickle=True)		
   Xpredict58 = np.load("data/Xpredict58.npy")		
   Xpredict = np.load("data/Xpredict.npy",allow_pickle=True)			
#   XpredictStr = np.load("data/XpredictStr.npy",allow_pickle=True)		
else: 
   data_text = Load_Data_FromTxt(file_train)
   np.save("data/data_text.npy", data_text)    
   Xpredict = Load_Data_FromTxt(file_predict)
   np.save("data/Xpredict.npy", Xpredict)    
   Xpredict58 = generate_dataX(Xpredict[:,0])  
   np.save("data/Xpredict58.npy", Xpredict58)    
#   data_predict = Load_Data_FromTxt(file_predict)
#   XpredictStr = np.array(data_predict[:, 0])
#   Xpredict = generate_dataInt(XpredictStr).astype(np.float32)
#   XtrainStr , YtrainStr = GetXYStr(data_text)


#print(data_text)

size = 500 
#y58_all =  generate_dataX(data_text[:, 1])
'''
idx = np.random.randint(0,data_text.shape[0], size)
print(idx)
tempY=data_text[idx, 1]
y58_all = generate_dataX(tempY)
print(tempY)
y58_row = y58_all[:,2]	
print(y58_row)


ggggggg
x58 = x58_all[idx]
y58 = y58_all[idx]

y58_row = y58[:,2]

print(y58_row)
for a in x58:
    xx = one_hot_decode(a)
    print(xx)
	
	
	
for a in y58_row:
    xx = one_hot_decodeY(a)
    print(xx)
print(xpredict)
'''




for i in range(15000):
    idx = np.random.randint(0,data_text.shape[0], size)
    idxValidation = np.random.randint(0,data_text.shape[0], int(size) )
	
	
    tempX=data_text[idx, 0]
    x58 = generate_dataX(tempX)

    tempXValidation=data_text[idxValidation, 0]
    Xvalidation = generate_dataX(tempXValidation)
#    print(x58.shape)
#    ddddd
    tempY=data_text[idx, 1]
    y58_all = generate_dataX(tempY)

    tempYValidation=data_text[idxValidation, 1]
    y58_allValidation = generate_dataX(tempYValidation)

    startAll = time.time() 
    for j in range(0,50+1):     # обкручиваем 51 модели    0 можно потом менять на 1 так как предсказание всегда 5 для ускорения
        start = time.time()  
        y58_row = y58_all[:,j]	# 5JusRfqvuV36QULBycMEh1CwJguQcsLaqCRSn7AW8LDXKZg3mk8   0 == 5  2 == u  50 == 8

        Yvalidation = y58_allValidation[:,j]	# 5JusRfqvuV36QULBycMEh1CwJguQcsLaqCRSn7AW8LDXKZg3mk8   0 == 5  2 == u  50 == 8
 
        model_name  = "data/md_" + str(j).zfill(2) + ".h5"
        model = newModel(size,model_name)	
        md = model.fit(x58, y58_row, epochs=1000, batch_size=size, verbose=0, validation_data=(Xvalidation, Yvalidation),shuffle=False)
        model.reset_states()
        model.save(model_name)
        end = time.time()
        print("End Train & save model ",model_name,"  " ,time.ctime()," train :{:3.2f} ".format( (end-start)/60 ),  "  loss " , md.history['loss'][-1], "acc ",md.history['acc'][-1] )	
    endAll = time.time()
    print("End Train Full "," train :{:3.2f} ".format( (endAll-startAll)/60 ))
##############################################################



    masterPredict = []

    for j in range(0,50+1):     # обкручиваем 51 модели
      model_name  = "data/md_" + str(j).zfill(2) + ".h5"
      model = newModel(size,model_name)	
      yhat = model.predict(Xpredict58, batch_size=size)
      if j == 0 :
           masterPredict.append(one_hot_decodeY_row(yhat))
      else:
           masterPredict=  np.core.defchararray.add(masterPredict, one_hot_decodeY_row(yhat))

    masterPredict = masterPredict[0]
    print(masterPredict)
    btcWalletCheck(Xpredict[:,0],masterPredict)
