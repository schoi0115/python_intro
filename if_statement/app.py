i = 5

if i <= 10:
    print("Today is not hot")
elif i >= 10:
    print("Today is hot")

is_male = False
is_tall = False

if is_male and is_tall: # and will be has to both condition True. or needs to be one of the condition needs to be True
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a male but not tall")
elif is_tall and not(is_male):
    print("You are tall but not male") 
else:
    print("You are not a male and not tall")