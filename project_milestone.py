#name: Joey
#date: 4/7/2025
#description: A fun game to play.
from openai import OpenAI
import threading
import random
import time

#importing the things i'm using

usersinput=False
gamemessages =[]
#making the list
loop = True
#this is to keep the game looping
day = 1
#the starting day
food = 3
water = 3
#starting food & water
die = False
#this is put as false to keep the game for dying imeditally
print("you have food & water for 3 days")
#telling the user the amount of food & water they have
print("if you don't have food or water for that day you die")
#telling the user what happens if they don't have food or water
while loop == True:
    
    time.sleep(5)
    #this is so the game doesn't go to fast
    use = True
    #use is for the use of food & water
    random_integer = random.randint(1, 5)
    if day >1:
        print("random day")
        #debuging
        if(random_integer == 5):
            userinput = input("what would you like to try today?: ")
            users = ("this is the user input: ",userinput)
            gamemessages.append(users)
            usersinput = True
            #this is for the user to try something in that day


    print(day)
    #telling the user what day they are on
    base = "You are the master of the game you will give a choice each day on events of that day."
    story = "There is a zombie apocalypse and the user is all alone they may meet people, friends or foes. their goal is to get out of their city. get help. or find a cure."
    game = "please end each message off with 1 of the 3 choices. (Alive) or (Dead) or (Won). depending on what happened in that day. NO MORE THAN 1 of those choices"
    wincondition = "win condition only happens if you get help, go somewhere else(like a city), or somehow stop the zombie plague."
    choices = "you can only make no more then 1 choices in a day"
    wincondition2 = "the win condtions should be rare to happen. dying should be uncommon then winning, and alive is common"
    response = "please don't add new lines or '\n'"
    foodgain = "if during that day the user found food please put: foodgain. at the end of the text"
    watergain = "if during that day the user found water please put: watergain. at the end of the text"
    noworries = "don't track their thirst or hunger as that is seperatly done"
    days = "this is the current day: ",day
    someting ="no more than 1 choice per day"
    before_the_day = "if the user asks something before the day starts try to follow through with it. example: 'I want to look for food'"
    give_food = "try your best to give food & water to the user because they can lose if you don't"
    #this is for telling chatgpt what is needed & not needed for this game
    ultimate_text=base+"\n"+story+"\n"+game+"\n"+wincondition+"\n"+choices+"\n"+wincondition2+"\n"+watergain+"\n"+foodgain+"\n"+noworries+"\n"+response+"\n"+someting+"\n"+str(days)+"\n"+before_the_day+"\n"+give_food
    if usersinput == True:
        ultimate_text = ultimate_text+"\n"+users
        usersinput = False

    OPEN_AI_KEY=""
    client= OpenAI(api_key=OPEN_AI_KEY)
    completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
            {"role": "user", "content": ultimate_text},
            {"role": "user", "content": "\n".join(gamemessages)}
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
    
    death = output.rfind("(Dead)")
    print("dead: "+str(death))
    if death >= 0:
        die = True
    #exit(0)
    if die == True:
        loop= False
        print("you died")
        print("you survived: ", day)
        exit(0)
        #checking if the user died & telling them how long they survived & ending the game
    
    win = output.rfind("(Won)")
    #exit(0)
    print("win: "+str(win))
    if win >= 0:
        loop= False
        print("you Won")
        print("you took: ", day,+"'s")
        exit(0)
        #checking if the user won & telling them how long it took & ending the game
    foods = output.rfind("Foodgain")
    waters = output.rfind("Watergain")    
    if foods >= 0:
        random_food = random.randint(1,3)
        food = food+random_food

    if waters >= 0:
        random_water = random.randint(1,3)
        water = water+random_water

    da = "its still the same day"
    if(random_integer == 5 and day > 1):
        gamemessages.append(str(users))
    outputs = "This was your response for that day: "+output
    gamemessages.append(str(outputs))
    #adding stuff to a list so chatgpt knows what it did prefcally  
    output = ""
    try:
        dids = int(input("if they're was a choice in that day put 1, if not put 0: "))

    except ValueError:
        while dids !=int:
            dids = input("invaild value please enter again: ")
    
    if dids > 0: 
        choose = input("input which choice you want to do: ")
        ultimate_text=base+"\n"+story+"\n"+game+"\n"+wincondition+"\n"+choices+"\n"+wincondition2+"\n"+watergain+"\n"+foodgain+"\n"+noworries+"\n"+choose+"\n"+da+"\n"+response+"\n"+"no more than 1 choice per day"+"\n"+str(days)+"\n"+before_the_day+"\n"+give_food
        
        
        completion = client.chat.completions.create(
                model="gpt-4o-mini",
                store=True,
                messages=[
                {"role": "user", "content": ultimate_text},
                {"role": "user", "content": "\n".join(gamemessages)}
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

        choice = "this was they players choice ",choices
        gamemessages.append(str(choice))
        outputs = "This was your response for that day",output
        gamemessages.append(str(outputs))
    
    death = output.rfind("(Dead)")
    print("dead: "+str(death))
    if death >= 0:
        die = True
    #exit(0)
    if die >= True:
        loop= False
        print("you died")
        print("you survived: ", day)
        exit(0)


    win = output.rfind("(Won)")
        #exit(0)
    print("win: "+str(win))
    if win >= 0:
        loop= False
        print("you Won")
        print("you took: ", day,+"day's")
        exit(0)
        #checking if the user won & telling them how long it took & ending the game
    foods = output.rfind("Foodgain")
    waters = output.rfind("Watergain")    
    if foods >= 0:
        random_food = random.randint(1,3)
        food = food+random_food

    if waters >= 0:
        random_water = random.randint(1,3)
        water = water+random_water



    time.sleep(10)
    #another wait
    day=day+1
    #adding a day




    
def foodwater_control():
    global die
    global use
    global food
    global water
    #making most of the varibles global to use throughout my code
    while die == False:
      #this stop if the player dies
        if use == True:
            #only runs at the start of a day
            water = water-1
            food = food-1
            #using the food & water
            use = False
            #so this doesn't loop
            print("you have: ",food,"food ","& ",water,"")
            #telling the user how much food & water they have left
            if water == -1:
                die=True
            elif food == -1:
                die = True
                #this is for if they run out of food for that day
                    


    #def print_letters():


thread1 = threading.Thread(target=foodwater_control)
#making the thread for food & water
#thread2 = threading.Thread(target=print_letters)

thread1.start()
#this starts the thread up.
#thread2.start()

thread1.join()
#this actually runs the thread
#thread2.join()




#{"role": "user", "content":  }
