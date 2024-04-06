import random

class ArithmeticProblem:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
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
            self.num1 = self.num1 * self.num2
            answer = self.num1 / self.num2

        # Limit decimal places to 2
        return round(answer, 10)

def generate_arithmetic_problems(grade,y,max_decimal_places=None):
    problems = []
    if grade == 1:
        # 一年级上
        for _ in range(y):
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(6, 10)
            num2 = random.randint(6, 10)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
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
    elif grade == max_decimal_places:
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
            num2 = random.randint(1, 10)
            result = random.randint(1, 100)
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
            num2 = random.randint(1, 9)
            result = random.randint(10, 100)
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
            num1 = random.randint(1000, 9999)
            num2 = random.randint(10, 99)
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
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 99)
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 99)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 99)
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
            num1 = random.randint(1000, 9999)
            num2 = random.randint(10, 99)
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
            num1 = round(random.uniform(0.01, 100), max_decimal_places)
            num2 = round(random.uniform(0.01, num1), max_decimal_places)
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(0.01, 100), max_decimal_places)
            num2 = round(random.uniform(0.01, 100), max_decimal_places)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(0.01, 100), max_decimal_places)
            num2 = round(random.uniform(0.01, num1), max_decimal_places)
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 11:
        # 六年级上
        for _ in range(y):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(5):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, num1)
            operator = '-'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = '*'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num2 = random.randint(1, 10)
            result = random.randint(1, 100)
            num1 = result * num2
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    elif grade == 12:
        # 六年级下
        for _ in range(y):
            num1 = round(random.uniform(-100, 100), max_decimal_places)
            num2 = round(random.uniform(-100, 100), max_decimal_places)
            operator = '+'
            problems.append(ArithmeticProblem(num1, num2, operator))
        for _ in range(y):
            num1 = round(random.uniform(-100, 100), max_decimal_places)
            num2 = round(random.uniform(-100, num1), max_decimal_places)
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
            operator = '/'
            problems.append(ArithmeticProblem(num1, num2, operator))
    return problems

# 测试生成六年级下的算式
grade = 12             #年级，从1到6共12个等级，分上下册。
num_problems = 5       #4倍的num_problems，为生成的算式总数。
max_decimal_places = 1 #以结果和除数的乘积作为被除，从而生成除法运算，这个是除数和结果的最大小数位数。
problems = generate_arithmetic_problems(grade, num_problems, max_decimal_places)
for i, problem in enumerate(problems):
    print(f"题目 {i+1}: {problem.num1} {problem.operator} {problem.num2} = {problem.answer}")