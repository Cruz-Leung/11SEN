import sys
import random
from time import sleep 
from dictionary import questions # input dictionary {questions} from dictionary.py   
from leaderboard_input import update_leaderboard # input leaderboard functions from leaderboard.py 


def typewriter(words): # typewriter effect
    for char in words:
        sleep(0.00) 
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in '.!?,:': # pause longer at certain times
            sleep(0.5)
    sys.stdout.write("\n\n") # space between sentences

def divider(): # divider in between sections
    print("\n\n" + "*" * 100 + "\n") # divider: 2 new lines before, 100 '*', 2 new lines after

def header(text): # special header effect
    print("\n" + "=" * len(text)) 
    print(text)
    print("=" * len(text) + "\n")


############################################## MAIN FUNCTIONS ##############################################

# Function to welcome user
def welcome(): # Welcome screen before entering Home page
    typewriter("Welcome to ultimate knowledge quiz.")
    typewriter("Test your skills across different categories and compete for the top 5 spot at the leaderboard")
    typewriter("You can ask for hints by typing 'hint' if you're stuck, but be careful, you only have 2 hints per question.")
    typewriter("Every question has a maximum of 3 attempts, each correct answer will give you 1 point.")
    typewriter("if you have reached the maximum attempts, you will move to the next question without gaining a point")
    typewriter("In order to put your name on the leaderboard, you must complete all categories.")
    typewriter("Good luck, and have fun!")
    typewriter("Please enter your name: ")


    name = ""
    while name == "": # loop until name is entered
        name = input("> ").strip() # strips spaces
        if name == "": # condition when name is empty
            typewriter("You've got to have a name. Please enter your name.")

    # Variables to make a banner
    word = list(name)
    syntax = "-" * 5
    rows = 3 
    message = ["W", "E", "L", "C", "O", "M", "E"]
    single = "-" * (len(word) * 2 + 18)
    for i in range(rows): # Loops through variables to print welcome banner
        if i == 1:
            print(syntax, end= " ")
            print(" ".join(message) + ", " + " ".join(word).upper() + " !", end= "") # end= "" to print on the same line, taken from stacks oveflow
            print(" " + syntax)
        else: 
            print(syntax + single + syntax)
    typewriter("created by Cruz...") # wateramrk
    divider()
    return name # returns name to be used in leaderboard


# Function to choose category
def choose_category(imported_questions, played_categories, name, score): # Home page with categories
    header("HOME PAGE")
   
    
    
    if len(played_categories) == 3: # checks if all categories have been played
        typewriter("Congratulations! You have managed to complete the quiz.")
        typewriter("You have played all the categories.")
        print("Did you make it to the leaderboard?")

        divider()
        header("LEADERBOARD")
        update_leaderboard(name, score) # updates leaderboard in leaderboard.py
        print("\n")
        print(f"Your final score for the quiz is: ")
        print(f"{name} - {score}")
        score = 0 # reset score
        played_categories = [] # reset played categories
        typewriter("Would you like to play again?")
        typewriter("Please type 'yes' or 'no'.")
        restart_response = input("> ").lower().strip()
        while restart_response != "":
            if restart_response == "yes":
                main()
            elif restart_response == "no":
                typewriter("Thank you for playing.")
                sys.exit("END OF QUIZ") # exits the quiz if condition met
            else:
                typewriter("Invalid response, please type 'yes' or 'no'.")
            restart_response = input("> ").lower().strip()
        


    typewriter("This quiz offers multiple categories for you to test yourself.")
    categories = [] # empty list to store categories
    typewriter("The categories are:")
    divider()
    for i in imported_questions:  # loop through topics without duplicates
        topic = i["Topic"]
        if topic not in categories and topic not in played_categories: #checks if topic is not in the list
            typewriter(topic) 
            categories.append(topic)
    divider()

    typewriter("Please choose a category above to begin the quiz.")
    chosen_category = input("> ").lower().strip() # input category 
    
    while True: # loop until category is chosen
        if chosen_category == "": # condition when category is empty    
            typewriter("Please choose a category to begin the quiz.")
        elif chosen_category not in categories: # checks if category is not in the list
            typewriter("Invalid category, please input one of the categories shown above.")
        elif chosen_category in played_categories:
            typewriter("You have already played this category, please choose another category.")
        else:
            print("You have selected {}.".format(chosen_category))
            played_categories.append(chosen_category)
            return chosen_category, played_categories
        chosen_category = input("> ").lower().strip()


# Function to print questions based on chosen category
def print_questions(imported_questions, played_categories, chosen_category, score, name, section_score): # prints questions based on chosen category
    divider() 
    header(chosen_category.upper()) # header with chosen category
    typewriter("Are you ready for the questions?")
    typewriter("Remember to input the letter of the answer.")
    typewriter("Good luck!") 
    divider()


    choice_limit = ["A", "B", "C", "D", "E"] # limit choices to A, B, C, D 

    random.shuffle(imported_questions) # shuffle questions

    for question in imported_questions:
        if question["Topic"] == chosen_category: # checks if topic matches chosen category
            typewriter(question["Question"])
            choices = (question["Choices"].split(",")) # split choices by comma
            for choice in choices: 
                typewriter(choice)

            hint_count = 0 # innitialize hint count
            incorrect_attempt = 0

            while True: # loop until correct answer is given
                answer = input("Enter your answer: ").strip().upper()

                # start validation
                if answer == "HINT": 
                    if hint_count == 0:
                        typewriter(question["HINT"])
                        hint_count += 1
                    elif hint_count == 1:
                        typewriter(question["HINT2"])
                        hint_count += 1
                    else:
                        typewriter("Sorry, no more hints available.")

                elif answer not in choice_limit:
                    typewriter("Invalid choice, please input a valid choice.")
                    
                elif answer == question["Answer"]:
                    typewriter("Correct!")
                    section_score += 1
                    hint_count = 0 # reset hint count
                    typewriter(f"Your section score is {section_score}.")
                    break
                
                else: # validation after incorrect answer
                    typewriter("Incorrect")
                    incorrect_attempt += 1
                    if incorrect_attempt == 2: # second last
                        typewriter("One more attempt left, make it count!")
                    if incorrect_attempt == 3: # maximum attempts
                        typewriter("Sorry, you have reached the maximum attempts.")
                        typewriter(f"The correct answer is {question['Answer']}, {question["display_answer"]}.")
                        typewriter(f"Your section score is {section_score}.")
                        break
                    if hint_count < 2: # different hints depending on hint and incorrect attempt count
                        if incorrect_attempt == 1 and hint_count == 0:
                            typewriter(f"Hint: {question["HINT"]}")
                            hint_count += 1
                        elif incorrect_attempt == 1 and hint_count == 1:
                            typewriter(f"Hint: {question["HINT2"]}")
                            hint_count += 1
                        if incorrect_attempt == 2 and hint_count == 1:
                            typewriter(f"Hint: {question["HINT2"]}")
                            hint_count += 1
                    elif incorrect_attempt == 2 and hint_count == 2: 
                        typewriter("Remember the two hints given.")
                        typewriter(f"{question['HINT']}")
                        typewriter(f"{question['HINT2']}")
                    typewriter("Try again.")
            divider()    
                
    hint_count = 0 # reset hint count                                 
    typewriter("Congratulations, you have this section of the quiz!")
    typewriter(f"Your section score is {section_score}.")
    typewriter("Would you like to try another section?")
    typewriter("Please type 'yes' or 'no'.")
    response = input("> ").lower().strip()
    while response != "":
        if response == "yes":
            score += section_score # add section score to total score
            section_score = 0
            chosen_category, played_categories = choose_category(imported_questions, played_categories, name, score)
            print_questions(imported_questions, played_categories, chosen_category, score, name, section_score)
        elif response == "no":
            typewriter("Thank you for playing.")
            score += section_score # add section score to total score
            typewriter(f"You score in this section is {section_score}.")
            typewriter(f"Your final score of the quiz is {score}.")
            section_score = 0 # reset section score
            score = 0 # reset score
            sys.exit("END OF QUIZ") # exits the quiz if condition met
            
        else:
            typewriter("Invalid response, please type 'yes' or 'no'.")
        response = input("> ").lower().strip()

############################################## MAIN FUNCTIONS ##############################################

# Main function to call functions
def main(): # main function
    played_categories = []
    section_score = 0 # score for each section
    score = 0 # main score
    name = welcome()
    imported_questions = questions
    chosen_category, played_categories = choose_category(imported_questions, played_categories, name, score) #this allows user to choose a category and returns the chosen category
    print_questions(imported_questions, played_categories, chosen_category, score, name, section_score)

main()
