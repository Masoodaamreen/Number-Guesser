import random as r
b=r.randint(0,101)
def numberguess():
    a=int(input("Enter your guess = "))
    if a>100:
       print( "WOAH! That's beyond high, Try in between 0-100")
       return numberguess()
    elif a==b+1 or a==b+2:
        print ("You are too close")
        return numberguess()
    elif a>b:
        print( "The number is too high")
        return numberguess()
    elif a==b-1 or a==b-2:
        print("you are too close")
        return numberguess()
    elif a<b:
        print("The nummber is too small")
        return numberguess()
    elif a==b:
        return f"Hurray! you are correct it is {b}!"
     
print(numberguess())