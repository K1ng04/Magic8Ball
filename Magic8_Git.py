# Magic 8 ball app
# source = https://en.wikipedia.org/wiki/Magic_8-Ball
from random import choice
Magic = [
    "it is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes - definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]
while True:
    Quest = input("What is your question: ")
    ans = choice(Magic)
    print(ans)
    quit = input("Would you like to quit (y/n): ")
    if quit.lower() == "n":
        Quest = input("What is your question: ")
        ans = choice(Magic)
        print(ans)
    elif quit.lower() == "y":
        print("Thanks for Playing!!")
        break
    else:
        print("Please enter y/n")
        quit2 = input("y/n: ")
        if quit2.lower() == "y":
            print("Thanks for Playing!!")
            break
        elif quit2.lower() == "n":
            print("Continue Playing!")
        else:
            break
