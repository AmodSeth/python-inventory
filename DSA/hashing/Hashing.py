


# pre stoing values 

## question1

n = [5,3,2,2,1,5,5,7,5,10] # n can only have from number 1 to 10 with len 10^8
m = [10,111,1,9,5,67,2] # m can have any number with len 10^8

#new to find frequency of each number in m from n

## using brute force
## T>C O(n*m)
def brute_force():
    for nums in m:
        count = 0
        for x in n:
            if x == nums:
                count += 1

## using frequency array

def frequency_array():
    freq = [0]*11

    for x in n:
        freq[x] += 1

    for nums in m:
        if nums >= 1 and nums <= 10:
            print(freq[nums])
        else:
            print(0)


def frequency_map():
    f_dict = dict()

    for x in n:
        f_dict[x] = f_dict.get(x,0) + 1

    for x in m:
        print(f_dict.get(x,0))


def character_mapping():

    s = "abcabcaayyzzaaccaabbqertashggfgd"
    hash_list = [0]*27

    for ch in s:
        ass_value = ord(ch) -97
        
        hash_list[ass_value]+=1

    print(hash_list,end="")

character_mapping()