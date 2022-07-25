print("Welcome to watermelon's watermelon shop!!")
name = input("What's your name btw?\n\n")
if name == "Watermelon" or name == "watermelon" or name == "Private" or name == "private" or name == "Cold flames" or name == "cold flames":
    print("\nEverything is free for watermelon and his friends, take whatever you want")
    quit()
else:
    print("\nHey "+(name)+" what would you like to buy today?\n")
print("""    Watermelon's menu
  1-big watermelon
  2-medium watermelon
  3-smol watermelon
  4-tiny watermelon
  5-watermelon drink
  6-watermelon pie\n
Btw everything costs 6$
cuz watermelon is lazy\n""")
while True:
    purchase = input()
    if purchase == '1' or purchase == '2' or purchase == '3' or purchase == '4' or purchase == '5' or purchase == '6':
        break
    else: 
        print("\nStop saying dumbass things *sobbing* your not even making sense\n")
print("\nOk how many do you want\n")
while True:
    quantity = input()
    x = quantity.isdigit()
    if x == True:
        break
    else:
        print("\nwrite that in numbers please -_-\n")
print("\nOk so that will be" ,int(quantity) * 6 ,"dollars\n")
print("""damn thats a lot.\n
I'm low on cash right now too...
Should I run? (y/n) \n""")
while True:
    choice = input()
    if choice == "y" or choice == "Y":
        print("""\nYou start running, but then you hear something and you turn around.
Watermelon is standing FULL DIAMOND ARMOR, DIAMOND SWORD FULL PROT!
Before you understand what is happening watermelon gets a 20x combo on you and you dissappear into the void
gg""")
        quit()
    if choice == "n" or choice == "N":
        print("\nThank you come again")
        quit()
    else:
        print("\ny or n bruh\n")