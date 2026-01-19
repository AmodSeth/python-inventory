# add emojoji after each word

emoji_dict = {
    "love" : "❤️",
    "happy" : "😂",
    "party" : "🍻",
    "sad" : "😭"
}


sentence = input("Enter the sentence in :")

# word_ = ""
# keywords = []
# for i in sentence:
#     if i != " ":
#         word_ = word_ + i 
#     else:
#         keywords.append(word_)
#         word_ = ""

# final_sentence = ""
# for i in keywords:
#     final_sentence = final_sentence + i +  emoji_dict.get(i, " ")

# print(final_sentence)




# updated code 
keywords = []
for word in sentence.split():
    cleaned = word.lower().strip(".,/?")
    emoji = emoji_dict.get(cleaned,"")
    if emoji : 
        keywords.append(f"{word} {emoji} ") 
    else: 
        keywords.append(f"{word}")


final = " ".join(keywords)

print(final)
    


        

        

    
    



   
    