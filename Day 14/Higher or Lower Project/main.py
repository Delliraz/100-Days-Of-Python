from timeit import default_number

from art import logo,vs
from game_data import data
from random import choice

print(logo)
score = 0
already_asked = []



def get_random_personality():
    rand = choice([i for i in range(0,len(data)-1) if i not in already_asked])
    already_asked.append(rand)
    return data[rand]

def is_personA_bigger(personA,personB):
    return personA["follower_count"] > personB["follower_count"]

def print_compare(tag, person):
    print(f"Compare {tag}: {person["name"]}, {person["description"]}, from {person["country"]}.")
personA = get_random_personality()

while True:
    personB = get_random_personality()
    print_compare("A",personA)
    print(vs)
    print_compare("B", personB)
    guess = input("Who has more followers? Type A or B: ")
    is_guess_right = False
    if guess == "A":
        is_guess_right = is_personA_bigger(personA,personB)
    else:
        is_guess_right = is_personA_bigger(personB,personA)
    if not is_guess_right:
        print(f"Sorry, thats wrong! Your final score {score}")
        break
    score += 1
    personA = personB
