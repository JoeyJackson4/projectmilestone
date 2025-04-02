from openai import OpenAI
import threading
import random
"""for i in (1,10,1):
    message = input("please enter message: ")
    messages = []
    messages.append(message)
    messages.insert(1, "h")
    print(messages)"
    """
loop = True
day = 1
while loop == True:



    

    random_integer = random.randint(1, 5)
    if day >1:
        print("random day")

        if(random_integer == 5):
            userinput = input("what would you like to try today?: ")




    base = "You are the master of the game you will give a choice each day on events of that day."
    story = "There is a zombie apocalypse and the user is all alone they may meet people, friends or foes. their goal is to get out of their city. get help. or find a cure."
    game = "please end each message off with 1 of the 3 choices. (Alive) or (Dead) or (Won). depending on what happened in that day. NO MORE THAN 1 of those choices"
    wincondition = "win condition only happens if you get help, go somewhere else(like a city), or somehow stop the zombie plague."
    choices = "you can only make no more then 2 choices in a day"
    wincondition2 = "the win condtions should be rare to happen. dying should be less rare then winning, and alive is common"
    response = "please don't add new lines or '\n'"


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
            {"role": "user", "content": response}
            ]
            )
        output = str(completion.choices[0].message)
        output = output.replace("\n"," ")
        output = output.replace("\n\n"," ")
        output = output.replace("\n1"," ")
        output = output.replace("\n2"," ")
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
                {"role": "user", "content": response}
                ]
                )
        
        
        output = str(completion.choices[0].message)
        output = output.replace("\n"," ")
        output = output.replace("\n\n"," ")
        output = output.replace("\n1"," ")
        output = output.replace("\n2"," ")
        print(output)
    loop = False
    day=day+1



    #if completion:


    #def print_numbers():


    #def print_letters():


    #thread1 = threading.Thread(target=print_numbers)
    #thread2 = threading.Thread(target=print_letters)

    #thread1.start()
    #thread2.start()

    #thread1.join()
    #thread2.join()



#{"role": "user", "content":  }
