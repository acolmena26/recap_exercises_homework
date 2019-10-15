num_read = 0
print("This program reads any numbers you input and will print the biggest one")
request = "Give me a number that you want to compare"
error = "That was not a valid number"

read = input("please give me a number to put as max nums to compare")
max_number = float(read)

max = 0
while num_read < max_number:
    try:
        read_line = input(request)
        num = float(read_line)
    except ValueError:
        print(error)
        continue
    if num_read == 0:
        max = num
    elif num > max:
        max = num
    num_read += 1

print("The biggest number read was ", max)

#change for max N numbers, where N is a number typed by the user
