import sys
from ast import literal_eval
import time
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
        count=0
        for s in sigfile:

            count+=1
            if int(query_bitmap) & ~int(sigfile[s])== int(query_bitmap):
                
                res.append(count)

    t=time.time()-start
    print(res)
    return t
###############################################
          #exact_bitslice_signature_file
###############################################
             
def exact_bitslice_signature_file(qu,bitslice,qnum):
    start=time.time()
    global res

    if int(qnum)==1:
        res={}
        counter_qu=-1
        for i in qu:
            
            counter_qu+=1
            bit=[]
            min_i=min(i)
            max_i=max(i)
            res[str(counter_qu)]=[]
            for k in range(0,min_i):
                bit.append(0)

            for j in range(min_i,max_i+1):
                
                if j in i:
                    bit.append(1)
                else:
                    bit.append(0)
            string_bit = [str(int) for int in bit]
            query_bitmap="".join(string_bit[::-1])
            
            #check if there is a transaction bitmap that satisfies query bitmap bits
            count_tr_bit=0
            for s in bitslice:
                
                count_tr_bit+=1
                if int(query_bitmap) & ~int(bitslice[s]) == int(query_bitmap):
                    
                    res[str(counter_qu)].append(count_tr_bit)

    else:   
        res=[]
        bit=[]
    
        min_i=min(qu[qnum])
        max_i=max(qu[qnum])

        for k in range(0,min_i):
            bit.append(0)
        for j in range(min_i,max_i+1):
            
            if j in qu[qnum]:
                bit.append(1)
            
            else:
                bit.append(0)
        string_bit = [str(int) for int in bit]
        query_bitmap="".join(string_bit[::-1])
        
        #check if there is a transaction bitmap that satisfies query bitmap bits
        count=0
        for s in bitslice:

            count+=1
            if int(query_bitmap) & ~int(bitslice[s])== int(query_bitmap):
                
                res.append(count)

    t=time.time()-start
    print(res)
    return t

############################################
           #inverted file 
############################################


def inverted_file(qu,trans_element_list,qnum):



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

            sigfile={}
            #sigfile construction
            counter=-1
            for i in tr:
                
                counter+=1
                sigfile[str(counter)]=[]
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
        elif method==2:
            #find the max value element in transactions array
            m = max(map(max, tr))
            bitslice={}
            #bitslice construction
            
            for i in range(0,m+1):
                bitslice[i]=0
                counter=-1
                for j in tr:
                    counter+=1
                    if i in j:
                        n=2^counter
                        bitslice[i]+=n
            print("Exact bitslice signature file method result :")
            print("Exact bitslice signature file method computation time =",exact_bitslice_signature_file(qu,bitslice,qnum))           
        elif method==3:
            #find the max value element in transactions array
            m = max(map(max, tr))
            trans_element_list={}
            # list for each transaction construction
            
            for i in range(0,m+1):
                [i]=[]
                counter=-1
                for j in tr:
                    counter+=1
                    if i in j:
                        
                        trans_element_list[i].append(j)
            print("Inverted file method result :")
            print("Inverted file method computation time =",inverted_file(qu,trans_element_list,qnum))                









if __name__ == '__main__':
   
   main()
   