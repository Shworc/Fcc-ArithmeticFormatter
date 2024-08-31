def arithmetic_arranger(problems, show_answers=False):
    #print(problems[1])
    #problem_count = 
    first_line = ""
    second_line = ""
    separator_line = ""
    answer_line = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        num1, operator, num2 = problem.split()

        if not num1.isnumeric() or not num2.isnumeric():
            return "Error: Numbers must only contain digits."
        
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if operator == '+':
            answer = str(int(num1) + int(num2))
        else:
            answer = str(int(num1) - int(num2))

    width = max(len(num1), len(num2)) + 2

    first_line += num1.rjust(width) + "    "
    second_line += operator + num2.rjust(width - 1) + "    "
    separator_line += "-" * width + "    "
    answer_line += answer.rjust(width) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + separator_line.rstrip()

    if show_answers:
        arranged_problems += "\n" + answer_line.rstrip()
    return arranged_problems
    
    
"""
problem_count0 = int(problems[0].split(' ')[0])
problem_count01 = str(problems[0].split(' ')[1])
problem_count02 = int(problems[0].split(' ')[2])
count_lines = len(problems[0])
result1 =  (problem_count0 + problem_count02) if problem_count01 == '+' else (problem_count0 - problem_count02)
print(f"{problem_count0} {problem_count01} {problem_count02}\n{count_lines * '-'}\n{result1}")
if problem_count01 != '+' and problem_count01 != '-':
    print("Error: Operator must be '+' or '-'.")
problem_count2 = problems[1]
problem_count3 = problems[2]
print(f"{problem_count2}\n{problem_count3}")


return problems
"""
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')