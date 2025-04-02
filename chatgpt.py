from openai import OpenAI

while True:
  OPEN_AI_KEY="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"

  print("welcome")
  print("Let's ask chatgpt something within our code:")

  question = input("enter question: ")
  start = input("Start? Yes or No: ")
  personality=0
  while not(start=="Yes" or start =="No"):
    start =input("invaild input. Please enter yes or no: ")
  if(start=="Yes"):
    print("starting")
  else:
    


    personality1 = input("enter personality trait here: ")
    start = input("Start? Yes or No: ")
    personality = 1
    while not (start == "Yes" or start =="No"):
      start =input("invaild input. Please enter yes or no: ")
    if(start=="Yes"):
      print("starting")
    else:
      personality2 = input("enter personality trait here: ")
      start = input("Start? Yes or No: ")
      personality= 2
      while not (start == "Yes" or start =="No"):
        start =input("invaild input. Please enter yes or no: ")
      if(start=="Yes"):
        print("starting")
      else:

        personality3 = input("enter personality trait here: ")
        start = input("Start? Yes or No: ")
        personality=3
        while not (start == "Yes" or start =="No"):
          start =input("invaild input. Please enter yes or no: ")
        if(start=="Yes"):
          print("starting")



  


  client= OpenAI(api_key=OPEN_AI_KEY)

  if(personality==0):
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      store=True,
      messages=[
          {"role": "user", "content":  question}
      ]
    )

    print(completion.choices[0].message);


  elif(personality==1):
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      store=True,
      messages=[
          {"role": "user", "content": personality1},
          {"role": "user", "content":  question}
      ]
    )

    print(completion.choices[0].message);

  elif(personality==2):
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      store=True,
      messages=[
          {"role": "user", "content": personality1},
          {"role": "user", "content": personality2},
          {"role": "user", "content":  question}
      ]
    )

    print(completion.choices[0].message);

  else:
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      store=True,
      messages=[
          {"role": "user", "content": personality1},
          {"role": "user", "content": personality2},
          {"role": "user", "content": personality3},
          {"role": "user", "content":  question}
      ]
    )

    print(completion.choices[0].message);

  Continue_ = input("Want to keep going? Yes or No: ")

  while not (Continue_ == "Yes" or Continue_ =="No"):
    Continue_ =input("invaild input. Please enter yes or no: ")
  if(Continue_=="Yes"):
    print("restarting")
  else:
    exit(0)


