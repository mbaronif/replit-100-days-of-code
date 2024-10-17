import os, time
listOfEmail = []

def prettyPrint():
    os.system("clear")
    print("listOfEmail")
    print()
#    counter = 1 - When we use an index, we don't need the counter, as the index will consider the whole list.
    for index in range(len(listOfEmail)):
        print(f"{index}: {listOfEmail[index]}")
#        counter+=1
    time.sleep(2)

def fakeSpamMessage(max):
    for i in range(0,max):
        #3" allows the split-line text in the code
        print(f"""Email {i+1}

Dear {listOfEmail[i]}

It has come to our attention that you're missing out on
the amazing Replit 100 days of code. We insist you do it
right away. If you dont, we will pass on your email
address to every spammer we've ever encountered and also
sign you up to the My Little Pony newsletter, because\nthat's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III
""")
        time.sleep(1)
        os.system("clear")      

while True:
    print("SPAMMER Inc.")
    menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu == "2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        fakeSpamMessage(10)  #10 is the max number of messages I want to send
    time.sleep(1)
    os.system("clear")
