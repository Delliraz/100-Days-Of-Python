import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
try_counter = 0
max_attemps = 6

placeholder = []
for i in range(0,len(chosen_word)):
    placeholder.append("_")

hangman_art.stages.reverse()

def find_all_index(chosen_word, guess):
    index = []
    for i in range (0,len(chosen_word)):
        if chosen_word[i] == guess:
            index.append(i)
    return index


while try_counter < max_attemps or "_" in placeholder:
    print("".join(placeholder))
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            print("Right")
            all_index = find_all_index(chosen_word,guess)
            for i in all_index:
                placeholder[i] = guess
            continue

    try_counter += 1
    print("Wrong")
    print(hangman_art.stages[try_counter])

    if try_counter == max_attemps:
        print("You are finished")
        break
    elif "".join(placeholder) == chosen_word:
        print("You've guessed right")
        break