def generate_vowelconsonant_sequence(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    result = ""
    prev_char = ""
    for char in string:
        if char in vowels:
            if prev_char != "V":
                result += "V"
                prev_char = "V"
        else:
            if prev_char != "C":
                result += "C"
                prev_char = "C"
    return result.upper()

string = input()
print(generate_vowelconsonant_sequence(string))