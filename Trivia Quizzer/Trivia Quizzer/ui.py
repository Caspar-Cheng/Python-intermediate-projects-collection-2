from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivia Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill="orange",
            font=("Arial", 15, "italic")
        )
        self.score = Label(text="Score:0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score.grid(row=0, column=1)

        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        self.t_button = Button(image=right_img, highlightthickness=0, border=0, command=self.right)
        self.t_button.grid(row=2, column=1)
        self.f_button = Button(image=wrong_img, highlightthickness=0, border=0, command=self.wrong)
        self.f_button.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="Lightgreen")
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've finished the quiz and the final score "
                                        f"is {self.quiz.score}/{len(self.quiz.question_list)}")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
