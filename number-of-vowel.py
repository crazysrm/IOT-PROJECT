def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


def vowel_consonant_ratio(s):
    v = count_vowels(s)
    c = count_consonants(s)

    if c == 0:
        return "Consonants count is zero, ratio not defined"
    else:
        return v / c


string = input("Enter a string: ")

vowels = count_vowels(string)
consonants = count_consonants(string)
ratio = vowel_consonant_ratio(string)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Ratio (vowels : consonants):", ratio)
