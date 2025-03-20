def eliminate_vowels(text):
    consonants_only = []
    for letter in text:
        if letter.lower() not in "aeiou":
            consonants_only.append(letter)
    return "".join(consonants_only)

sample_text = "Hello, World!"
print("Text after vowel removal:", eliminate_vowels(sample_text))
