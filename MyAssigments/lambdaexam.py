# lambda examples
'''
add = lambda x: x + 15
print(add(15))
mul = lambda x, y: x * y
print(mul(10, 15))

# Sort tuple using lambda
ip = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
ip.sort(key = lambda x: x[0])
print(ip)

# Sort dictionary using lambda
ip = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
ip.sort(key = lambda x : x['color'])

# filter even numbers and odd number from given list
ip = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_ip = list(filter(lambda x : x % 2 == 0, ip))
odd_ip = list(filter(lambda x : x % 2 != 0, ip))
print( even_ip)
print(odd_ip)

# square and cube every number in a given list of integers
ip = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq = list(map(lambda x : x * x, ip))
print(sq)
cube = list(map(lambda y : y * y * y, ip))
print(cube)

# insert section of two lists
x = [1, 2, 3, 5, 7, 8, 9, 10]
y = [1, 2, 4, 8, 9]

op = list(filter(lambda z: z in x, y))
print(op)

# count the even, odd numbers in a given array of integers
ip = [1, 2, 3, 5, 7, 8, 9, 10]

print(len(list(filter(lambda x: x % 2 == 0, ip))))
print(len(list(filter(lambda y: y % 2 != 0, ip))))

# add two lists
ip1 = [1, 2, 3]
ip2 = [4, 5, 6]
merge = list(map(lambda x, y: x + y, ip1, ip2))
print(merge)
# find numbers divisible by nineteen or thirteen from a list
ip_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
op_list = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), ip_list))
op_list.sort()
print(op_list)

# find list with maximum and minimum length
ip_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

max_length = max(len(x) for x in input_list)
max_list = max(input_list, key=lambda i: len(i))'''

