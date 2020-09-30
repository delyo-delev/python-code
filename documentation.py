# my code:
validation = input().split()
input_from_user = input()

user_name = validation[0]
password = validation[1]

while input_from_user != password:
    input_from_user = input()

print(f"Welcome {user_name}")


name = input()
ascii_sum = 0

for i in range(len(name)):
    ascii_sum += ord(name[i])
print(f"ASCII sum of name {name} is {ascii_sum}")


text = input()
for i in range(len(text) - 1, 0 - 1, -1):
    print(text[i], end=" ")

for j in reversed(text):  # text[::-1]
    print(j, end=" ")


# lists:
strings_list = ["1", "2", "3", "4", "5", "6"]
numbers_list = (list(map(lambda x: int(x), strings_list)))
print(numbers_list)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter((lambda x: x % 2 == 0), list_of_numbers))
print(even_numbers)


def cube(n):
    return n * 3


print(list(map(cube, [1, 2, 3, 4, 5, 6])))
print(list(map(lambda n: n * 3, [1, 2, 3, 4, 5, 6])))

print(list(enumerate([1, 2, 3, 4, 5, 6])))

strings = ["Python", "SoftUni", "Programing basics"]
list_comprehension = [word for word in strings if len(word) > 3]
print(list_comprehension)

for word in strings:
    if len(word) > 3:
        print(word, end=", ")

print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_comprehension = [num * 2 for num in numbers if num % 2 == 0]
print(list_comprehension)

for num in numbers:
    if num % 2 == 0:
        num *= 2
        print(num, end=", ")

print()

numbers_list = (list(filter((lambda num: num % 2 == 0), numbers)))
print(numbers_list)


def my_filter(function, items):
    new_items = []

    for item in items:
        if function(item):
            new_items.append(item)

    return new_items


special_numbers = [1, 2, 3, 4, 5, 6]

result = (my_filter(lambda x: x % 2 == 0, special_numbers))
print(result)

result_two = (list(filter((lambda x: x % 2 == 0), special_numbers)))
print(result_two)

result_three = (list(map(lambda x: x * 2, special_numbers)))
print(result_three)

random_numbers = [2, 4, 6, 2, 5, 6, 1, 3, 6, 4, 2, 5, 10]
unique_numbers = list(set(random_numbers))
print(unique_numbers)

# dictionaries:
my_dictionary = {
    1: "Python Fundamentals",
    2: "Python Advanced",
    3: "Python OOP"
}

for key in my_dictionary.keys():
    print(key, end=" ")

print()

for value in my_dictionary.values():
    print(value, end=" ")

print()

for (key, value) in my_dictionary.items():
    print(f"Key: {key}, Value: {value}")

if 1 in my_dictionary:
    print(my_dictionary[1])

if 2 in my_dictionary.keys():
    print(my_dictionary[2])

if "Python OOP" in my_dictionary.values():
    print("Python OOP")

x = lambda a, b: a * b
print(x(3, 4))

x = lambda a: a + 10
print(x(5))

full_name = lambda first_name, last_name: f"My name is {first_name} {last_name}"
print(full_name("Delyo", "Delev"))

my_dictionary = {
    "Delyo": 33,
    "Valentin": 5,
    "Daniela": 34
}

sorted_dictionary = dict(sorted(my_dictionary.items(), key=lambda x: x[1]))
print(sorted_dictionary)

another_sorted_dictionary = dict(sorted(my_dictionary.items(), key=lambda x: (-x[1], x[0])))
print(another_sorted_dictionary)

# text processing:
string = "Python Fundamentals"
print(string[slice(0, 6)])
print(string[0:6])

print("23".isdigit())
print("name".isalpha())
print("PYTHON".islower())

print("hello".upper())
print("HELLO".lower())
print(" Python ".strip())

text = "My name is Delyo"
print(text.replace("Delyo", "Valentin"))
