import sys




def main():      
        
        transactions=sys.argv[1]
        queries=sys.argv[2]



        with open(transactions ,mode='r') as trans,open(queries ,mode='r',encoding='UTF-8') as q:
               for line in trans:
                   print(line)
               for line in q:
                   print(q)





if __name__ == '__main__':
   
   main()
   