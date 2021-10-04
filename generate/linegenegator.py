import os
from bitcoinaddress import Wallet
import argparse
#использование (usage)
#    %cd drive/MyDrive/btcpredict/generate
#    !pip install bitcoinaddress
#    python linegenegator.py --f train.txt --c  2  --t extend

# допустимые значения в приватном ключе в зависимости от разряда
SeqIn=[['H','J','K'],
['1','2','3','4','5','6','7','8','9','A','B','c','d','e','f','G','H','i','j','K','L','M','N','o','P','q','r','s','t','u','V','w','x','y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','i','J','k','L','M','N','o','p','q','R','s','t','U','V','w','x','y','Z'],
['1','2','3','4','5','6','7','8','9','a','b','c','D','E','f','G','h','i','J','k','L','m','N','o','P','q','r','S','t','U','V','W','x','y','Z'],
['1','2','3','4','5','6','7','8','9','a','b','C','d','E','F','g','h','i','j','K','L','M','N','o','P','Q','r','S','t','U','v','W','x','y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','c','d','e','f','g','H','i','J','K','L','m','n','o','P','q','R','S','T','U','v','W','X','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','c','d','e','f','g','H','i','J','k','L','m','n','o','P','Q','r','S','t','u','v','w','x','Y','z'],
['1','2','3','4','5','6','7','8','9','a','b','c','D','e','F','G','h','i','J','k','L','M','N','o','P','Q','R','S','T','U','V','w','X','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','b','C','D','e','F','g','H','i','J','k','L','m','N','o','P','Q','R','s','t','U','v','W','X','y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','C','D','e','f','G','H','i','j','K','L','m','n','o','P','q','R','s','t','u','V','w','X','y','Z'],
['1','2','3','4','5','6','7','8','9','A','b','c','D','E','f','G','H','i','J','K','L','m','N','o','p','Q','r','S','T','U','V','w','x','y','Z'],
['1','2','3','4','5','6','7','8','9','a','b','C','d','e','f','g','h','i','j','K','L','m','n','o','p','q','r','s','t','u','v','W','x','y','z'],
['1','2','3','4','5','6','7','8','9','A','B','c','d','e','f','G','h','i','J','k','L','M','N','o','p','q','R','s','T','u','V','W','x','y','Z'],
['1','2','3','4','5','6','7','8','9','A','b','C','d','e','F','G','H','i','J','k','L','m','N','o','p','Q','r','S','T','u','v','W','x','y','Z'],
['1','2','3','4','5','6','7','8','9','a','b','c','D','e','f','G','H','i','J','k','L','M','N','o','P','Q','R','S','T','u','v','W','x','y','z'],
['1','2','3','4','5','6','7','8','9','a','b','c','D','E','f','g','h','i','J','K','L','m','N','o','P','Q','r','s','T','U','V','w','X','Y','z'],
['1','2','3','4','5','6','7','8','9','a','b','C','D','e','F','G','h','i','J','k','L','M','N','o','P','Q','R','S','t','u','V','w','X','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','c','d','E','F','G','H','i','j','K','L','m','N','o','p','q','R','s','t','u','v','W','X','Y','z'],
['1','2','3','4','5','6','7','8','9','a','b','C','D','e','f','G','h','i','J','K','L','m','n','o','P','Q','r','s','t','U','v','w','X','y','z'],
['1','2','3','4','5','6','7','8','9','A','B','C','d','e','f','G','H','i','J','K','L','m','n','o','p','q','R','s','t','u','v','w','x','y','z'],
['1','2','3','4','5','6','7','8','9','A','b','C','d','E','F','g','H','i','J','K','L','M','n','o','P','q','r','s','T','U','v','W','x','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','g','h','i','j','k','L','m','n','o','P','Q','R','S','t','u','V','w','X','y','Z'],
['1','2','3','4','5','6','7','8','9','a','B','c','D','E','f','g','H','i','j','k','L','m','n','o','p','Q','r','S','t','u','V','w','X','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','c','D','E','f','g','h','i','j','K','L','m','N','o','P','Q','R','s','T','u','V','W','x','Y','z'],
['1','2','3','4','5','6','7','8','9','A','b','C','d','E','f','G','h','i','j','k','L','M','N','o','p','Q','R','s','T','U','V','w','X','y','z'],
['1','2','3','4','5','6','7','8','9','a','b','C','D','e','f','g','H','i','j','k','L','m','N','o','P','Q','R','s','t','u','V','w','X','Y','Z'],
['1','2','3','4','5','6','7','8','9','a','b','C','d','e','F','G','h','i','j','K','L','m','n','o','p','q','r','S','t','U','v','W','x','y','Z'],
['1','2','3','4','5','6','7','8','9','a','b','C','D','E','f','G','H','i','j','K','L','M','N','o','p','q','R','S','t','u','v','W','X','y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','c','D','e','F','g','H','i','J','k','L','M','N','o','p','q','R','s','T','U','V','W','X','Y','z'],
['1','2','3','4','5','6','7','8','9','a','b','C','D','e','f','g','h','i','J','k','L','m','N','o','p','q','R','s','t','U','V','w','x','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','b','c','D','E','f','g','H','i','J','k','L','m','n','o','P','Q','r','s','T','u','v','w','x','Y','z'],
['1','2','3','4','5','6','7','8','9','A','b','C','d','e','f','G','h','i','j','K','L','M','n','o','p','q','R','S','t','u','v','W','X','y','Z'],
['1','2','3','4','5','6','7','8','9','a','b','C','d','E','f','G','h','i','J','K','L','M','n','o','P','Q','r','S','T','U','v','W','x','y','z'],
['1','2','3','4','5','6','7','8','9','a','b','C','D','e','F','G','H','i','J','K','L','m','N','o','p','Q','R','S','T','U','v','W','x','Y','z'],
['1','2','3','4','5','6','7','8','9','A','b','C','D','e','f','g','H','i','J','K','L','m','n','o','p','Q','r','s','t','U','v','w','X','y','z'],
['1','2','3','4','5','6','7','8','9','A','B','C','d','E','F','G','h','i','J','K','L','M','N','o','P','Q','R','S','T','u','v','W','X','Y','z'],
['1','2','3','4','5','6','7','8','9','A','b','C','d','E','f','g','H','i','j','k','L','M','N','o','p','Q','r','s','T','U','V','W','x','y','Z'],
['1','2','3','4','5','6','7','8','9','a','B','c','D','e','F','g','H','i','j','k','L','M','N','o','p','Q','r','s','T','U','V','w','x','Y','Z'],
['1','2','3','4','5','6','7','8','9','a','b','C','d','E','f','G','H','i','j','K','L','M','N','o','P','Q','R','s','t','u','v','w','X','Y','z'],
['1','2','3','4','5','6','7','8','9','A','B','C','D','e','f','g','h','i','J','k','L','m','n','o','P','q','R','S','t','U','v','w','x','y','Z'],
['1','2','3','4','5','6','7','8','9','A','b','c','d','E','f','g','h','i','j','K','L','m','N','o','p','q','R','s','t','U','v','w','x','Y','z'],
['1','2','3','4','5','6','7','8','9','A','B','c','D','e','F','G','h','i','J','K','L','M','N','o','P','q','R','s','t','U','v','W','X','y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','c','D','e','F','G','h','i','J','k','L','M','N','o','P','Q','R','s','T','U','v','W','X','Y','z'],
['1','2','3','4','5','6','7','8','9','a','B','C','D','E','f','g','H','i','j','K','L','M','n','o','p','q','R','s','T','u','V','W','X','Y','z'],
['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','H','i','J','K','L','m','N','o','P','Q','r','S','t','u','V','W','x','Y','z'],
['1','2','3','4','5','6','7','8','9','a','b','C','d','E','f','G','h','i','J','K','L','M','n','o','p','Q','r','S','t','u','v','w','X','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','c','D','e','f','G','H','i','J','k','L','M','N','o','P','q','R','S','T','u','v','W','x','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','B','C','D','e','f','g','h','i','J','K','L','m','N','o','p','q','R','S','T','u','v','w','X','Y','Z'],
['1','2','3','4','5','6','7','8','9','A','b','c','d','E','f','G','H','i','j','k','L','M','n','o','p','q','R','S','T','u','v','w','x','y','Z'],
['1','2','3','4','5','6','7','8','9','A','b','c','D','e','f','g','H','i','j','k','L','m','n','o','P','Q','R','s','t','U','V','w','X','Y','z']
]



def get_unical(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n





def run(f,c,t):
#если такой файл есть удалаяем его (remove file)
    if os.path.isfile(f):
        os.remove(f)
    counter = 0
    myfile = open(f, 'a')
    if t == 'extend':	
        wif_temp = []
        wif_real = []
		
        for i in range(c): 
#        wallet = Wallet('5KJ6H7syUczrx7NRmHeQXefo81z6SFMZYiZ6Qc3oF2BH9XnQHyD')	
#        print(wallet)
            wallet = Wallet()
            wif=wallet.key.__dict__['mainnet'].__dict__['wif']
            pubaddr1=wallet.address.__dict__['mainnet'].__dict__['pubaddr1']
            pubaddr1c=wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']
            if (len(pubaddr1)!= 34  or len(pubaddr1c)!= 34 ):
                continue    # continue here 
				
# получили 10 ключей нужного размера				

            for k in range(1,51): 
                for j in range(0,len(SeqIn[k-1])): 
                    wif_extend=wif[0:k] + SeqIn[k-1][j] + wif[k+1:999999999]
					# собрали для каждого ключа переборук примерно 1700 переборов
#                    print(wif_extend)
                    wallet_e =    Wallet(wif_extend)
                    wif_e =       wallet_e.key.__dict__['mainnet'].__dict__['wif']
#                    print(wif_e)					
                    pubaddr1_e =  wallet_e.address.__dict__['mainnet'].__dict__['pubaddr1']
                    pubaddr1c_e = wallet_e.address.__dict__['mainnet'].__dict__['pubaddr1c']
                    if (len(pubaddr1_e)!= 34  or len(pubaddr1c_e)!= 34 ):
                       continue    # continue here 
                    wif_temp.append(wif_e)
#                    myfile.write(pubaddr1_e  + ";"+wif_e+"\n")						   



        wif_real = get_unical(wif_temp)
        for i in wif_real:
            wallet_e =    Wallet(i)
            pubaddr1_e =  wallet_e.address.__dict__['mainnet'].__dict__['pubaddr1']
            wif_e =       wallet_e.key.__dict__['mainnet'].__dict__['wif']
#            print(wif_e)	
            counter = counter + 1			
            myfile.write(pubaddr1_e  + ";"+wif_e+"\n")			

	
    else: 	
        for i in range(c): 
#        wallet = Wallet('5KJ6H7syUczrx7NRmHeQXefo81z6SFMZYiZ6Qc3oF2BH9XnQHyD')	
#        print(wallet)
            wallet = Wallet()
            wif=wallet.key.__dict__['mainnet'].__dict__['wif']
            pubaddr1=wallet.address.__dict__['mainnet'].__dict__['pubaddr1']
            pubaddr1c=wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']
            if (len(pubaddr1)!= 34  or len(pubaddr1c)!= 34 ):
                continue    # continue here 
            myfile.write(pubaddr1  + ";"+wif+"\n")	
            counter = counter + 1
    print('DONE in file (',f, ') generated ',counter,' btc pairs PC;PK')


if __name__ == '__main__':
    ARGS_PARSER = argparse.ArgumentParser()
    ARGS_PARSER.add_argument('--f', default='train.txt',type=str,help='file to load btc address')
    ARGS_PARSER.add_argument('--c', default=10,type=int,help='count generate btc address')
    ARGS_PARSER.add_argument('--t', default='normal',type=str,help='have (normal, extend) normal - simle list , extend multi list')
    ARGS = ARGS_PARSER.parse_args()
    run(**vars(ARGS))