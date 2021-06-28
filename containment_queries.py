#Eftihia Kiafa AM:3003

import sys
from ast import literal_eval
import time
from functools import reduce
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
            
            common=set(sorted(tr[i])).intersection(set(sorted(qu[qnum])))
            if sorted(common)==sorted(qu[qnum]):
                
                res.append(i)

                
    t=time.time()-start
    if qnum==-1:
        sys.stdout=open("naive.txt",mode="w")
        print("Naive method result:")
        for i in res:
            print (str(i)+":"+ str(res[i]))
        
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
            count_tr_sig=-1
            for s in sigfile:
                
                count_tr_sig+=1
                if int(query_bitmap,2) & ~int(sigfile[s],2) == 0:
                    
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
            
            if int(query_bitmap,2) & ~int(sigfile[s],2)== 0:
                
                res.append(count)

    t=time.time()-start
    if qnum==-1:
        sys.stdout=open("sigfile.txt",mode="w")
        print("Exact signature file method result :")
        for i in sigfile:
            print (str(i)+":"+ str(int(sigfile[i],2)))
        
        sys.stdout=original_stdout
    else:
        sys.stdout=open("sigfile.txt",mode="w")
        print("Exact signature file method result :")
        for i in sigfile:
            print (str(i)+":"+ str(int(sigfile[i],2)))
        
        sys.stdout=original_stdout
        print("Exact signature file method result :")
        print(res)
    return t

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
        for i in bitslice:
            print (str(i)+":"+ str(bitslice[i]))
        
        sys.stdout=original_stdout
    else:
        print("Exact bitslice signature file method result :")
        print(res)
        sys.stdout=open("bitslice.txt",mode="w")
        sys.stdout.write('\n')
        print("Exact bitslice signature file method result :")
        for i in bitslice:
            print (str(i)+":"+ str(bitslice[i]))
        
        sys.stdout=original_stdout

    return t



############################################
           #inverted file 
############################################



def intersection(a, b, n, m):
    
    #a: given sorted array a
    #n: size of sorted array a
    #b: given sorted array b
    #m: size of sorted array b
    #return: array of inter of two array or -1
    
 
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
    if int(qnum)==-1:
        res={}
        for i in qu:
           
            for j in qu[i]:
                counter=-1
                qu_list=[]
                for k in qu[i]:
                    qu_list.append(trans_element_list[k])
                for p in range(0,len(qu_list)-1):
                    
                    counter+=1
                    if counter==0:
                        m_res=intersection(qu_list[p],qu_list[p+1],len(qu_list[p]),len(qu_list[p+1]))
                    
                    else:
                        m_res=intersection(m_res,qu_list[p],len(m_res),len(qu_list[p]))
                        
            res[i]=m_res 
    else:
        res=[]

        counter=-1
        qu_list=[]
        for j in qu[qnum]:
            qu_list.append(trans_element_list[j])
        for i in range(0,len(qu_list)):
            
            counter+=1
            if counter==0:
                m_res=intersection(qu_list[i],qu_list[i+1],len(qu_list[i]),len(qu_list[i+1]))
            
            else:
                m_res=intersection(m_res,qu_list[i],len(m_res),len(qu_list[i]))
                        
        res=m_res




    t=time.time()-start      
    if qnum==-1:
        sys.stdout=open("invfile.txt",mode="w")
        print("Inverted file method result :")
        for i in trans_element_list:
            print (str(i)+":"+ str(trans_element_list[i]))
        
        sys.stdout=original_stdout
    else:
        sys.stdout=open("invfile.txt",mode="w")
        print("Inverted file method result :")
        for i in trans_element_list:
            print (str(i)+":"+ str(trans_element_list[i]))
        
        sys.stdout=original_stdout
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

        if method==2 or method==-1 :

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
                      
        if method==3 or method==-1:
            
            #find the max value element in transactions array
            m = max(i for v in tr.values() for i in v)
            trans_element_list={}
            # list for each transaction construction
            
            for i in range(0,m+1):
                trans_element_list[i]=[]
                
                for j in tr:
                
                    if i in tr[j]:
                        
                        trans_element_list[i].append(j)

            print("Inverted file method computation time =",inverted_file(qu,trans_element_list,qnum))                









if __name__ == '__main__':
   
   main()
   