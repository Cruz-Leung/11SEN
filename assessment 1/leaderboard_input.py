# Description: This file contains the leaderboard_standings list and the update_leaderboard function. The leaderboard_standings list contains a dictionary with the name and score of the player. The update_leaderboard function takes in the name and score of the player and appends it to the leaderboard_standings list. It then prints the leaderboard.
import os # find file path

# Tried to put score and name in python dictionary but it doesn't save after the function ends
# txt file code from class notes, modified by copilot to fit code

# Tried to do it withut os, but file wasn't found. 
leaderboard_file = os.path.join(os.path.dirname(__file__), "leaderboard") # os module to specify file path
leaderboard_standings = []

# Load and read the leaderboard file
def load_leaderboard(): 
     with open(leaderboard_file, "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            leaderboard_standings.append({"name": name, "score": int(score)})
        return leaderboard_standings
    
# Save the new score to the file
def save_leaderboard(leaderboard_standings):
    with open(leaderboard_file, "w") as file:
        for i in leaderboard_standings:
            file.write(f"{i['name']}, {i['score']}\n")

leaderboard_standings = load_leaderboard()

def update_leaderboard(name, score): # updates leaderboard with name and score with conditions
    leaderboard_standings.append({"name": name, "score": score})

    # Sort the leaderboard by score in descending order 
    # Attempted to do it by putting dictionary in a single variable but didn't work
    # Taken from stacks overflow, modified to fit code
    leaderboard_standings.sort(key=lambda x: x["score"], reverse=True) 
    if len(leaderboard_standings) > 5: # condition to keep only top 5 scores
        leaderboard_standings.pop() # line found in stack overflow

    save_leaderboard(leaderboard_standings) # saves leaderboard to file

    for i in leaderboard_standings:
        print(f"{i['name']} - {i['score']}") # prints leaderboard
