#1
for i in range(0,151,1):
    print(i)
#2
for i in range(5,1001,5):
    print(i)
#3
for i in range(1,101,1):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("coding")    
    else:
        print(i)
#4
result=0
for i in range(500001):
    if i%2 !=0:
        result +=i
print(result)

#5
for i in range(2018,0,-4):
    print(i)

#6
low_num = 1
high_num = 25
mult = 5
for i in range(low_num,high_num+1):
    if i%mult==0:
        print(i)