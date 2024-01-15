import random
import time

def get_operator():
    operators = ('+', '-', '*', '/')
    rand_op = random.choice(operators)
    return rand_op

def random_number():
    min_num = 0
    max_num = 11
    number = random.randint(min_num, max_num)
    return number

def start_game():
    problems_printed = 0
    i = 1
    while problems_printed < 10:
        operand1 = random_number()
        operand2 = random_number()
        operator = get_operator()
        if operator == '/':
            if operand2 == 0 or operand1 % operand2 != 0:
                continue
        
        expression = f"{operand1} {operator} {operand2}"
        computer_answer = int(eval(expression))
        user_answer = int(input(f"Problem No. {i}:   {expression} = "))

        while computer_answer != user_answer:
            user_answer = int(input(f"Problem No. {i}:   {expression} = "))

        problems_printed += 1
        i += 1

if __name__ == '__main__':
    start_time = time.time()
    start_game()
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    print(f"You completed all math problems in {time_taken} seconds.")
