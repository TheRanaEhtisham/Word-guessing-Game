import random

name = input("What is your name? ")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)



def play_game():
    
    total_guesses = 5
    guesses_made = 0
    print(f"Welcome {name} to the Word Guessing Game!")

    while guesses_made < total_guesses:
        
        guess = input("Guess a word: ").lower()

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            break
        else:
            guesses_made += 1
            print(f"Sorry, '{guess}' is not in the word. You have {total_guesses - guesses_made} guesses left.")
        
    
        
    else:
        print(f"Sorry {name}, you've used all your guesses. The word was '{word}'. Better luck next time!")
        
        


if __name__ == "__main__":
    print("Welcome to the Word Guessing Game!")
    play_game()