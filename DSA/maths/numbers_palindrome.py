def cheating_way() -> str:
    n = int(input(""))

    #convert into string
    n_string = str(n)
    rev_string = ("".join(reversed(n_string)))
    
    print("YES") if n_string == rev_string else print("NO")




if __name__ == "__main__":
    cheating_way()