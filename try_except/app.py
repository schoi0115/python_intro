try:
    #value = 10 / 0 #cannot process try but except catches the error right away
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid Input")
'''

This is a bad practice using only except: . Use error code.
except:
    print("Invalid Input")
'''