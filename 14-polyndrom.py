# word = input("write word:")
# word_reverse = ""
# for i in word:
#     word_reverse = i +word_reverse
# if word == word_reverse:
#     print ("your word is polyndrom")
# else:
#     print("your word is polyndrom")

word = input ("")
length = len(word)
half_len = length//2

if length%2 == 0:
    first_half = word[:half_len]
    second_half = first_half[::-1]
    print(first_half+second_half)
else:
    first_half = word[:half_len]
    midle = word[half_len]
    second_half = first_half[::-1]
    print(first_half+midle+second_half)