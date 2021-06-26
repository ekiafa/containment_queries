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
    if qnum==-1:
        sys.stdout=open("naive.txt",mode="w")
        print("Naive method result:")
        print(res)
        sys.stdout=original_stdout
    else:
        print("Naive method result:")
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
    if qnum==-1:
        sys.stdout=open("sigfile.txt",mode="w")
        print("Exact signature file method result :")
        print(res)
        sys.stdout=original_stdout
    else:
        print("Exact signature file method result :")
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
    if qnum==-1:
        sys.stdout=open("bitslice.txt",mode="w")
        print("Exact bitslice signature file method result :")
        print(res)
        sys.stdout=original_stdout
    else:
        print("Exact bitslice signature file method result :")
        print(res)
    return t



############################################
           #inverted file 
############################################



def intersection(a, b, n, m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: array of inter of two array or -1
    '''
 
    inter = []
    i = j = 0
     
    while i < n and j < m:
        if a[i] == b[j]:
 
            # If duplicate already present in inter list
            if len(inter) > 0 and inter[-1] == a[i]:
                i+= 1
                j+= 1
 
            # If no duplicate is present in inter list
            else:
                inter.append(a[i])
                i+= 1
                j+= 1
        elif a[i] < b[j]:
            i+= 1
        else:
            j+= 1
             
    if not len(inter):
        return [-1]
    return inter   

def inverted_file(qu,trans_element_list,qnum):
    start=time.time()
    global res
    if int(qnum)==1:
        res={}
        counter_qu=-1
        for i in qu:
            counter_qu+=1
            counter=-1
            for j in i:
                counter+=1
                if counter==0:
                    m_res=intersection(trans_element_list[j],trans_element_list[j+1],len(trans_element_list[j]),len(trans_element_list[j+1]))
                else:
                    m_res=intersection(m_res,trans_element_list[j],len(m_res),len(trans_element_list[j]))
            res[i]=m_res   
    else:
        res=[]

        counter=-1
        for j in qu[qnum]:
            counter+=1
            if counter==0:
                m_res=intersection(trans_element_list[j],trans_element_list[j+1],len(trans_element_list[j]),len(trans_element_list[j+1]))
            else:
                m_res=intersection(m_res,trans_element_list[j],len(m_res),len(trans_element_list[j]))
        res=m_res
    t=time.time()-start      
    if qnum==-1:
        sys.stdout=open("invfile.txt",mode="w")
        print("Inverted file method result :")
        print(res)
        sys.stdout=original_stdout
    else:
        print("Inverted file method result :")
        print(qnum,":",res)
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
        global original_stdout
        original_stdout = sys.stdout

        if method==0 or method==-1:
            
            print("Naive method computation time =",naive(tr,qu,qnum))
        if method==1 or method==-1:
            
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
                
            
           
            print("Exact signature file method computation time =",exact_signature_file(qu,sigfile,qnum))
        if method==2 or method==-1:

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

            
            print("Exact bitslice signature file method computation time =",exact_bitslice_signature_file(qu,bitslice,qnum))           
        if method==3 or method==-1:
            
            #find the max value element in transactions array
            m = max(map(max, tr))
            trans_element_list={}
            # list for each transaction construction
            
            for i in range(0,m+1):
                trans_element_list[i]=[]
                counter=-1
                for j in tr:
                    counter+=1
                    if i in j:
                        
                        trans_element_list[i].append(counter)

            
            print("Inverted file method computation time =",inverted_file(qu,trans_element_list,qnum))                









if __name__ == '__main__':
   
   main()
   