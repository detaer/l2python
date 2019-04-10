import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again.'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Foncentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

print("Ask a question of the mighty 8ball")
input("Type your question here:")
print("How hard do you want to shake the 8 ball?")
intensity=""
intensity=input("Hard, Soft, Weak")

if intensity == "Hard":
    print("Ohh gutsy")
elif intensity == "Soft":
    print("Bold move cotton, lets see how this plays out")
else:
    print("Really? Thats gonna help get the answer you are looking for?")

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)