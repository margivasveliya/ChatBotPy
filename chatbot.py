
from datetime import datetime, date

print("I’m ChatBot. Let's have a chat. (type 'bye' when you're leave)")

while True:
    msg = input("You: ").strip().lower()

    if msg in ["bye", "exit", "quit"]:
        print("ChatBot: Okay, see you.")
        break

    elif msg in ["hi", "hello", "hey"]:
        print("ChatBot: Hey there! How can i help you?")

    elif "how are you" in msg:
        print("ChatBot: I’m good, Just chilling here waiting for chats.")

    elif "your name" in msg:
        print("ChatBot: Folks call me ChatBot.")

    elif "time" in msg:
        now = datetime.now()
        print(f"ChatBot: It’s {now.strftime('%I:%M %p')} right now.")

    elif "date" in msg:
        today = date.today()
        print(f"ChatBot: Today’s {today.strftime('%B %d, %Y')}.")

    elif "weather" in msg:
        print("ChatBot: I can’t check the weather, but I hope it’s nice outside there.")

    else:
        print("ChatBot: Umm... not sure what you mean. Try asking something else?")
