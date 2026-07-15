# 1
x = [ [5,2,3], [10,8,9]]
x[1][0]=15
print(x)

students = [
    {'first_name': 'Michael', 'last_name':'Jordan'},
    {'first_name': 'John', 'last_name':'Rosales'}
]
students[0]['last_name']="Bryant"
print(students)

sports_directory = {
    'basketball': ['Kobe','Jordan','James','Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20}]
z[0]['y']=30
print(z)

# 2
def iterateDictionary(some_list):
    for dictionary in some_list:   
        for key in dictionary:
            print(f"{key} - {dictionary[key]}")

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)

# 3
def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key_name])

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#4
def printInfo(some_list):
    for key in some_list:
        print(f"{len(some_list[key])} {key}")
        for val in some_list[key]:
            print(val)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC','Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh','Devon']
}
printInfo(dojo)