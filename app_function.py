import random
import math

class ArithmeticProblem:
    def __init__(self, num1, num2, operator):
        self.num1 = round(num1,3)
        self.num2 = round(num2,3)
        self.operator = operator
        self.answer = self.calculate_answer()

    def calculate_answer(self):
        if self.operator == '+':
            answer = self.num1 + self.num2
        elif self.operator == '-':
            answer = self.num1 - self.num2
        elif self.operator == '*':
            answer = self.num1 * self.num2
        elif self.operator == '/':
            # Avoid division by zero
            if self.num2 == 0:
                self.num2 = random.randint(1, 100)
            # Ensure divisible
            answer = self.num1 / self.num2
            answer = round(answer,4)

        # Limit decimal places to 2
        return round(answer, 10)

def generate_arithmetic_problems(grade,y,max_decimal_places=None):
    problems = []
    if grade == 1:
        # 一年级上
        for _ in range(y):
            num1 = random.randint(1, 5)
            num2 = random.randint(6, 10)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(6, 10)
            num2 = random.randint(10, 15)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 10)
            num2 = random.randint(10, 20)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 2:
        # 一年级下
        for _ in range(y):
            num1 = random.randint(1, 20)
            num2 = random.randint(1, num1)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            operator = random.choice(['+', '-'])
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 20)
            num2 = random.randint(1, num1)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            operator = random.choice(['+', '-'])
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 3:
        # 二年级上
        for _ in range(y):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 10)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = random.randint(1, 10)
            result = random.randint(1, 100)
            num1 = result * num2
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 10)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = random.randint(1, 10)
            result = random.randint(1, 100)
            num1 = result * num2
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 4:
        # 二年级下
        for _ in range(y):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, num1)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = random.randint(1, 100)
            result = random.randint(1, 10)
            num1 = result * num2
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 5:
        # 三年级上
        for _ in range(y):
            num1 = random.randint(1, 10000)
            num2 = random.randint(1, 100)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 10000)
            num2 = random.randint(1, 100)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(10, 100)
            num2 = random.randint(1, 9)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = random.randint(1, 50)
            result = random.randint(1, 100)
            num1 = result * num2
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 6:
        # 三年级下
        for _ in range(y):
            num1 = random.randint(100, 1000)
            num2 = random.randint(10, 100)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(100, 1000)
            num2 = random.randint(10, 100)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 99)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
          #  num1 = random.randint(1000, 9999)
            num2 = random.randint(1, 100)
            result = random.randint(1, 50)
            num1 = result * num2
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 7:
        # 四年级上
        for _ in range(y):
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 99)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = random.randint(1, 50)
            result = random.randint(1, 200)
            num1 = result * num2
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 99)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = random.randint(1, 50)
            result = random.randint(1, 200)
            num1 = result * num2
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 8:
        # 四年级下
        for _ in range(y):
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(10, 100)
            num2 = random.randint(10, num1)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 99)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
         #   num1 = random.randint(1000, 9999)
            result = random.randint(1,100)
            num2 = random.randint(1, 100)
            num1=num2*result
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 9:
        # 五年级上
        for _ in range(y):
            num1 = round(random.uniform(0.01, 100), max_decimal_places)
            num2 = round(random.uniform(0.01, 100), max_decimal_places)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(0.01, 100), max_decimal_places)
            num2 = round(random.uniform(0.01, num1), max_decimal_places)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(0.01, 10), max_decimal_places)
            num2 = round(random.uniform(0.01, 10), max_decimal_places)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = round(random.uniform(0.01, 10), max_decimal_places)
            result = round(random.uniform(0.01, 100), max_decimal_places)
            num1 = result * num2
            num1 = round(num1,3)
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 10:
        # 五年级下
        for _ in range(y):
            num1 = round(random.uniform(0.01, 100), max_decimal_places)
            num2 = round(random.uniform(0.01, 100), max_decimal_places)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = round(random.uniform(0.01, 10), max_decimal_places)
            result = round(random.uniform(0.01, 100), max_decimal_places)
            num1 = result * num2
            num1 = round(num1, 3)
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(0.01, 100), max_decimal_places)
            num2 = round(random.uniform(0.01, 100), max_decimal_places)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = round(random.uniform(0.01, 10), max_decimal_places)
            result = round(random.uniform(0.01, 100), max_decimal_places)
            num1 = result * num2
            num1 = round(num1, 3)
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 11:
        # 六年级上
        for _ in range(y):
            num1 = round(random.uniform(-5000, 5000), max_decimal_places)
            num2 = round(random.uniform(-2000, 2000), max_decimal_places)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(-5000, 5000), max_decimal_places)
            num2 = round(random.uniform(-2000, 2000), max_decimal_places)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(-10, 10), max_decimal_places)
            num2 = round(random.uniform(-10, 10), max_decimal_places)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = round(random.uniform(-10, 10), max_decimal_places)
            result = round(random.uniform(-100, 100), max_decimal_places)
            num1 = result * num2
            num1 = round(num1, 3)
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 12:
        # 六年级下
        for _ in range(y):
            num1 = round(random.uniform(-5000, 5000), max_decimal_places)
            num2 = round(random.uniform(-2000, 2000), max_decimal_places)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(-5000, 5000), max_decimal_places)
            num2 = round(random.uniform(-2000, 2000), max_decimal_places)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(-100, 100), max_decimal_places)
            num2 = round(random.uniform(-20, 20), max_decimal_places)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = round(random.uniform(-20, 20), max_decimal_places)
            result = round(random.uniform(-200, 200), max_decimal_places)
            num1 = result * num2
            num1 = round(num1, 3)
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    return problems
