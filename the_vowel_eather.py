user_word = input("Enter a word: ").upper()
vowels = ['A', 'E', 'I', 'O', 'U']
for letter in user_word:
    if letter in vowels:
        continue
    print(letter)
