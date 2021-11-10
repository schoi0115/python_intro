i = 10

if i < 10:
    print("Today is not hot")
elif i > 10:
    print("Today is hot")
else:
    print("Today is a perfect weather")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(str(num1) + " is the biggest number.")
    elif num2 >= num1 and num2 >= num3:
        print(str(num2) + " is the biggest number.")
    elif num3 >= num1 and num3 >= num2:
        print(str(num3) + " is the biggest number.")

max_num(500 , 150 ,170)

your_pet = "dog"
def find_pet():
    if your_pet == "dog":
        print("Your pet is a perfect dog")
    elif your_pet == "cat":
        print("Your pet is a perfect cat")
    else:
        print("Your pet is " + your_pet)

find_pet()

def find_person(x):
    if x == x:
        print("It is " + x)

find_person("Shawn")