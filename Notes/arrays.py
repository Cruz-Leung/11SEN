scores = [5, 7, 9, 31, 11]

def max_search(scores):
    item = 0
    max = 0
    
    while item < len(scores):
        if scores[item] > max:
            max = scores[item]
        item += 1
    return max

print(max_search(scores))