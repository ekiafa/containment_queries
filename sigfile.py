#Eftihia Kiafa AM:3003

import sys
from ast import literal_eval
import time

global original_stdout
#######################################
          #exact_signature_file
#######################################
def exact_signature_file(qu,sigfile,qnum):
    start=time.time()
    global res
    if int(qnum)==-1:
        res=dict()
        counter_qu=-1
        #convert query to bitmap format
        for i in qu:
            
            counter_qu+=1
            sig=[]
            min_i=min(qu[i])
            max_i=max(qu[i])
            res[str(counter_qu)]=[]
            for k in range(0,min_i):
                sig.append(0)

            for j in range(min_i,max_i+1):
                
                if j in qu[i]:
                    sig.append(1)
                else:
                    sig.append(0)
            string_sig = [str(int) for int in sig]
            query_bitmap="".join(string_sig[::-1])
            
            #check if there is a transaction bitmap that satisfies query bitmap bits
            count_tr_sig=0
            for s in sigfile:
                
                count_tr_sig+=1
                if int(query_bitmap) & ~int(sigfile[s]) == int(query_bitmap):
                    
                    res[str(counter_qu)].append(count_tr_sig)
    else:
        res=[]
        sig=[]
    
        min_i=min(qu[qnum])
        max_i=max(qu[qnum])

        for k in range(0,min_i):
            sig.append(0)
        for j in range(min_i,max_i+1):
            
            if j in qu[qnum]:
                sig.append(1)
            
            else:
                sig.append(0)
        string_sig = [str(int) for int in sig]
        query_bitmap="".join(string_sig[::-1])
        
        #check if there is a transaction bitmap that satisfies query bitmap bits
        count=-1
        for s in sigfile:

            count+=1
            print(query_bitmap)
            if int(query_bitmap,2) & ~int(sigfile[s],2)== 0:
                
                res.append(count)

    t=time.time()-start
    if qnum==-1:
        sys.stdout=open("sigfile.txt",mode="w")
        print("Exact signature file method result :")
        print(res)
        sys.stdout=original_stdout
    else:
        print("Exact signature file method result :")
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

        if method==1 or method==-1:
            
            sigfile={}
            #sigfile construction
            counter=-1
            for i in tr:
                
                counter+=1
                sigfile[str(counter)]=[]
                sig=[]
                min_i=min(tr[i])
                max_i=max(tr[i])
                for k in range(0,min_i):
                    sig.append(0)
                for j in range(min_i,max_i+1):
                    
                    if j in tr[i]:
                        sig.append(1)
                    else:
                        sig.append(0)
                string_sig = [str(int) for int in sig]
                sigfile[str(counter)]="".join(string_sig[::-1])
                
            
           
            print("Exact signature file method computation time =",exact_signature_file(qu,sigfile,qnum))








if __name__ == '__main__':
   
   main()
   
