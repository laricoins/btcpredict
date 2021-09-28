import os
from bitcoinaddress import Wallet
import argparse
#использование (usage)
#    %cd drive/MyDrive/btcpredict/generate
#    !pip install bitcoinaddress
#    python linegenegator.py --f train.txt --c  10

def run(f,c):
#если такой файл есть удалаяем его (remove file)
    if os.path.isfile(f):
        os.remove(f)
    j = 0
    myfile = open(f, 'a')
    for i in range(c): 
#        wallet = Wallet('5KJ6H7syUczrx7NRmHeQXefo81z6SFMZYiZ6Qc3oF2BH9XnQHyD')	
#        print(wallet)
        wallet = Wallet()
        wallet = Wallet()
        wif=wallet.key.__dict__['mainnet'].__dict__['wif']
        pubaddr1=wallet.address.__dict__['mainnet'].__dict__['pubaddr1']
        pubaddr1c=wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']
        if (len(pubaddr1)!= 34  or len(pubaddr1c)!= 34 ):
            continue    # continue here 
        myfile.write(pubaddr1  + ";"+wif+"\n")	
        j = j + 1
    print('DONE in file (',f, ') generated ',j,' btc pairs PC;PK')


if __name__ == '__main__':
    ARGS_PARSER = argparse.ArgumentParser()
    ARGS_PARSER.add_argument('--f', default='train.txt',type=str,help='file to load btc address')
    ARGS_PARSER.add_argument('--c', default=10,type=int,help='count generate btc address')
    ARGS = ARGS_PARSER.parse_args()
    run(**vars(ARGS))