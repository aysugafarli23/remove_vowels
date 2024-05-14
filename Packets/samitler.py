def samitleri_al(string):
    vowels = ['a','ə','e','ı','i','o','ö','u','ü']
    result = {letter for letter in string if letter.lower() not in vowels }
    # result = ''.join(result)
    return result
