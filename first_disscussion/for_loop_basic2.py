#1
def biggie_size(arr):
    new_arr=[]
    for i in range(len(arr)):
        if arr[i]<0:
            new_arr.append(arr[i])
        else:
            new_arr.append("big")
    return new_arr
arr=[-1,3,-2,5,-5]
print(biggie_size(arr))

#2
def count_positives(list):
    count = 0
    for num in list:
        if num > 0:
            count += 1
    list[len(list)-1] = count
    return list
print(count_positives([-2, 1, 5, -1])) 


#3
def sum_total(list):
    count =0
    for num in list:
        count +=num
    return count
arr=[1,4,2,3]
print(sum_total(arr))

# 4
def average(list):
    sum =sum_total(list)
    avg =sum/len(list)
    return avg
arr=[1,4,2,3]
print(average(arr))

# 5
def length(list):
    count = 0
    for val in list:
        count += 1
    return count

print(length([37, 2, 1, -9])) 
print(length([]))   

# 6
def minimum(list):
    if len(list) == 0:
        return False
    temp=list[0]
    for val in list:
        if val<temp:
            temp =val
    return temp
print(minimum([5,2,7,9,1,5,6,4]))
#  7
def maximum(list):
    if len(list) == 0:
        return False
    temp=list[0]
    for val in list:
        if val>temp:
            temp =val
    return temp
print(maximum([5,2,7,9,1,5,6,4]))

# 8
def ultimate_analysis(list):
    if len(list) == 0:
        return {'sumTotal': 0, 'average': 0, 'minimum': None, 'maximum': None, 'length': 0}

    dic_for_list = {
        "sumTotal": sum_total(list),
        "average": average(list),
        "minimum": minimum(list),
        "maximum": maximum(list),
        "length": length(list) 
    }
    return dic_for_list

print(ultimate_analysis([5, 2, 7, 9, 1, 5, 6, 4]))
print(ultimate_analysis([]))

def reverse_list(list):
    for i in range(0,len(list),1):
        right=(len(list)-1)-i
        temp=0
        if i<right:
            temp =list[i]
            list[i]=list[right]
            list[right]=temp
    return list
print(reverse_list([1,2,3,4,5,6]))