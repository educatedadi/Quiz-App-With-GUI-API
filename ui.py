from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TITLE_FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        # self.window.minsize(width=300, height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        right_tick = PhotoImage(file="images/true.png")
        wrong_mark = PhotoImage(file="images/false.png")

        self.score_label = Label(text='SCORE : 0')
        self.score_label.grid(row=0, column=1)
        self.score_label.config(bg=THEME_COLOR, fg="white", )

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_txt = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Title',
            font=TITLE_FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_btn = Button(image=right_tick, highlightthickness=0, command=self.true_btn_pressed)
        self.right_btn.grid(row=2, column=0)

        self.wrong_btn = Button(image=wrong_mark, highlightthickness=0, command=self.false_btn_pressed)
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='White')
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.score_label.config(text=f'SCORE : {self.quiz.score}')
            self.canvas.itemconfig(self.question_txt, text=question)
        else:
            self.canvas.itemconfig(self.question_txt, text="You've reached the end of the quiz")
            self.right_btn.config(state='disabled')
            self.wrong_btn.config(state='disabled')

        self.canvas.itemconfig(self.question_txt, fill=THEME_COLOR)

    def give_feedback(self, is_true: bool):
        if is_true:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.canvas.itemconfig(self.question_txt, fill='White')
        self.window.after(1000, self.get_next_question)

    def true_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))
        # self.check_answer('True')

    def false_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))
        # self.check_answer('False')


