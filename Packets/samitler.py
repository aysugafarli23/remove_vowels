def samitleri_al(string):
    vowels = ['a','e','i','o','u']
    result = {letter for letter in string if letter.lower() not in vowels }
    # result = ''.join(result)
    return result

# # or
# string = "Hello world and how are u guys"
# rem_vowel(string)