def greet(name):
    return f"Hello, {name}"

def calc_avg(scores):
    num_sub = len(scores)
    average_score = sum(scores) / num_sub if num_sub > 0 else 0
    return num_sub, average_score

def res(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = input("Enter student's name: ")
    scores_input = input("Enter scores separated by spaces: ")
    scores = [float(score) for score in scores_input.split()]
    
    greeting = greet(name)
    num_sub, average_score = calc_avg(scores)
    result = res(average_score)
    print(greeting)
    print(f"Subjects: {num_sub}")
    print(f"Average Score: {average_score}")
    print(f"Result: {result}")


main()
