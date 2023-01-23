import math

def zadacha1():

#Задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.60 -> 2, 2, 3, 5

    n=(int(input('Задайте число N: ')))
    i = 2
    List = []
    while i <= n:
        if n % i == 0:
            List.append(i)
            n //= i
            i = 2
        else:
            i += 1
    print(List)


def zadacha2():
    #Задача 2. В первой строке файла находится информация об ассортименте мороженного,
    #во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
    # Пример:
    # 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
    # 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
    # Ответ.Закончилось «Бурёнка»

    data = open('icecream.txt', mode = 'r', encoding = 'utf-8')
    text = data.readlines()
    data.close()
    print(text)


    icecream_assort = set(text[0].removesuffix('\n').split(', '))
    icecream_fact = set(text[1].removesuffix('\n').split(', '))
    print(icecream_assort)
    print(icecream_fact)

    result = icecream_assort - icecream_fact
    print(result)

def zadacha3():
    #     Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
    # 3 -> 3.142
    n = int(input('Введите количество знаков после запятой для числа Пи: '))
    print (round(math.pi,n))


# zadacha1()
# zadacha2()
# zadacha3()