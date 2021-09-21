import json
with open("/home/vishal/Desktop/SSD/Assignment3/Assignment3a/org.json", "r") as read_file:
    data = json.load(read_file)
dict={}
for key,val in data.items(): 
    for k in val:
        if len(k) > 1:
            dict[k['name']] = k['parent']
        else:
            dict[k['name']] = "000"
read_file.close()
#print(dict)

num=int(input())





def find_leader(dict,employee):
    list1=[]
    if(employee in dict.keys()):
        while(dict[employee] != "000"):
            m = dict[employee]
            list1.append(m)
            employee = m
    #print(list1)        
    return list1

def find_commonLeader(arr,list3):
    count=0
    leader=""
   # print(list3)

    for i in list3[0]:
        #print(list3[0])
        for j in range(1,lent3):
            if i not in list3[j]:
                count=1
                break
            
        if count==0:
            leader=i
            for j in range(lent3):
                arr[j]=list3[j].index(i)+1
            break    
    return leader            



list3=[[]]*num
lent3=len(list3)              
employee = ["false" for x in range(num)]
empl = ["false" for x in range(num)]
arr = [ 0 for x in range(num)]






for i in range(num):
    employee[i]=input()
for i in range(num):
    empl[i]=employee[i]

for i in range(num):
    list3[i]=find_leader(dict,employee[i])

l=find_commonLeader(arr,list3)
#print(l)

if l!="":
    print("common leader is :" + l)
    for j in range(num):
        string="leader "+ l +" is "+str(arr[j])+" levels above "+empl[j]
        print(string)
    
else:
    print("common leader not found")



