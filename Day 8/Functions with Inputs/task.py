def calculate_love_score(name_1, name_2):
    name_1 = name_1.lower()
    name_2 = name_2.lower()
    true = list("TRUE".lower())
    love = list("LOVE".lower())

    for letter_true in list(true):
        ind = find_indicies(list(name_1), letter_true)
        print(f"{letter_true} occurs in name1 {len(ind)} times")


def find_indicies(arr, letter):
    indicies = []
    i = 0
    for a in arr:
        if a == letter:
            indicies.append(i)
        i += 1
