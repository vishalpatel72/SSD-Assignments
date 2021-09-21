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



dictionary={}

listA=[[]]*num

lent=len(listA)

employee = ["false" for x in range(num)]

arr = [ 0 for x in range(num)]






for i in range(num):
    employee[i]=input()


for i in range(num):
    dictionary[i]=find_leader(dict,employee[i])
i=0
for val in dictionary.values():
    listA[i]=val
    i+=1

#print(listA)

res = list(set.intersection(*map(set, listA)))
print(res)

if not res:
    print("no common leader found")
else:  
    print("common leader is:"+ res[0])

for k in range(lent):
    arr[k]=listA[k].index(res[0])+1

#print(arr)

for k in range(num):
    string= " leader " +res[0]+ " is " + str(arr[k]) +" levels above "+employee[k]
    print(string)

