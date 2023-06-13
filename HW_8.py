#1  *******************************************************************************************************************
print("HT#1")
def hello(imya):
    if not imya:
        print('Вітаю, Сергій!')
    else:
        print("Вітаю", imya)

name = input('Введітьсвоє ім\'я - ')
hello(name)
print()
#2  *******************************************************************************************************************
print("HT#2")
def func_bkstp(x):
    x = x ** (x / 2)
    return x

def func_stp(x):
    return x ** x

for i in range(-5, 5):
    a = func_bkstp(i)
    b = func_stp(i)
    print("F1=", a, "\n\tF2=", b)
print()
#4 ********************************************************************************************************************
print("HT#4")
def mid_sum(*num):
    suma = 0
    for i in num:
        suma += i
        return suma / 3

val = []
for i in range(3):
    val.append(int(input(f'Введіть число {i+1} - ')))
print("Список чисел - ", val)

y = mid_sum(*val)
print("Середнє арифметичне - ", round(y, 2))
print()
#5  *******************************************************************************************************************
print("HT#5")
def IMT(rost, ves):
    rez = 0
    rez = ves / (rost **2)
    if rez < 18.5:
        print(f'ІВТ={round(rez, 2)}.Дефіцит ваги тіла')
    elif 18.5 < rez <24.9:
        print(f'ІВТ={round(rez, 2)}. Норма')
    else:
        print(f'ІВТ={round(rez, 2)}. Надлишкова вага')

print("Для виходу наберіть \"off\"!")
while True:
        heigh = float(input('Введіть зріст - '))
        mass = float(input("Введіть массу - "))
        imt = IMT(heigh, mass)
        ext = input()
        if ext == "off":
            break