THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
import os

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)
        self.window.maxsize(height=500, width=350)
        #score
        self.label = Label(text=f"Score: {self.quiz.score}",
                           bg=THEME_COLOR,
                           fg="white",
                           font=("Arial", 10, "bold")
                           )
        #canvas
        self.canvas = Canvas(height=250, width=300,  highlightthickness=0)
        self.question_text = self.canvas.create_text(
                                            150,
                                            125,
                                            width=280,
                                            text="filler",
                                            fill=THEME_COLOR,
                                            font=("Arial", 20, "italic"),
                                            )
        #photos
        self.right_button_photo = PhotoImage(file="images/true.png")
        self.wrong_button_photo = PhotoImage(file="images/false.png")
        #buttons
        self.true_button = Button(width=100,
                                  height=97,
                                  image=self.right_button_photo,
                                  highlightthickness=0,
                                  bd=0,
                                  command=self.right_pressed
                                  )
        self.wrong_button = Button(width=100,
                                   height=97,
                                   image=self.wrong_button_photo,
                                   highlightthickness=0,
                                   bd=0,
                                   command=self.wrong_pressed
                                   )
        #layout
        self.label.grid(row=0, column=1, padx=20, pady=20, sticky="e")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.true_button.grid(row=2, column=0, pady=(0, 20))
        self.wrong_button.grid(row=2, column=1, pady=(0, 20))
        #load question
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=text)

    def right_pressed(self):
        if self.quiz.still_has_questions():
            is_right = self.quiz.check_answer("True")
            self.ux_canvas_response(is_right)
        else:
            is_ok = messagebox.askokcancel(title="Quizler", message="Play again?")
            if is_ok:
                print("NEED TO UPDATE TO ALLOW THIS BUTTON TO RESTART THE PROGRAM")

    def wrong_pressed(self):
        if self.quiz.still_has_questions():
            is_right = self.quiz.check_answer("False")
            self.ux_canvas_response(is_right)
        else:
            is_ok = messagebox.askokcancel(title="Quizler", message="Exit?")
            if is_ok:
                quit()

    def update_score_question(self):
        self.canvas.configure(bg="white")
        self.label.configure(text="Score: {}".format(self.quiz.score))
        if self.quiz.still_has_questions():
            self.next_question()
        else:
            self.game_over()

    def ux_canvas_response(self, bool: bool):
        if bool:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.update_score_question)

    def game_over(self):
        self.canvas.itemconfig(self.question_text, text=f"Game over\nScore: {self.quiz.score}/10")
