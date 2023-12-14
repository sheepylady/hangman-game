import random

def check_guess(letter):
    #takes in a letter that has been guessed by the user and checks to see if it is in the work that was randomly 
    # picked by the computer from the list of fruits
   
   # puts the letter in lower case
    letter.lower() 

    if letter in word:
        print(f"Good guess! {letter} is in the word.")       
    else:
        print(f"Sorry, {letter} is not in the word. Try again.") 
    

def ask_for_input():
  
  # asks the user for input. The while statements keeps on asking for input until the correct input is entered
  #checks if the letter is = to 1 char in lenght and is a letter i.e. part of the alphabet.
  # if it is then the whil estatement is broken. otherwise a statement si printed.
  
  check_guess(guess) # function to see if letter is part of the chosen word
  while True:
    guess = input ("Please choose a single letter ")
    if len(guess) == 1 and guess.isalpha():
         
         break
    else: print( "Invalid letter. Please, enter a single alphabetical character.")    



word_list = ['cherry', 'lychee', 'apricot', 'apple','kiwi']

word = random.choice(word_list)# random word is chodsen from the list
print(word)


ask_for_input()



