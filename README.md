# containment_queries
Containment methods assignment in the context of Complex Data Management course [Complex Data Management,MYY041](https://www.cs.uoi.gr/course/%CE%B4%CE%B9%CE%B1%CF%87%CE%B5%CE%AF%CF%81%CE%B9%CF%83%CE%B7-%CF%83%CF%8D%CE%BD%CE%B8%CE%B5%CF%84%CF%89%CE%BD-%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD/)


<h3>Input files:</h3>
   <li>  transactions.txt</li>
   <li>  queries.txt</li>

<h3>Program file:</h3>
   <li>  containment_queries.py : File with 4 methods implementation, data management and file making for some of methods.Bitwise operations are supported.</li>
   <p>      </p>
   <h3>qnum</h3>
   <li>call all the queries with qnum=-1 </li>
   <li>call one of them by giving as input number >=0  </li>
   
   <h3>methods</h3>
   <li>call naive only with method=0</li>
   <li>call exact signature only with method=1</li>
   <li>call exact bitslice signature file only with method=2</li>
   <li>call invertedfile only with method=3</li>
   <li>call all of them with method=-1</li>
   <p>      </p>
   
 > python3 containment_queries.py transactions.txt queries.txt qnum method  



 <p>Example:</p>
 
 
 > python3 containment_queries.py transactions.txt queries.txt 0 3 
  

<h3>Language:</h3>
     Python 3.6.0

<h3>License:</h3>
     MIT
