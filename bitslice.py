#Eftihia Kiafa AM:3003

import sys
from ast import literal_eval
import time
from functools import reduce
global original_stdout
###############################################
          #exact_bitslice_signature_file
###############################################
             
def exact_bitslice_signature_file(qu,bitslice,qnum):
    start=time.time()
    global res

    if int(qnum)==-1:
        res={}
        
        for i in qu:
            bitslice_and=[]
            res[i]=[]
            for j in qu[i]:
                bitslice_and.append(int(bitslice[j]))
                    
            a=reduce(lambda x,y: x & y, bitslice_and)
                
            c=format(a, "b")
                
            counter=-1

            for k in c[::-1]:
                    
                counter+=1
                if k=='1':
                    res[int(i)].append(counter)

    else:   
        res=[]
        
        bitslice_and=[]
        
        for i in qu[qnum]:
        
            bitslice_and.append(int(bitslice[i]))
            
        a=reduce(lambda x,y: x & y, bitslice_and)
        
        c=format(a, "b")
        
        counter=-1

        for i in c[::-1]:
            
            counter+=1
            if i=='1':
                res.append(counter)
            



    t=time.time()-start
    if qnum==-1:
        sys.stdout=open("bitslice.txt",mode="w")
        sys.stdout.write('\n')
        print("Exact bitslice signature file method result :")
        for i in res:
            print (str(i)+":"+ str(res[i]))
        
        sys.stdout=original_stdout
    else:
        print("Exact bitslice signature file method result :")
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
                   #tr.append(literal_eval(line.rstrip("\n")))
                counter=-1
                for line in q:
                    counter+=1
                    qu[counter]=literal_eval(line.rstrip("\n"))
                    
        qnum=int(qnum)
        method=int(method)
        global original_stdout
        original_stdout = sys.stdout


        if method==2 :

            #find the max value element in transactions array
            
            m = max(i for v in tr.values() for i in v)
            
            bitslice={}
            #bitslice construction
            
            for i in range(0,m+1):
                
                bitslice[i]=0
                for j in tr:
                    if i in tr[j]:
                        bitslice[i]+=pow(2,j)

    
            print("Exact bitslice signature file method computation time =",exact_bitslice_signature_file(qu,bitslice,qnum))           
             









if __name__ == '__main__':
   
   main()
   

