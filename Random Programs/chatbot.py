import random

question1 = ("How old are you?")
question2 = ("What is your name?")
question3 = ("How is your day?")
question4 = ("What is your Favorite Color?")
question5 = ("Want to Hang out sometime?")

replysad1 = ("Feels Bad.")
replysad2 = ("Thats too bad.")
replygood1 = ("Thats Great!")
replygood2 = ("Awesome!")
replygood3 = ("Cool!")
replynorm1 = ("Okay.")
replynorm2 = ("Alright.")

questionAll = ([question1, question2, question3, question4, question5])
questionNew = random.choice(questionAll)

print(questionNew)
if (questionNew == question1):
    a = int(input())
    if (a >= 16):
        reply16old = random.choice(["Wow, you can drive now! Cool!", replygood1, replygood2, replygood3])
        print(reply16old)
    elif (a < 16 and a > 0):
        replyrandomgood = random.choice([replygood1, replygood2, replygood3 ])
        print(replyrandomgood)
    elif (a <= 0):
        print("Wait thats not right... But Okay!")
if (questionNew == question2):
    a = input( )
    replyname = random.choice(["Nice Name!", "I feel like I heard that name before.", replygood1, replygood2, replygood3])
    print(replyname)
if (questionNew == question3):
    a = input ( )
    if (a == "good" or a == "okay"):
        print("Thats good to here!")
    elif (a == "bad" or a == "not great"):
        replydaysad = random.choice([replysad1, replysad2])
        print(replydaysad)
    else:
        replyday = random.choice([replynorm1, replynorm2])
        print(replyday)
if (questionNew == question4):
    a = input( )
    favcolor = random.choice(["blue", "red", "purple"])
    hatedcolor = random.choice(["green", "orange", "yellow"])
    if (a == favcolor):
        print("Wow "+ favcolor +" is my favorite color too!")
    elif (a == hatedcolor):
        print("Oh, I don't really like"+ hatedcolor)
    else:
        replycolor = random.choice([replygood1, replygood2, replygood3, "Thats a good color.", "Cool! My favorite color is "+ favcolor])
        print(replycolor)
if (questionNew == question5):
    a = input( )
    if (a == "yes" or a == "okay" or a == "alright"):
        print("Alright when?")
        a = input( )
        print("Oh I'm busy " + a)
    elif (a == "no" or a == "never"):
        replynohang = random.choice([replysad1, replysad2, "Oh, I guess I'll be alone", "Well I'll just ask someone else later"])
        print(replynohang)
    else:
        replyelsehang = random.choice([replynorm1, replynorm2])
        print(replyelsehang)

questionAll.remove(questionNew)
questionNew = random.choice(questionAll)
print(questionNew)

if (questionNew == question1):
    a = int(input())
    if (a >= 16):
        reply16old = random.choice(["Wow, you can drive now! Cool!", replygood1, replygood2, replygood3])
        print(reply16old)
    elif (a < 16 and a > 0):
        replyrandomgood = random.choice([replygood1, replygood2, replygood3 ])
        print(replyrandomgood)
    elif (a <= 0):
        print("Wait thats not right... But Okay!")
if (questionNew == question2):
    a = input( )
    replyname = random.choice(["Nice Name!", "I feel like I heard that name before.", replygood1, replygood2, replygood3])
    print(replyname)
if (questionNew == question3):
    a = input ( )
    if (a == "good" or a == "okay"):
        print("Thats good to here!")
    elif (a == "bad" or a == "not great"):
        replydaysad = random.choice([replysad1, replysad2])
        print(replydaysad)
    else:
        replyday = random.choice([replynorm1, replynorm2])
        print(replyday)
if (questionNew == question4):
    a = input( )
    favcolor = random.choice(["blue", "red", "purple"])
    hatedcolor = random.choice(["green", "orange", "yellow"])
    if (a == favcolor):
        print("Wow "+ favcolor +" is my favorite color too!")
    elif (a == hatedcolor):
        print("Oh, I don't really like "+ hatedcolor)
    else:
        replycolor = random.choice([replygood1, replygood2, replygood3, "Thats a good color.", "Cool! My favorite color is "+ favcolor])
        print(replycolor)
if (questionNew == question5):
    a = input( )
    if (a == "yes" or a == "okay" or a == "alright"):
        print("Alright when?")
        a = input( )
        print("Oh I'm busy " + a)
    elif (a == "no" or a == "never"):
        replynohang = random.choice([replysad1, replysad2, "Oh, I guess I'll be alone", "Well I'll just ask someone else later"])
        print(replynohang)
    else:
        replyelsehang = random.choice([replynorm1, replynorm2])
        print(replyelsehang)

questionAll.remove(questionNew)
questionNew = random.choice(questionAll)
print(questionNew)

if (questionNew == question1):
    a = int(input())
    if (a >= 16):
        reply16old = random.choice(["Wow, you can drive now! Cool!", replygood1, replygood2, replygood3])
        print(reply16old)
    elif (a < 16 and a > 0):
        replyrandomgood = random.choice([replygood1, replygood2, replygood3 ])
        print(replyrandomgood)
    elif (a <= 0):
        print("Wait thats not right... But Okay!")
if (questionNew == question2):
    a = input( )
    replyname = random.choice(["Nice Name!", "I feel like I heard that name before.", replygood1, replygood2, replygood3])
    print(replyname)
if (questionNew == question3):
    a = input ( )
    if (a == "good" or a == "okay"):
        print("Thats good to here!")
    elif (a == "bad" or a == "not great"):
        replydaysad = random.choice([replysad1, replysad2])
        print(replydaysad)
    else:
        replyday = random.choice([replynorm1, replynorm2])
        print(replyday)
if (questionNew == question4):
    a = input( )
    favcolor = random.choice(["blue", "red", "purple"])
    hatedcolor = random.choice(["green", "orange", "yellow"])
    if (a == favcolor):
        print("Wow "+ favcolor +" is my favorite color too!")
    elif (a == hatedcolor):
        print("Oh, I don't really like"+ hatedcolor)
    else:
        replycolor = random.choice([replygood1, replygood2, replygood3, "Thats a good color.", "Cool! My favorite color is "+ favcolor])
        print(replycolor)
if (questionNew == question5):
    a = input( )
    if (a == "yes" or a == "okay" or a == "alright"):
        print("Alright when?")
        a = input( )
        print("Oh I'm busy " + a)
    elif (a == "no" or a == "never"):
        replynohang = random.choice([replysad1, replysad2, "Oh, I guess I'll be alone", "Well I'll just ask someone else later"])
        print(replynohang)
    else:
        replyelsehang = random.choice([replynorm1, replynorm2])
        print(replyelsehang)

questionAll.remove(questionNew)
questionNew = random.choice(questionAll)
print(questionNew)

if (questionNew == question1):
    a = int(input())
    if (a >= 16):
        reply16old = random.choice(["Wow, you can drive now! Cool!", replygood1, replygood2, replygood3])
        print(reply16old)
    elif (a < 16 and a > 0):
        replyrandomgood = random.choice([replygood1, replygood2, replygood3 ])
        print(replyrandomgood)
    elif (a <= 0):
        print("Wait thats not right... But Okay!")
if (questionNew == question2):
    a = input( )
    replyname = random.choice(["Nice Name!", "I feel like I heard that name before.", replygood1, replygood2, replygood3])
    print(replyname)
if (questionNew == question3):
    a = input ( )
    if (a == "good" or a == "okay"):
        print("Thats good to here!")
    elif (a == "bad" or a == "not great"):
        replydaysad = random.choice([replysad1, replysad2])
        print(replydaysad)
    else:
        replyday = random.choice([replynorm1, replynorm2])
        print(replyday)
if (questionNew == question4):
    a = input( )
    favcolor = random.choice(["blue", "red", "purple"])
    hatedcolor = random.choice(["green", "orange", "yellow"])
    if (a == favcolor):
        print("Wow "+ favcolor +" is my favorite color too!")
    elif (a == hatedcolor):
        print("Oh, I don't really like"+ hatedcolor)
    else:
        replycolor = random.choice([replygood1, replygood2, replygood3, "Thats a good color.", "Cool! My favorite color is "+ favcolor])
        print(replycolor)
if (questionNew == question5):
    a = input( )
    if (a == "yes" or a == "okay" or a == "alright"):
        print("Alright when?")
        a = input( )
        print("Oh I'm busy " + a)
    elif (a == "no" or a == "never"):
        replynohang = random.choice([replysad1, replysad2, "Oh, I guess I'll be alone", "Well I'll just ask someone else later"])
        print(replynohang)
    else:
        replyelsehang = random.choice([replynorm1, replynorm2])
        print(replyelsehang)

print("I'd best be going now... Have a good day!")
