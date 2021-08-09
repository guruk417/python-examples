
# Identify num of times each word repeats in the sentence
x = '''test.txt
hello world
this is my first python program
python is fun
hello world
hello world'''

x_list = x.split()
print([(word, x_list.count(word)) for word in set(x_list)])

print({i: x_list.count(i) for i in x_list})

input_list = [1, 2, 3, 3, 4, 4, 4]
print([(element, input_list.count(element)) for element in set(input_list)])
# print([(element, input_list.count(element)) for element in input_list])

x = [1, 2, 3]
y = [3, 4, 5]

print(set(x) ^ set(y))

def isPrimeno(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2

p = [i for i in range(1,101) if(isPrimeno(i))]
print(p)
list1 = ['a', 'b', 'c', 'd']
dict = {list1.index(i) : i for i in list1}
print(dict)

