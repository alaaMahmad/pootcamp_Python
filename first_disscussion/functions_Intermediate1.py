import random

def randInt(min=0, max=100):
    if max < 0:
        return "max must be greater than 0"
    
    temp=0
    if min > max:
        temp = min
        min = max
        max =temp

    num = random.random() * (max - min) + min
    return round(num)


print(randInt())  
print(randInt(max=-5))  
print(randInt(min=100,max=0))           
print(randInt(max=50))        
print(randInt(min=50))        
print(randInt(min=50, max=200))

