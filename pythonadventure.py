name = input("type your name:")
print("welcome",name,"to this adventure")

answer = input("you are on a dirt road and which way you would like to go?".lower())
if answer == "left":
    answer = input("you come to the riveer and now either you can walk or swim young one for the journey has to come and u must go on.Type walk to walk and swim to swim  ")
    if answer == "walk":
        print("young warrior u have started to walk go on man ")
    elif answer == "swim":
        print("sorry bro u fall inside a waterfall")
    else:
        print("sorry bro ")

elif answer == "right":
    answer = input("ok u gonna go to market or brothel.Type market to go to market and brothel for going to brothel ")
    if answer == "market":
        print("you are on the market")
    elif answer == "brothel":
        print("you are on the brothel")
    else:
        print("sorry bro")
else:
    print("invalid question")





