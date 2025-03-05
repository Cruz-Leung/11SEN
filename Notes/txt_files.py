# Open and read the text file 
with open("students.txt", "r") as file: # 'r' = READ ONLY, (security measure) ; 'w' = write 
    for line in file:
        name, secret_word = line.strip().split(", ")
        print(f"Name {name}, Silly Word: {secret_word}")