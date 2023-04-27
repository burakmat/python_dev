class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score=0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def next_question(self):
        user_input=input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text}")

        self.check_answer(user_input,self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self,user_input,answer):
   #     global final_score
        if user_input.lower()==answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f"The correct answer was {answer}\nYour current score is: {self.score}/{self.question_number+1}\n")
