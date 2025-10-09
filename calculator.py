from math import *

a = float(input("Введите первое число\n"))
b = float(input("Введите второе число\n"))
c = str(input("Введите операцию\n"))


class Calculator:
    def init(self, num1: int, num2: int, oper: str):  # Определяем конструктор класса Calculator,принимаем 4 параметра: self (ссылку на создаваемый экземпляр класса),num1 и num2 (числа) и oper(операцию)
        self.num1 = num1
        self.num2 = num2
        self.oper = oper

    def obuchnui(self, num1: int, num2: int, oper: str):  # Обычный калькулятор
        if oper == "*":
            print(int(num1 * num2))
        elif oper == "+":
            print(num1 + num2)
        elif oper == "-":
            print(num1 - num2)
        elif oper == "/":
            print(num1 / num2)
        else:
            print("Изивините,я не знаю такую команду")

    def injenernui(self, num1: int, num2: int, oper: str):  # Инженерный кальлкулятор
        if oper == "*":
            print(int(num1 * num2))
        elif oper == "+":
            print(num1 + num2)
        elif oper == "-":
            print(num1 - num2)
        elif oper == "/":
            print(num1 / num2)
        elif oper == "sin":
            print(sin(num1))
        elif oper == "cos":
            print(cos(num1))
        elif oper == "**":
            print(pow(num1, num2))
        elif oper == "log":
            print(log(num1, num2))

operaciya = Calculator(a, b, c)
operaciya.injenernui(a, b, c)
