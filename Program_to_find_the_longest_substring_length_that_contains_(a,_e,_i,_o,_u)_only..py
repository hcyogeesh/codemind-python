def longest_vowel_substring(s):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    max_length = 0
    curr_length = 0
    for c in s:
        if c in vowels:
            curr_length += 1
            max_length = max(max_length, curr_length)
        else:
            curr_length = 0
    return max_length

s = input()
print(longest_vowel_substring(s))
