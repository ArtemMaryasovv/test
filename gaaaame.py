from random import *
s=('tea', 'eternity', 'fate', 'exodus', 'life')
word=choice(s)
right=word
mix=""
while word:
        p=randrange(len(word))
        mix+=word[p]
        word=word[:p]+word[p+1:]

print('Welcome to Anagramm game, you need to rearrange the letters to get the original word')
print("Let's start:", mix)
v=input("Your word is:")
while v!=right and v!="":
        print("Your word is incorrect :(")
        break
if v==right:
        print("You are absolutely right!")
