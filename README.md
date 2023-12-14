Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

milestone_2.py
The file mileston_2.py is a python file that holds a list of my favourite fruit in the variable 'word_list'. a random word is taken fromm the word_list using the method random.choice and stored in the variable 'word'. The user is alsked to put in a single character which is stored in the variable 'guess'

An if statement is used to check the length is 1 and whether the charcter entered is an alpha.If it is then "good guess!" statement is printed out.

If this is not the case the following else statment is triggered and "Oops! That is not a valid input." is printed.

mileston_3.py
The file milestone_3.py is a upgraded version of mileston_2.py. Here 2 functions have been produced. check_guess takes in the gussed letter as an argument and checks if the letter is in the word that the computer had randomly chose from the word_list containing a list of 5 fruits. the function ask_for_input is the main driver of the programme. IT has a while loop set to true. It then asks for input from the user. then there is an if statement that checks that the input is valis i.e. the length is 1 and it is an alphabet character. If it passes this test the while loop is broken. if it fails then a print statement asks for the user to try again.

##milestone_4.py

this file is a possible example of oop programming. A class Hangman is created and contains methods for playing a round of hangman. In this class the following variables are intialised. the following variables are definded the word_list and number _of Lives(which is set to 5) are passed as arguemnts and are set as self. i.e. self.word_list and self_num_of_lives. the word is chosen using the random.choice function and called self.word. the list word_guessed is initalised using '' to represent each letter. The list is as long as the word. the num_letters is the number of UNIQUE letters in the word using (list(len(set.self.word)). an empty list called list_of _guesses.

the check_guess function is expanded from mileston_3.py. a for loop is added in the if statement after the print statement. the for loop looks at each letter(variable each_letter) and the posistion(variable count) it holds in the word. it then compares it to the guess and if it is the same then places the letter in the list word_guessed at the index count. Outside the if statement containing the for loop but within the outside if statement the num_letters is reduced by 1. The else statement is also changed. num_lives is reduced by 1 an additional print statement is added print(f"You have {self.num_lives} lives left.")

##The structure at this point.

class named Hangman inside this class are 3 methods, 1.the magic method called --init--
ask_for_input which is a while loop for an input statement for a user to choose letters It calls the 3rd function check_guess if the letter is a single letter and a member of the alphabet.if not then it issues print statements to ask for a single letter to be input. It also checks to see if the letter has been tried before. If so a print statement saying so is issued.
Check_guess checks if the letter is in the word. if it is it looks to see where the letter is in the word and places it in the right place in the word_guessed list and reduces the number of letters to be found by 1. if the letter is not in the word the number of lives is reduced by 1. 2 print statements inform the letter is not in the word and that they have so many lives left. the letter is placed in the list of guesses.
##milestone_5.py

changes to milestone_4.py

A new function is created called play_game . It takes word_list as an argument. Ouside of this function an instance of Hangman is created called game. Inside play_game a while loop is set to True. inside the while loop an if statement checks if the num_of_lives is 0. If it is then the player is informed that they have lost. The loop is broken here. If the num_of_lives is greater than 0 and the num_letters is 0 then the user is informed that they have won. The loop si broken here. IF the num_of_lives is greater than 0 then the ask_input method in game is triggered and the user is asked to input a letter etc. The only change to the methods described in milestone_4.py is that thewhile loop in ask_for_input is no longer required as it is now in play_game.

##What I have learnt.

i have a fundementally better idea about how python handles OOP. I had trouble when init;aizing varibles but that was a misunderstnading on my part as i didn't realise that the init method was actually the same as anyother method in that you could do things hewre the same asin other methods and it was not confinded just to initalising variables. I also had trouble when i was trying to run the programme as an OOp programme as I had difficultly calling the ask_for input function but that was solved by indenting the methods by a single space (took a while to sort that one out). My last problem was getting the local varibles in the instance game to be read from outside the class. Still don't know why that started to work. Anyway It's all working now, I hope.
