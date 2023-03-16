"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

number = int(input('Введите число: '))

exponent = 0
temp = 1
while temp <= number:
    temp *= 2
    print(exponent, end=' ')
    exponent +=1