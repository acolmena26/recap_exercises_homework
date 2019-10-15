import random
print("This program generates 4 random numbers than prints the biggest one")
a = random.random()*100
b = random.random()*100
c = random.random()*100
d = random.random()*100

print("I have generated these numbers: %.2f %.2f %.2f %.2f" % (a, b, c, d))
if a >= b and a >= c and a >= d:
    print("The biggest number is %.2f" % a)
    if b >= c and b >= d:
        print("The second biggest number is %.2f" % b)
    elif c >= b and c >= d:
        print("The second biggest number is %.2f" % c)
    else:
        print("The second biggest number is %.2f" % d)

elif b >= a and b >= c and b >= d:
    print("The biggest number is %.2f" % b)
    if a >= c and a >= d:
        print("The second biggest number is %.2f" % a)
    elif c >= a and c >= d:
        print("The second biggest number is %.2f" % c)
    else:
        print("The second biggest number is %.2f" % d)
elif c >= a and c >= b and c >= d:
    print("The biggest number is %.2f" % c)
    if a >= b and a >= d:
        print("The second biggest number is %.2f" % a)
    elif b >= a and b >= d:
        print("The second biggest number is %.2f" % b)
    else:
        print("The second biggest number is %.2f" % d)
else:
    print("The biggest number is %.2f" % d)
    if a >= b and a >= c:
        print("The second biggest number is %.2f" % a)
    elif b >= a and b >= c:
        print("The second biggest number is %.2f" % b)
    else:
        print("The second biggest number is %.2f" % c)

# determine the second largest number

