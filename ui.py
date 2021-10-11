from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
import time
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, text="Title",
                                                   fill=THEME_COLOR,
                                                   font=("Ariel", 20, "italic"),
                                                   width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # buttons
        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.answer_true)
        self.right_button.grid(column=0, row=2, pady=20)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.answer_false)
        self.wrong_button.grid(column=1, row=2, pady=20)

        # labels
        self.score_lable = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 10))
        self.score_lable.grid(column=1, row=0, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.question_number > 9:
            messagebox.showinfo(title="Finish Quiz", message=f"You've completed the quiz\n"
                                                             f"Your final score"
                                                             f" was: {self.quiz.score}/{self.quiz.question_number}")
            exit(0)
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=q_text)

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.score_lable.config(text=f"Score: {self.quiz.score}")

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.score_lable.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

