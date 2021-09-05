
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

x[1][0] = 15
students[0]['last name']= 'Bryant'

sports_directory['soccer'][0] = "Andres"

z[0]['y'] = 30

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]

def iterateDictionary(some_list):
    

    for k in some_list:
        print(k) 
        

iterateDictionary(students)

iterateDictionary2(key, some_list):
    for dict in some_list
        print(dict[key])
iterateDictionary('first_name', students)
iterateDictionary('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):

    for key in some_dict.keys():
        print(len(some_dict[key])), key.upper())
        for val in some_dict[key]:
            print(val)
            print('\n')
printInfo(dojo)
    
    