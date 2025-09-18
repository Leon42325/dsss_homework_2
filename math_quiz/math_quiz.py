import random


def random_number(num1, num2):
    """
    Generate a random integer between num1 and num2.
    """
    return random.randint(num1, num2)


def random_operator():
    """
    Generate a random operator.
    """
    return random.choice(['+', '-', '*'])


def calculate(n1, n2, operator):
    """
    Do the calculation.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+': result = n1 + n2
    elif operator == '-': result = n1 - n2
    else: result = n1 * n2
    return problem, result

def math_quiz():
    """
    Quiz
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = random_number(1, 10); n2 = random_number(1, 5); o = random_operator()

        PROBLEM, ANSWER = calculate(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except ValueError:
            print("Wrong input.")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
