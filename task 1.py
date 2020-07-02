"""+Поработайте с переменными, создайте несколько, выведите на экран,
+запросите у пользователя несколько чисел и строк и сохраните в
+переменные, выведите на экран."""



name = input("Введите ваше имя: ")
number = input("Введите любое число в промежутке от 1 до 100: ")
print ("Привет", name)
print ("Вы ввели", number)


time = int(input("Введите время в секундах "))
hour= time/3600
minute= time - (hour*3600)/60
second=time - (hour*3600)/60
print (f"Введеное время равно {hour}:{minute}:{second}")

a= int(input("Введите целое положительное число от 1 до 10  "))
if a<10:
    aa=a*11
    aaa=a*111
    sum=a+aa+aaa
    print("Сумма чисел в формате a+aa+aaa равна", sum)
else:
    print("Вы ввели не верное число")

revenue = int(input("Введите сумму выручки вашей фирмы  "))
expences = int(input("Введите сумму расходов вашей фирмы  "))
if revenue < expences:
    loss = expences - revenue
    print("Убыток", loss)
else:
    profit = revenue - expences
    ratio=profit/revenue
    print("Прибыль", profit)
    print("Рентабельность", ratio)

