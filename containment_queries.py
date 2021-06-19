import sys
from ast import literal_eval
import time
def naive(tr,qu,qnum):
    start=time.time()
    global res
    if int(qnum)==-1:
        
        res=dict()
        counter_qu=-1
        for i in qu:
            counter_qu+=1
            l=len(i)
            res[str(counter_qu)]=[]
            counter_tr=-1
            for j in tr:
                counter_tr+=1
                common=list(set(i).intersection(j))
                
                if len(common)==l:

                    res[str(counter_qu)].append(counter_tr)
    else:
        
        res=[] 
        counter=-1
        for i in tr:
            counter+=1
            common=list(set(i).intersection(qu[int(qnum)]))
            if len(common)==len(qu[int(qnum)]):
                res.append(counter)
    t=time.time()-start
    print(res)
    return t


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
            min_i=min(i)
            max_i=max(i)
            res[str(counter_qu)]=[]
            for k in range(0,min_i):
                sig.append(0)

            for j in range(min_i,max_i+1):
                
                if j in i:
                    sig.append(1)
                else:
                    sig.append(0)
            string_sig = [str(int) for int in sig]
            query_bitmap="".join(string_sig[::-1])
            
            #check if there is a transaction bitmap that satisfies query bitmap bits
            count_tr_sig=0
            for s in sigfile:
                count_tr_sig+=1
                if int(query_bitmap) & ~int(s) == 0:
                    
                    res[str(counter_qu)].append(count_tr_sig)
    else:
        res=[]
        sig=[]
    
        min_i=min(qu[int(qnum)])
        max_i=max(qu[int(qnum)])
        for k in range(0,min_i):
            sig.append(0)
        for j in range(min_i,max_i+1):
            
            if j in qu:
                sig.append(1)
            else:
                sig.append(0)
        string_sig = [str(int) for int in sig]
        query_bitmap="".join(string_sig[::-1])
        
        #check if there is a transaction bitmap that satisfies query bitmap bits
        count=0
        for s in sigfile:
            count+=1
            if int(query_bitmap) & ~int(s) == 0:
                
                res.append(count)

    t=time.time()-start
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
                tr=[]
                qu=[]
                for line in trans:
                   tr.append(literal_eval(line.rstrip("\n")))
                   
                for line in q:
                    qu.append(literal_eval(q.readline().rstrip("\n")))
        qnum=int(qnum)
        method=int(method)
        if method==0:
            print("Naive method result:")
            print("Naive method computation time =",naive(tr,qu,qnum))
        elif method==1:
            
            s = set(range(len(tr)))
            sigfile=dict.fromkeys(s)
            #sigfile construction
            counter=0
            for i in tr:
                counter+=1
                sig=[]
                min_i=min(i)
                max_i=max(i)
                for k in range(0,min_i):
                    sig.append(0)
                for j in range(min_i,max_i+1):
                    
                    if j in i:
                        sig.append(1)
                    else:
                        sig.append(0)
                string_sig = [str(int) for int in sig]
                sigfile[str(counter)]="".join(string_sig[::-1])
            
            print("Exact signature file method result :")
            print("Exact signature file method computation time =",exact_signature_file(qu,sigfile,qnum))
            







if __name__ == '__main__':
   
   main()
   