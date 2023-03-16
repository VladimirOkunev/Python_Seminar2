"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть"""


from random import randint

coin_number = int(input('Введите количество монет: '))
count = 0
pos_resh = 0
pos_orel = 0
while count < coin_number:
    coin_pos = randint(0,1)
    print(coin_pos, end =' ')
    if coin_pos == 0:
        pos_resh += 1
    else:
        pos_orel += 1
    count += 1
if pos_orel < pos_resh:
    print(f'\n Необходимо перевернуть {pos_orel} монет')
else:
    print(f'\n Необходимо перевернуть {pos_resh} монет')