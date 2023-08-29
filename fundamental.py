#Exercise 1
name = 'John Smith'
age = 20
is_patient = False

#Exercise 2
full_name = input("Hi, what is your name? ")
fav_colour = input("What is your favourite colour? ")
print(full_name + ' likes ' + fav_colour)

#Exercise 3
print("Simple age calculator")
birth_year = input("What is your birth year? ")
current_year = input("Enter current year: ")
age = int(current_year) - int(birth_year)
print(age)

#Exercise 4
weight_in_lbs = input("Enter your weight (in lbs): ")
temp_weight = 0.454 * float(weight_in_lbs)
weight_in_kg = str(temp_weight)
print("Your weight in kg: " + weight_in_kg)

#Exercise 5
name = 'Jennifer'
print(name) # should print 'ennife'

#Exercise 6
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
msg = f'Hi, {first_name} [{last_name}]'
print(msg)

#Exercise 7
house_price = 1000000
is_good_credit = False
if is_good_credit:
    house_price -= house_price*0.1
else:
    house_price -= house_price * 0.2
final_price = house_price
print(int(final_price))

#Exercise 8
weight = input("Weight: ")
option = input("(L)bs or (K)g: ")
if option.lower() == 'l' or option.upper() == 'L':
    weight = float(weight)/0.45
    print("You are: " + str(round(weight)) + " lbs")
elif option.lower() == 'k' or option.upper() == 'K':
    weight = float(weight)*0.45
    print("You are: " + str(round(weight)) + " kg")
else:
    print("Invalid input!")

#Exercise 9
car_started = False
car_stopped = False

while True:
    input_command = input()
    if input_command.lower() == 'help':
        print("start - to start the car")
        print("stop - to stop the car")
        print("exit - to exit")
    elif input_command.lower() == 'start':
        if car_started:
            print("The car is already started! Stop repeating this command!")
        else:
            print("Car ready to go!")
            car_started = True
    elif input_command.lower() == 'stop':
        if car_stopped:
            print("The car is already started! Stop repeating this command!")
        else:
            print("Car stopped!")
            car_stopped = True
    elif input_command.lower() == 'exit':
        break
    else:
        print("I don't understand that")

#Exercise 10
number_list = [3,9,4,11,42,37]
max_num = number_list[0]
for number in number_list:
    if number > max_num:
        max_num = number
print(max_num)

#Exercise 11
numbers = [2,2,2,2,5]
for count1 in numbers:
    output = ''
    for count2 in range(count1):
        output += 'x'
    print(output)

#Exercise 12
numbers = [1,3,5,12,22,4,66,19]
max_num = numbers[0]
for count in numbers:
    if max_num < count:
        max_num = count
print(max_num)