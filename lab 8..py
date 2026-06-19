#1
a={1:"jai",2:"kishore",3:"pranav",4:"hari"}
print(a)
#2
a={"jai":98,"kishore":88,"pranav":93,"hari":77}
print(a["jai"])
#3
a={1:"jai",2:"kishore",3:"pranav",4:"hari"}
a[3]="vishnu"
print(a)
#4
a={"jai":98,"kishore":88,"pranav":93,"hari":77}
highest=max(a,key=a.get)
print(highest)
#5
a={"jai","kishore"}
b={"pranav","hari"}
a.update(b)
print(a)
#6
a=str(input("enter:"))
print(len(a))
#7
a={1,2,5,6,7,89,1000}
highest=max(a)
print(highest)
#8
a={1,2,5,6,7,89,1000}
lowest=min(a)
print(lowest)
#9
a={1,2,3,4,1000}
print(sum(a))
#10
def student(name,roll,dep):
   print(name,roll,dep)
student("jai",38,"ece")
#11
def calculate(m1,m2,m3):
   print(m1+m2+m3)
calculate(98,99,100)
#12
def greeting_user(name,message="hi"):
   print(name,message)
greeting_user('jai'
#13
def rectangle(length,area):
   print(length*area)
rectangle(2,3)
#14
def add(*args):
    return sum(args)
print(add(10,20,30))
#15
def multiply(*args):
    result=1
    for i in args:
        result=result*i
    print(result)
    
multiply(2,3,4)
    
