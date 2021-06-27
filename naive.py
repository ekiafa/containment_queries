#Eftihia Kiafa AM:3003

import sys
from ast import literal_eval
import time

global original_stdout
################################
          #naive
################################


def naive(tr,qu,qnum):
    start=time.time()
    global res
    if int(qnum)==-1:
        
        res=dict()
        counter_qu=-1
        for i in qu:
            counter_qu+=1
            
            res[str(counter_qu)]=[]
            counter_tr=-1
            for j in tr:
                counter_tr+=1
                common=list(set(qu[i]).intersection(set(tr[j])))
                
                if sorted(common)==sorted(qu[i]):

                    res[str(counter_qu)].append(counter_tr)
    else:
        
        res=[] 
        
        for i in tr:   
            print(qu[0])
            common=set(sorted(tr[i])).intersection(set(sorted(qu[qnum])))
            if sorted(common)==sorted(qu[qnum]):
                
                res.append(i)

                
    t=time.time()-start
    if qnum==-1:
        sys.stdout=open("naive.txt",mode="w")
        print("Naive method result:")
        print(res)
        sys.stdout=original_stdout
    else:
        print("Naive method result:")
        print(res)
    return t



def main():      

        transactions=sys.argv[1]
        queries=sys.argv[2]
        # call all the queries with qnum=-1
        # call one of them by giving as input number >=0      
        qnum=sys.argv[3]
        # call naive only with method=0
        # call exact signature only with method=1
        # call exact bitslice signature file only with method=2
        # call invertedfile only with method=3
        # call all of them with method=-1
        method=sys.argv[4]
        
        with open(transactions ,mode='r') as trans,open(queries ,mode='r',encoding='UTF-8') as q:
                tr={}
                qu={}
                counter=-1
                for line in trans:

                   counter+=1
                   tr[counter]=literal_eval(line.rstrip("\n"))
                   
                counter=-1
                for line in q:
                    counter+=1
                    qu[counter]=literal_eval(line.rstrip("\n"))
                    
        qnum=int(qnum)
        method=int(method)
        global original_stdout
        original_stdout = sys.stdout
        
        if method==0 or method==-1:
            
            print("Naive method computation time =",naive(tr,qu,qnum))
        


if __name__ == '__main__':
   
   main()
   
