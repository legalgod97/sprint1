def even_numbers(end):
    for i in range(0, end + 1, 2):
        yield i

even_numbers_list = even_numbers(10)
for number in even_numbers_list:
    print(number)