import csv
file="rec.csv"
def read():
    with open(file,"r+",newline="\r\n") as o:
        hold=csv.reader(o)
        for u in hold:
            print(u)
def write():
    with open(file,"a+") as o:
        writer=csv.writer(o)
        name=input("ENter the name :")
        roll=int(input("enter the roll no:"))
        marks=int(input("enter the marks:"))
        lit=[roll,name,marks]
        writer.writerow(lit)
while True:
    print("type 1 to view records")
    print("Type 2 to Add records")
    response=int(input())
    if response==1:
        read()
    elif response==2:
        write()
    else:
        break
