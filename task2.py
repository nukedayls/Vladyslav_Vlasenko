def first_non_repeating_letter(string):
    non_repeating_letter = [letter for letter in string if string.lower().count(letter.lower()) == 1]
    return  non_repeating_letter[0] if len(non_repeating_letter) > 0 else ""

print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('sTress'))
print(first_non_repeating_letter('ababab'))