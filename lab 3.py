#1
for i in range(1,11):
   print(i)
#2   
for i in range(1,11):
   print(i,"x2=",i*2)
#3
for i in range(1,51):
    if i%2==0:
        print(i)
#4
n=6
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
#5
for i in range(65,72):
 print(chr(i))
#6
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*",end="")
#7
for i in range(1,21):
   if i%2!=0:
       print(i)
#8
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#9
for i in range(6, 0, -1):
    for j in range(i):
        print('+', end=' ')
    print()
#10
n = 9
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()




                   










