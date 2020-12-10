"""
Experimenting with tkinter &
Building a basic calculator
"""

import tkinter as tk
from functools import partial

class Calc():
    def __init__(self):
        # Set up the app
        self.window = tk.Tk()
        self.window.title('Simple Calculator')
        self.window.rowconfigure([0,1,2,3,4,5], weight=1)
        self.window.columnconfigure([0,1,2,3], weight=1)

        # Define Calculator Variables
        self.ans = None
        self.ent = 0
        self.repeat = False
        # Operations:
        # Add = 1
        # Subtract = 2
        # Multiply = 3
        # Divide = 4
        self.operations = 0

        # Create the app's widgets
        common_args = {'padx': 20,
                       'pady': 20,
                       'bg': 'black',
                       'activebackground': 'gray',
                       'fg': 'white',
                       'font': 'Georgia 16'}
        self.entry = tk.Entry(bg=common_args['bg'],fg=common_args['fg'],font=common_args['font'],justify='right')
        num_btns = []
        for i in range(10):
            btn = tk.Button(text=str(i), **common_args, command=partial(self.show, str(i)))
            num_btns.append(btn)
        dot = tk.Button(text='.', **common_args, command=partial(self.show,'.'))
        plus = tk.Button(text='+', **common_args, command=self.add)
        minus = tk.Button(text='-', **common_args, command=self.subtract)
        times = tk.Button(text='x', **common_args, command=self.multiply)
        divide = tk.Button(text='/', **common_args, command=self.divide)
        equals = tk.Button(text='=', **common_args, command=self.enter)
        clear = tk.Button(text='Clear', **common_args, command=self.clear)

        # Display all the widgets
        self.entry.grid(row=0, columnspan=4, sticky='nesw', ipady=15)
        self.entry.insert(0,'0')

        num_btns[0].grid(row=4, column=1, columnspan=2, sticky='news')

        num_btns[1].grid(row=3,column=0,sticky='news')
        num_btns[2].grid(row=3, column=1,sticky='news')
        num_btns[3].grid(row=3, column=2,sticky='news')

        num_btns[4].grid(row=2,column=0,sticky='news')
        num_btns[5].grid(row=2, column=1,sticky='news')
        num_btns[6].grid(row=2, column=2,sticky='news')

        num_btns[7].grid(row=1,column=0,sticky='news')
        num_btns[8].grid(row=1, column=1,sticky='news')
        num_btns[9].grid(row=1, column=2,sticky='news')

        dot.grid(row=4,column=0, sticky='news')
        plus.grid(row=1, column=3,sticky='news')
        minus.grid(row=2, column=3,sticky='news')
        times.grid(row=3, column=3,sticky='news')
        divide.grid(row=4, column=3,sticky='news')
        equals.grid(row=5, column=0, columnspan=2, sticky='news')
        clear.grid(row=5, column=2, columnspan=2, sticky='news')

        self.window.bind("<Key>", self.key)
        self.window.bind("<Return>", self.enter)

        self.window.mainloop()

    def key(self, event):
        press = event.char
        if press == '+':
            self.add()
        elif press == '-':
            self.subtract()
        elif press == '*':
            self.multiply()
        elif press == '/':
            self.divide()
        else:
            try:
                int(press)
                self.show(press)
            except ValueError:
                pass

    def show(self, num):
        # if last button pressed was enter
        # assume this is a new calculation
        # and reset everything
        if self.repeat:
            self.entry.delete(0,'end')
            self.repeat = False
            self.operations = 0
        # Add the number pressed to the end of the input box
        self.entry.insert('end', num)

    def clear(self):
        # Deletes whatever is currently in the input box
        # sets all calculator variables back to original values
        self.entry.delete(0,'end')
        self.entry.insert(0, '0')
        self.operations = 0
        self.ans = None
        self.ent = 0
        self.repeat = False

    def get_current_ans(self):
        # repeat means user pressed enter again without changing anything
        # so self.ent should remain the same
        # otherwise user did press another operation
        # so get current input number
        if self.repeat == False:
            self.ent = round(float(self.entry.get()),4)
        self.entry.delete(0, 'end')

        # calculate new answer according to which operation is active
        if not self.ans or self.operations == 0:
            self.ans = self.ent
        elif self.operations == 1:
            self.ans += self.ent
        elif self.operations == 2:
            self.ans -= self.ent
        elif self.operations == 3:
            self.ans *= self.ent
        elif self.operations == 4:
            self.ans /= self.ent

        # if current ans is a whole number
        # then get rid of decimal
        # otherwise round it
        if int(self.ans) == self.ans:
            self.ans = int(self.ans)
        else:
            self.ans = round(self.ans,4)

    def check(self):
        # if repeat is active then clear current answer
        if self.repeat:
            self.ans = None
        # check function is only used when an operation button is pressed
        self.repeat = False
        # current input will be set as new current ans
        self.get_current_ans()

    def add(self):
        self.check()
        self.operations = 1

    def subtract(self):
        self.check()
        self.operations = 2

    def multiply(self):
        self.check()
        self.operations = 3

    def divide(self):
        self.check()
        self.operations = 4

    def enter(self, event=None):
        self.get_current_ans()
        self.entry.insert(0,str(self.ans))
        self.repeat = True

def show_calc():
    calc = Calc()

if __name__ == '__main__':
    show_calc()