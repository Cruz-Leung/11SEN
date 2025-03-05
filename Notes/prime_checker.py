def non_prime():
    print("{} is not a prime number".format(n))
def prime():
    print("{} is a prime number".format(n))

def process():
    for i in range(2, n): 
        if n % i == 0:
            non_prime()
            return  
    prime()
        
n = int(input("n: "))
if n == 1:
    non_prime()
elif n == 2 or n == 3:
    prime()
else: 
    process()


    


        



