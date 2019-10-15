# print("This program asks for a number and tests if it is prime")
# while True:
#     try:
#         read_line = input("Please give me an integer number")
#         num = int(read_line)
#     except ValueError:
#         print("That was not a valid integer number")
#         continue
#     break
# for i in range (2, num // 2):
#     if num % i == 0:
#         print("The number", num, "is not prime")
#         exit()
# print("The number", num, "is prime")

# generate 100 numbers, print only the prime ones
import random

mylist = []
prime_list = []
for i in range(0,100):
    x = random.randint(1,100)
    mylist.append(x)

print(mylist)

def isPrime(num):
    if num < 2 or num == 4:
        return False
    for i in range (2, num // 2):
        if num % i == 0:
            return False
    return True

for num in mylist:
    if isPrime(num):
        prime_list.append(num)
print(prime_list)
