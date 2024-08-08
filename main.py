import random

word_list = ["chicken","fish","orange"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

total_lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display) 
            
    if guess not in chosen_word:
        total_lives -= 1
        print("you lose a life")
        if total_lives == 0:
            game_over = True
            print("you lose")
            
    if "_" not in display:
        game_over = True
        print("You win.")