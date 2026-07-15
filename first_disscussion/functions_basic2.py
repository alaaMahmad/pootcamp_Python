#1
def countdown(num):
    arr=[]
    for i in range(num,-1,-1):
        arr.append(i)
    return arr
print(countdown(5))

#2
def print_and_return(arr):
    print(arr[0])
    return arr[1]
arr=[2,5]
test =print_and_return(arr)
print(test)

#3
def first_plus_length(arr):
    return arr[0]+len(arr)
arr =[9,2,3,4,5,6,7]
print(first_plus_length(arr))

#4
def values_greater_than_second(arr):
    if len(arr) <2:
        return False
    new_arr =[]
    for i in range(0,len(arr),1):
        if arr[i] >arr[1]:
            new_arr.append(arr[i])
    return new_arr
arr_1=[7,3,4,1,2,6,9]
arr_2=[1]
print(values_greater_than_second(arr_1))
print(values_greater_than_second(arr_2))

#5
def length_and_value(len,val):
    arr=[]
    for i in range(0,len,1):
        arr.append(val)
    return arr
print(length_and_value(5,7))