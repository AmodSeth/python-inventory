from Questions.question_display import print_question
from random import randrange
from Questions.question_display import question_engine

    

"""
def while_loops_practise():

    user_input = input("Do you wish to run the program? (yes/no): ")

    while user_input == "yes":
        print("We're running")
        user_input = input("Do you still wish to run the program? (yes/no): ")

    print("we stopped running the loop")


"""
def stop_game(total_score):
    print("The Game has stopped ,Total score", total_score)
  
def update_score(user_answer, actual_anwer, current_score):
    if actual_anwer.lower() == user_answer.lower():
        return current_score + 1, True
    else:
        return current_score, False

def game_engine():
    total_score = 0
    game_running = True

    while game_running:
        user_input = input("Do you wish to keep the quiz running: (Yes/No) Or Enter:  ")
        if user_input == "No":
            stop_game(total_score)
            game_running = False
        else:
            print("We're running")
            # get the question and input
            data = question_engine(randrange(10))
            current_question_id = data["id"]
            current_question = data["question"]
            actual_anwer = data["answer"]
            print(current_question)
            for idx, option in enumerate(data["options"], start=1):
                 print(f"{idx}. {option}")
            user_answer = input("Please provide your answer by typing the whole answer:  ")
            curent_score, Flag = update_score(user_answer,actual_anwer, total_score)
         
            if Flag:
                total_score = curent_score
                print("Yippeeee you answer was correct --->  " , total_score)
            else :
                print("You fucked up !!!!! " , total_score)
            
            

        

        
        
        



        
    


    print("The quiz stopped running")
    





if __name__ == "__main__":
    game_engine()



