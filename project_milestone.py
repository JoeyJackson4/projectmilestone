from openai import OpenAI
import threading
import random
import time
"""for i in (1,10,1):
    message = input("please enter message: ")
    messages = []
    messages.append(message)
    messages.insert(1, "h")
    print(messages)"
    """

gamemessages =[]
loop = True
day = 1
food = 3
water = 3
die = False
print("you have food & water for 3 days")
print("if you don't have food or water for that day you die")
while loop == True:

    time.sleep(5)
    use = True







    

    random_integer = random.randint(1, 5)
    if day >1:
        print("random day")
        
        if(random_integer == 5):
            userinput = input("what would you like to try today?: ")
            users = ("this is the user input: ",userinput)
            





    base = "You are the master of the game you will give a choice each day on events of that day."
    story = "There is a zombie apocalypse and the user is all alone they may meet people, friends or foes. their goal is to get out of their city. get help. or find a cure."
    game = "please end each message off with 1 of the 3 choices. (Alive) or (Dead) or (Won). depending on what happened in that day. NO MORE THAN 1 of those choices"
    wincondition = "win condition only happens if you get help, go somewhere else(like a city), or somehow stop the zombie plague."
    choices = "you can only make no more then 2 choices in a day"
    wincondition2 = "the win condtions should be rare to happen. dying should be less rare then winning, and alive is common"
    response = "please don't add new lines or '\n'"
    foodgain = "if during that day the user found food please put: foodgain. at the end of the text"
    watergain = "if during that day the user found water please put: watergain. at the end of the text"
    noworries = "don't track their thirst or hunger as that is seperatly done"


    OPEN_AI_KEY="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"
    client= OpenAI(api_key=OPEN_AI_KEY)
    if(random_integer == 5 and day > 1):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
            {"role": "user", "content": base},
            {"role": "user", "content": story},
            {"role": "user", "content": game},
            {"role": "user", "content": wincondition},
            {"role": "user", "content": userinput},
            {"role": "user", "content": choices},
            {"role": "user", "content": wincondition2},
            {"role": "user", "content": watergain},
            {"role": "user", "content": foodgain},
            {"role": "user", "content": noworries},
            {"role": "user", "content": gamemessages},
            {"role": "user", "content": response}
            ]
            )
        output = str(completion.choices[0].message)
        output = output.replace("\n"," ")
        output = output.replace("\n\n"," ")
        output = output.replace("\n1"," ")
        output = output.replace("\n2"," ")
        output = output.replace("refusal=None","")
        output = output.replace("role='assistant'","")
        output = output.replace("annotations=[],","")
        output = output.replace("audio=None,","")
        output = output.replace("function_call=None,","")
        output = output.replace("tool_calls=None","")
        print(output)
        
        
    else:
        completion = client.chat.completions.create(
                model="gpt-4o-mini",
                store=True,
                messages=[
                {"role": "user", "content": base},                
                {"role": "user", "content": story},
                {"role": "user", "content": game},
                {"role": "user", "content": wincondition},
                {"role": "user", "content": choices},
                {"role": "user", "content": wincondition2},
                {"role": "user", "content": watergain},
                {"role": "user", "content": foodgain},
                {"role": "user", "content": noworries},
                {"role": "user", "content": gamemessages},
                {"role": "user", "content": response}
                ]
                )
        
        
        output = str(completion.choices[0].message)
        output = output.replace("\n"," ")
        output = output.replace("\n\n"," ")
        output = output.replace("\n1"," ")
        output = output.replace("\n2"," ")
        output = output.replace("refusal=None"," ")
        output = output.replace("role='assistant,"," ")
        output = output.replace("annotations=[],"," ")
        output = output.replace("audio=None,"," ")
        output = output.replace("function_call=None,"," ")
        output = output.replace("tool_calls=None"," ")
        print(output)
    death = output.rfind("(Dead)")
    if death == 0:
        die = True
    #exit(0)
    if die == True:
        loop= False
        print("you died")
        print("you survived: ", day)
        exit(0)
    
    win = output.rfind("(Won)")
    #exit(0)
    if win == 0:
        loop= False
        print("you Won")
        print("you took: ", day,+"'s")
        exit(0)



    day=day+1
    if(random_integer == 5 and day > 1):
        gamemessages.append(users)
    outputs = "This was your response for that day",output
    gamemessages.append(outputs)
    time.sleep(10)




    
def foodwater_control():
    global die
    global use
    global food
    global water
    while die == False:
        if use == True:
            water = water-1
            food = food-1
            use = False
            print("you have: ",food,"food ","& ",water,"")
            if water == 0:
                die=True
            elif food == 0:
                die = True
                    


    #def print_letters():


thread1 = threading.Thread(target=foodwater_control)
    #thread2 = threading.Thread(target=print_letters)

thread1.start()
    #thread2.start()

thread1.join()
    #thread2.join()



#{"role": "user", "content":  }
