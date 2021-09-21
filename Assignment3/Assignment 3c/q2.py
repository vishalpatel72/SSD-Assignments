import sys
sys.stdout = open('/home/vishal/Desktop/SSD/Assignment3/Q2/output.txt', 'w')
sys.stdin = open('/home/vishal/Desktop/SSD/Assignment3/Q2/date_calculator.txt', 'r')

def month(m):
        switcher={ "Jan": 1,"Feb": 2,"Mar": 3,"Apr": 4,"May": 5,"Jun": 6,"Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11,"Dec": 12 }
        return switcher.get(m,m)


def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def daysInMonth(month,year):
    while month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    while month in (4, 6, 9, 11):
         return 30
    if month==2:
        if isLeapYear(year):
             return 29
        else:
             return 28
    return 0
         

def no_of_leapYears(year):

    return int((year / 4 - year / 100 + year / 400 )) 



def countDays(year1, month1, day1, year2, month2, day2):
    
    val1 = (year1 - 1)*365 + day1


    for t in range(1 , month1):
        val1 += daysInMonth(t , year1)
    

    val1 += no_of_leapYears(year1 - 1)

    
    
    val2 = (year2 - 1)*365 + day2

    for t in range(1 , month2):
        val2 += daysInMonth(t , year2)
    
    

    val2 += no_of_leapYears(year2 - 1)
    

    print(val2 - val1)






date1 = input()
date2 = input()
bad_chars = ["-" , "/" , "st" , "th",".",","," ",":"]
for i in bad_chars :
    date1 = date1.replace(i, " ")
    date2 = date2.replace(i, " ")

x = date1.split()
y = date2.split()

if sys.argv[1]=="mm/dd/yyyy" or sys.argv[1]=="mm-dd-yyyy" or sys.argv[1]=="mm.dd.yyyy":
    mon_1=x[1]
    dat1=int(x[2][ :3])
    mon1=month(mon_1)
    mon1=int(mon1)
    ye1=int(x[3])


    mon_2=y[1]
    dat2=int(y[2][ :3])
    mon2=month(mon_2)
    mon2=int(mon2)
    ye2=int(y[3])

    countDays(ye1,mon1,dat1,ye2,mon2,dat2)

else:
    d1 = int(x[1])
    m_1 = x[2][ :3]
    m1 = month(m_1)
    m1 = int(m1)
    y1 = int(x[3])

    d2 = int(y[1])
    m_2 = y[2][ :3]
    m2 = month(m_2)
    m2 = int(m2)
    y2 = int(y[3])

    countDays(y1,m1,d1,y2,m2,d2)    






