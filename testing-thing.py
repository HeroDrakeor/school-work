import random 


number = random.randint(0,100003840) # Randomly generates a number. 
if number <= 24415:
    print("You found a ✨Shiny✨ number!")
    isShinyNumber = True # Just a little cosmetic thing, doesn't do anything special. Dunno if it can generate though, haven't had it naturally happen.
else:
    isShinyNumber = False
float(number)
i = 2
wantToContinue = "Y"


with open("testing-thing.csv", "a", newline="") as fp: # Puts the generated number into testing-thing.csv
    fp.write(f"{number}""\n")



while wantToContinue == "Y":
    while i <= (number / 2):
        if number % i == 0:
            print(f"The number generated, {number}, is not a prime number.")
            print("It is divisible by", i)
            isShinyNumber = False 
            break
        i += 1 
        if i == 45000000: # From here till line 47 is cosmetic, things for the program to print while the user waits.
            print("I'm surprised you got this message. Good job!") 
        elif i == 40000000:
            print(f"I'm out of space for messages. This is the home-stretch.")
        elif i == 20000000:
            print("I don't know how many more messages I can give you. How have you not left. You really want to know if that number is prime, huh?") 
        elif i == 10000000:
            print("So... have you found a shiny number? They're about 1/4096, so don't be discouraged if you don't find one.") 
        elif i == 7000000:
            print("I'm losing contact. Give me a moment.")
        elif i == 5000000:
            print("How large is this number?!")
        elif i == 4000000: 
            print("How long will this go?")
        elif i == 3000000:
            print("Damn. That's just tragic.")
        elif i == 2000000:
            print("Someone's unlucky")
        elif i == 1000000:
            print("This one's a bit tricky.")


    if i > (number / 2) and isShinyNumber == True:
        print("This number is a ✨shiny✨ prime!") # I don't actually know the odds of a shiny prime.
        print(number)
        break
    elif i > (number / 2):
        print(number, "is prime")
        break



    wantToContinue = input("Do you want to continue? Y/N ")
    wantToContinue = wantToContinue.upper()
    if wantToContinue == "Y":
        number /= i
        i = 2
    else:
        break
print("Bye bye!")