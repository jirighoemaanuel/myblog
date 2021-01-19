from random import randint

# first exercise
# name = input('name: ')
# name = name + ' '
# print(name * randint(1, 10))


# second exercise
user_seconds = int(input('how many seconds? '))
mins = user_seconds // 60
seconds = mins * 60 - user_seconds
print(f'{mins}minutes and {abs(seconds)}seconds')
