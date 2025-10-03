

def dictionary():
    friends = ['Rolf', 'amod', 'seth', 'august']
    time = [1,3,2,4]

    long_timers = {
        friends[i]:time[i]
        for i in range(len(friends))
    }
    print(long_timers)


def zip_function():
    friends = ['Rolf', 'amod', 'seth', 'august']
    time = [1,3,2,4]
    #used for zipping 2 list togther
    zipped_output = zip(friends,time)
    print(list(zipped_output))
    

def enumerate_function():
    friends = ['Rolf', 'amod', 'seth', 'august']
    # for counter,friends in enumerate(friends):
    #     print(counter,friends)
    
    print(list(enumerate(friends)))




def udemy_excercise():
    players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]
    for player in players:
        player_name = player["name"]
        numbers = player["numbers"]

        for i in numbers:
            print(i)



if __name__ == "__main__":
    udemy_excercise()