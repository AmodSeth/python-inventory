def solve():
    n  = int(input(""))
    for i in range(n):
        word = input("")
        word_len = len(word)
        if len(word) > 10:
            new_word = word[0] + str(word_len-2) + word[word_len-1]
            print(new_word)
        else:
            print(word)
    



solve()