#from openai import OpenAI

for i in (1,10,1):
    message = input("please enter message: ")
    messages = []
    messages.append(message)
    messages.insert(1, "h")
    print(messages)























"""
base = "You are the master of the game you will give a choice each day on events of that day."
OPEN_AI_KEY="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"
client= OpenAI(api_key=OPEN_AI_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
    {"role": "user", "content": base},
    ]
    )

print(completion.choices[0].message);



def print_numbers():


def print_letters():


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()



{"role": "user", "content":  }
"""