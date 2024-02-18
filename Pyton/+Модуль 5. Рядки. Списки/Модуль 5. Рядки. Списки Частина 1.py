#Завдання 1

text=input("\tEnter your text: ")
text=text.lower()
text=text.replace(" ","")
if text==text[::-1]:
  print("\tYour text is a palindrome.")
else:
  print("\tYour text is not a palindrome.")

#Завдання 2

text=input("\tEnter your text: " )
list=input("\tEnter your words with a space: ").split()
for i in list:
  text=text.replace(i,i.upper())
print(f"\tYour changed text: {text}")

#Завдання 3

text=input("\tEnter your text: ")
text=text.replace("!",".")
text=text.replace("?",".")
text=text.replace("...",".")
print (f"\tThe number of sentences in your text is {text.count('.')}.")