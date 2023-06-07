# Напишіть функцію change(lst),
# яка приймає список і змінює місцями його перший і останній елемент.
# У вихідному списку щонайменше 2 елементи
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


input_list = []
while len(input_list) < 2:
    input_list = input('Enter a list separated by spaces: ').split()
    if len(input_list) < 2:
        print('List must contain at least 2 elements!')

final_list = change(input_list)
print(f'Here is your transformed list: {final_list}')

# Напишіть функцію to_dict(lst),
# яка приймає аргумент у вигляді списку і повертає словник, в якому кожен елемент списку є ключем і значенням.
# Передбачається, що елементи списку відповідатимуть правилам завдання ключів у словниках.


def to_dict(lst):
    return {item: item for item in lst}


initial_list = input('Enter a list separated by spaces: ').split()
final_dict = to_dict(initial_list)
print('Here is a dict from your list:', final_dict)

# Напишіть функцію sum_range(start, end),
# яка підсумовує всі цілі числа від значення start до величини end включно.
# Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.


def sum_range(start, end):
    if start > end:
        start, end = end, start

    total = 0
    for num in range(start, end + 1):
        total += num
    return total


while True:
    try:
        start = int(input('Enter initial number: '))
        break
    except ValueError:
        print('Initial number must be a whole number!')

while True:
    try:
        end = int(input('Enter final number: '))
        break
    except ValueError:
        print('Final number must be a whole number!')

sum_result = sum_range(start, end)
print(f'The sum of numbers in range from {start} to {end} is {sum_result}')
