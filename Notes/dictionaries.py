'''
# array.list 
results = [99,60,30,40,50]
students = ["Cruz", "Harry", "Ben", "briscoe", "Zac"]
print(f"{students[0]} received a score of {results[0]}")
'''

results = [
{"Name": "Cruz", "Englsih": 55, "Maths": 85},
{"Name": "Nathan", "Englsih": 100, "Maths": 30},
{"Name": "Hans", "Englsih": 75, "Maths": 25},
{"Name": "Tom", "Englsih": 535, "Maths": 90},
{"Name": "Ben", "Englsih": 100, "Maths": 20}
]
'''
for result in results:
    print(f"{result["Name"]}'s grades are {result["English"]} and {result["Maths"]}")
'''


total = 0
for result in results:
    total += results["Maths"]
avg = total / len(results) 
print(avg)