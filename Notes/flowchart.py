#calculate the first grade for a student
# based on 3 assesment scores entenred using a loop
# Displkay the results (average.)


def main():
    scores = []
    collect_scores(scores)
    while len(scores) != 3:
        scores = collect_scores(scores)
    average = calculate_average(scores)
    grade = determine_grade(average)
    display_results(average, grade)

def collect_scores(scores):
    for i in range(3):
        score = int(input("Enter score: "))
        scores.append(score)
        return scores

def calculate_average(scores):
   average = average(scores)
   return average

def determine_grade(average):
    if average >= 90:
        grade = "Band 6"
    elif average >= 80:
        grade = "Band 5"
    elif average >= 70:
        grade = "Band 4"
    else: 
        grade = "Fail"
    return grade 

def display_results(average, grade):
    print("Average: {average}, Grade: {grade}")

def display_you_suck():
    print("you suck")
main()