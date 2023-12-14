import random

class Hangman():
 '''This class implements the game Hangman. 
 
     It has 3 methods. The first is a magic method to initalise incoming arguements
     of word_list and the num_of_lives which is set to 5. Additional variables 
     that are intialised here are  
     word - the random choice from the word_list
     word_guessed - the list filled with spaces for characters. It is the length of the word.
     num_letters - which is number of unique letters in the chosen word
     finally list_of guesses - initalised as an empty list but it is used to hold all the quesses 
     of the user so that they can be told if they have tried that letter before
     The 2nd method the  ask_for input which has a while loop set to true. in it 
     is an input statement which asks the user to input a single letter. 
     there is an if statement to check that the input is a single letter. if not 
     a print asttement is executed telling the user to try again. this is followed by elif 
     which tells the user that they have tried this letter before (because the letter is in the 
     list_of_guesses list.) Finally if the letter is single and a character and not in the list of guesses then
     it calls the final function check_guess.
     check_guess takes the letter and sees if it is in the word. if it is then it looks to see where it is
     in the word and places the letter in the appropriate place in the word_guessed list, replacing one of the empty slots
     It also reduces the number of letters to be found by. IF the letter is not in the word the number of lives is 
     reduced by 1, 2 print statements are issued to say that the letter was not in the word and they have so many lives left.
     The guess is placed in the list of guesses

     the function play_game sits out side the class structure and triggers the playing of the game hangman.
     Outside this function an instance of hangman is created called game.
     the function play_game looks at the num_of_lives. If it reaches 0 then the game is over and 
     the user is told this. If this happens the while loop is broken and the game stops.
     if the number_of_lives is greater than 0 and the num_of_letters is 0 then the user is told that they have won the game. 
     The loop is broken at this point. While the number_of_lives is more than 0 the
     ask_for_input method in game is triggered (see above). 
           '''
 
  
    
 def __init__(self,word_list,num_lives = 5):
    self.word_list = word_list #list of words to choose from
    self.num_lives = num_lives #number of tries
    self.word = random.choice(self.word_list) #random word chosen from word_list
    self.word_guessed = [''] * len(self.word)  #list of empty spaces =to length of the word
    self.num_letters = len(list(set(self.word))) # number of unique chrs in word
    self.list_of_guesses = [] #list of guesses
      
    print(f"The mystery word has {self.num_letters} characters")


 


         
 def ask_for_input(self):
  guess = input ("Please choose a single letter ")
   
  if not (len(guess) == 1 and guess.isalpha()):
         print( "Invalid letter. Please, enter a single alphabetical character.")
  elif guess in self.list_of_guesses: 
        print( "You already tried that letter!") 
  else:
       print(guess) 
       self.check_guess(guess) # function to see if letter is part of the chosen word
     

 def check_guess(self,guess):
  guess.lower() 
  if guess in self.word:
        print(f"Good guess! {guess} is in the word.")    
        for count, each_letter in enumerate(self.word):
            if  guess == each_letter:
                self.word_guessed[count]= guess

        self.num_letters = self.num_letters -1 
                 
  else:
        self.num_lives = self.num_lives -1
        print(f"Sorry, {guess} is not in the word. Try again.")
        print(f"You have {self.num_lives} lives left.")
        
  self.list_of_guesses.append(guess) 
  print(self.list_of_guesses)   




#word list

word_list = ['cherry', 'lychee', 'apricot', 'apple','kiwi']



#set the game off

def play_game(word_list):
   num_lives = 5
   game = Hangman(word_list)
   
 
#set the game off
   while True:
     
    if game.num_lives == 0:
        print("you lost!")    
        break
    elif num_lives > 0 and game.num_letters == 0 :
           print("You have won the game. Yaaay")
           break 
    elif num_lives > 0:
        print(num_lives)
        print(game.num_letters)
        game.ask_for_input()
      
            

#call the function to start the game

play_game(word_list)

