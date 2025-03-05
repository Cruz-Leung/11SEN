# Get input from the user
text = input("Enter a sentence: ")

# Initialize an empty string for the result
result = ""

# Loop through using a range
for i in range(len(text)):
    if text[i].isalpha():  # Only apply the pattern to letters
        if i % 2 == 0:
            result += text[i].upper()
        else:
            result += text[i].lower()
    else:
        result += text[i]  # Keep spaces and other characters unchanged

# Display the result
print(result)