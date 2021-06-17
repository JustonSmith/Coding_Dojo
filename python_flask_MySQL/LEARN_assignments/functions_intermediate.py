#
#

# 1.

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


def change():
    x[1][0] = 15 # 1.1
    print(x) 

    students[0]['last_name'] = 'Bryant' # 1.2
    print(students)

    sports_directory['soccer'][0] = 'Andres' # 1.3
    print(sports_directory)

    z[0] ['y'] = 30 # 1. 4
change()

# 
# 
# 

# # 2. 
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
    
# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(len(students)):
        for k, v in students[i].items():
            print(k,'-', v)

### OR ###

print(type(students))



iterateDictionary(students)



# 3.Get Values From a List of Dictionaries:
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(key, value):
    for i in value:
        print(i[value])

iterate_dictionary(students, 'first_name')

def iterate_dictionary_2(key, value):
    for i in value:
        print(i[value])

iterate_dictionary_2(students, 'last_name')


# Iterate Through a Dictionary with List Values:
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(dojo):
    num_loc = len(dojo['locations'])
    num_inst = len(dojo['instructors'])
    print(num_loc, "LOCATIONS")
    print(" ")
    for i in range(len(dojo['locations'])):
        print(dojo['locations'][i])
    print(num_inst, "INSTRUCTORS")
    print(" ")
    for i in range(len(dojo['instructors'])):
        print(dojo['instructors'][i])
print_info(dojo)

