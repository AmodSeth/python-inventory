# if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.

# "CHAT WITH HER!" or # " "IGNORE HIM!""


def solve():
    message = input()
    f_map = dict()

    for ch in message:
        f_map[ch] = f_map.get(ch,  0) + 1

    totat = len(f_map)
    print("IGNORE HIM!") if totat % 2 else print("CHAT WITH HER!")



solve()