# 1) A self-checkout kiosk at a grocery store needs to display a countdown timer 
# (from 10 to 1) before automatically canceling an inactive session. 
# The system should print numbers from 1 to 10 to show the time remaining before
#  session expiration.


for i in range(10,0,-1):
    print(i)

counter=10
while counter>=1:
    print(counter)
    counter-=1

#________________________________________________________

# finding_prime_numbers
def findPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    
    return True
    
def listOfPrimes(n):
    listt=[]
    for i in range(2,n+1):
        if findPrime(i):
            listt.append(i)
    return listt
    
ans=listOfPrimes(100)
print(ans)
#__________________________________________________________
#Finding all list of armstrongs, and given number is armstrong or not

def findArmstrong(number):
    original=number
    length=len(str(number))
    sum=0
    while number>0:
        digit=number%10
        sum+=digit**length
        number//=10
        
    if original==sum:
        return True
    else:
        return False
    
def listOfArmStrongs(start,end):
    listt=[]
    for i in range(start,end+1):
        if findArmstrong(i):
            listt.append(i)
    return listt

ans=listOfArmStrongs(1,1000)
print(ans)


#Finding Non_prime_number and sum of non_primes in the given number


def findNonPrime(n):
    if n<=1:
        return True
    for i in range(2,n):
        if n%i==0:
            return True
    
    return False
    
def sumOfNonPrime(number):
    sum=0
    while number>0:
        digit=number%10
        if findNonPrime(digit):
            sum+=digit
        number//=10
    return sum
    
ans=sumOfNonPrime(3436)
print(ans)

# Find the smallest prime digit in the number.e.g., 2357196
def findSmallPrime(number):
    small=10
    while number>0:
        digit=number%10
        if digit in [2,3,5,7]:
            if digit<small:
                small=digit
        number//=10
    if small==10:
        return "No small Primes found in the given range"
    else:
        return small

ans=findSmallPrime(2357196)
print(ans)

#finding NextPrime number
def findPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
def nextPrime(n):
    next=n+1
    while True:
        if findPrime(next):
            return next
        next+=1

ans=nextPrime(43)
print(ans)


# Your task is to write a program that finds the nearest prime number to a given input number N

#     Sample inputs: 8                           input: 21
#                  output: 7                  output: 19,23


def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
def nextPrime(n):
    # if isPrime(n):
    #     return n
    lower=n-1
    upper=n+1
    
    while True:
        if (lower)>=2 and isPrime(lower):
            return lower
        if isPrime(upper):
            return upper
        lower-=1
        upper+=1

ans=nextPrime(71)
print(ans)


#Finding the lower and upper bounds both

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nearestPrimes(n):
    # Find nearest lower prime
    lower = n - 1
    while lower >= 2 and not isPrime(lower):
        lower -= 1
    
    # Find nearest upper prime
    upper = n + 1
    while True:
        if isPrime(upper):
            break
        upper += 1

    return lower, upper

# Example usage
num = 43
lower_prime, upper_prime = nearestPrimes(num)
print("Nearest lower prime:", lower_prime)
print("Nearest upper prime:", upper_prime)


