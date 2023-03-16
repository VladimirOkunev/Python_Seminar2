"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел 
S и их произведение P. Помогите Кате отгадать задуманные Петей числа."""

import math

sum = int(input('Введите сумму чисел: '))
mult = int(input('Введите произведение чисел: '))

discr = sum ** 2 - 4 * 1 * mult

if discr > 0:
    x = (sum + math.sqrt(discr)) / (2 * 1)
    y = sum - x
    print(f'Число X = {x} \nЧисло Y = {y}')
elif discr == 0:
    x = sum / (2 * 1)
    y = sum - x
    print(f'Число X = {x} \nЧисло Y = {y}')
else:
    print("Введите другие числа")