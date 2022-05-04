from tkinter import *
from keyboard import Keyboard


class Window:

    def __init__(self, keyboard_layout_type: str):
        """
        :param keyboard_layout_type: Specify a keyboard type. Use: "us"
        """

        self.window = Tk()
        self.window.config(padx=20, pady=20)
        self.window.title("Keyboard")

        self.keyboard_layout_type = keyboard_layout_type
        self.keyboard = Keyboard(self.keyboard_layout_type)
        self.keyboard.keyboard_frame.grid(row=0, column=0)

        self.window.mainloop()
