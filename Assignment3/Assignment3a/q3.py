from datetime import datetime
from datetime import timedelta
import ast
import math
import sys

sys.stdout = open("/home/vishal/Desktop/SSD/Assignment3/Q3/output.txt", 'w')
f = open("/home/vishal/Desktop/SSD/Assignment3/Assignment3a/Employee1.txt", "r")
t = open("/home/vishal/Desktop/SSD/Assignment3/Assignment3a/Employee2.txt", "r")
dict={}
dict1={}
string=f.read()
dict = ast.literal_eval(string)
litrl=t.read()
dict1 = ast.literal_eval(litrl)
e1_name=list(dict.keys())[0]
e1_date=list(list(dict.values())[0].keys())[0]
#print(empDate1)
e1_busy=list(list(dict.values())[0].values())[0]

e2_name=list(dict1.keys())[0]
e2_date=list(list(dict1.values())[0].keys())[0]
#print(empDate1)
e2_busy=list(list(dict1.values())[0].values())[0]
#print(e2_busy)

list1=[]
list2=[]
e1_available=[]
e2_available=[]
e1_duration=[]
e2_duration=[]
result=[]


def find_res(f1,f2,l1,l2,dur):
    m=""
    m=f2.strftime("%-I:%M%p")
    m+="-"
    m=m+(f2+dur).strftime("%-I:%M%p")
    #print(m)
    result.append(m)

def find_ans(f1,f2,l1,l2,dur):
    m=""
    m=f1.strftime("%-I:%M%p")
    m+="-"
    m=m+(f2+dur).strftime("%-I:%M%p")
    result.append(m)



def find_common(dur):
    dur=float(dur)*60*60
    dur=timedelta(0,dur)
    i=0
    
    flag=1
    #print(dur<=e1_duration[0])
    while i < len(e1_duration):
        if flag==0:
            break
        if dur<=e1_duration[i]:
            j=0
            while j < len(e2_duration):
            
                if dur <= e2_duration[j]:
                   #print(i,j)
                   f1=datetime.strptime(list(e1_available[i].split("-"))[0], "%I:%M%p")
                   f2=datetime.strptime(list(e2_available[j].split("-"))[0], "%I:%M%p")
                   l1=datetime.strptime(list(e1_available[i].split("-"))[1], "%I:%M%p")
                   l2=datetime.strptime(list(e2_available[j].split("-"))[1], "%I:%M%p")

                   if f1<=f2 and l1-f2>=dur and l2-f2 >= dur:
                      find_res(f1,f2,l1,l2,dur)
                      flag=0
                   elif f1>f2 and l1-f1>=dur and l2-f1>=dur :
                      find_ans(f1,f2,l1,l2,dur)
                      flag=0
                j=j+1
                #print(i,j)
        i=i+1
                   
                      

    dictonary={}
    dictonary[e1_date]=result
    print(e1_available)
    print(e2_available)
    print(dictonary)



def conversion(l):
        ls = ' '.join([str(elem) for elem in l])  
        x= ls.replace("-" ,"")
        x.strip()
        #print(x)
        res = " ".join(x.split()) 
        li=list(res.split(" "))
        for i in li:
            #print(i)
            date_object = datetime.strptime(str(i),"%I:%M%p")
            list1.append(date_object)
        #list(group(list1,2))
        #print(list1[0])


def conversion1(l):
        ls = ' '.join([str(elem) for elem in l])  
        x= ls.replace("-" ,"")
        x.strip()
        #print(x)
        res = " ".join(x.split()) 
        li=list(res.split(" "))
        for i in li:
            #print(i)
            date_object = datetime.strptime(str(i),"%I:%M%p")
            list2.append(date_object)
        #print(list2)

def fun1():
    m=""
    m+=start.strftime("%-I:%M%p")
    m+="-"
    m+=list1[0].strftime("%-I:%M%p")
    e1_available.append(m)
    e1_duration.append(list1[0]-start)

def fun2():
    m=""
    m+=start.strftime("%-I:%M%p")
    m+="-"
    m+=list2[0].strftime("%-I:%M%p")
    e2_available.append(m)
    e2_duration.append(list2[0]-start)    

  



              
            
k=1
v=1
if(e1_date!=e2_date):
    sys.exit()
else:
    conversion(e1_busy)
    conversion1(e2_busy) 
    start=datetime.strptime("9:00AM", "%I:%M%p")
    end=datetime.strptime("5:00PM", "%I:%M%p")
    if list1[0] > start:
       fun1()
    while k <= len(list1)-2:
        if list1[k]<list1[k+1]:
            m=""
            m+=list1[k].strftime("%-I:%M%p")
            m+="-"
            m+=list1[k+1].strftime("%-I:%M%p")
            e1_available.append(m)
            e1_duration.append(list1[k+1]-list1[k])
        k=k+2

    if end>list1[-1]:
        m=""
        m+=list1[-1].strftime("%-I:%M%p")
        m+="-"
        m+=end.strftime("%-I:%M%p")
        e1_available.append(m)
        e1_duration.append(end-list1[k])
    #print(e1_available)
    #print(e1_duration)    

    if list2[0] > start:
       fun2()
    while v <= len(list2)-2:
        if list2[v]<list2[v+1]:
            m=""
            m+=list2[v].strftime("%-I:%M%p")
            m+="-"
            m+=list2[v+1].strftime("%-I:%M%p")
            e2_available.append(m)
            e2_duration.append(list2[v+1]-list2[v])
        v=v+2

    if end>list2[-1]:
        m=""
        m+=list2[-1].strftime("%-I:%M%p")
        m+="-"
        m+=end.strftime("%-I:%M%p")
        e2_available.append(m)
        e2_duration.append(end-list2[v])
    #print(e2_available)
    #print(e1_duration)
    #print(e2_duration)
    dur=input()
    find_common(dur)
    #print(result)

