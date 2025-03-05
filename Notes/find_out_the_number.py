def find_odd_one_out(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]

    if len(evens) == 1:
        print(f"{evens[0]} is the even one out")
    else:
        print(f"{odds[0]} is the odd one out")

numbers = list(map(int, input("Enter numbers: ").split()))
find_odd_one_out(numbers)

# Find outs which number is the odd one out