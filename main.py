
count = 0

def lol():
    global count
    global name
    print(f"{name} is wrong.\n{name} lose")
    calculate()
    exit()

def calculate():
    global count
    global name
    amount = count * 100000
    dollar=format(amount)
    print(f"{name} won ${dollar}")
    t= "THANKS FOR PLAYING"
    print(t.center(80))

def million():
  global name
  cent = f"{name} is a millionaire ${count*100000}"
  print(cent.center(80))

def won():
    global count
    global name
    count += 1
    print(f"{name} are correct!!!\n{name} won $100000")
    if count == 3:
        million()

a = "Welcome to the game"
b = a.capitalize()
print(b.center(80))
name= input("Enter your name:")

d = "Rules of the game are very simple"
c = d.capitalize()
print("If one question is answered incorrectly, your game will end.")
print("For each correct answer, you will win $100000.")

ask = input("Are you ready? (YES/NO): ")

if ask.lower() == "no":
    exit()
elif ask.lower() == "yes":
    l = ['What is the capital of England', 'What is the national bird of Australia', 'Who invented the light bulb']
    answer1 = input(l[0] + ": ")

    if answer1.lower() == "london":
        won()
    else:
        print("the correct answer is London")
        lol()
    answer2 = input(l[1] + ": ")

    if answer2.lower() == "emu":
        won()
    else:
        print("the correct answer is emu")
        lol()

    answer3 = input(l[2] + ": ")
    if answer3.lower() == "thomas edison":
        won()
    else:
        print("the correct answer is thomas edison")
        lol()

else:
    print("Please enter 'YES' or 'NO' to start the game.")
