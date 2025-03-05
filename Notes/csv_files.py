import csv

# Open and read the CSV file
with open("stidemts.csv", newline="") as file:
    reader = csv.reader(file)
    # next(reader) Skip the head row
    for row in reader
    name, silly_word = row
    print(f"Name: [name], Silly_Word: {silly_word}")