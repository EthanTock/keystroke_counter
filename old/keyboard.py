from tkinter import *
import keyboard_layouts
import math


class Keyboard:

    def __init__(self, layout_type: str):  # , keys: list[Key]):
        """
        :param layout_type: Specify a keyboard type. Use: "us"
        """
        self.key_layout = keyboard_layouts.US_KEYBOARD_LAYOUT
        if layout_type == "us":
            self.key_layout = keyboard_layouts.US_KEYBOARD_LAYOUT
        self.SIZE_MULTIPLIER = 4
        self.keyboard_frame = Frame(
            height=5*self.SIZE_MULTIPLIER,
            width=15*self.SIZE_MULTIPLIER,
            pady=5,
            padx=5
        )
        self.assemble_keyboard()

    def assemble_keyboard(self):
        row_num = 0
        for row in self.key_layout:
            column_num = 0
            row_frame = Frame()
            for key in row.items():
                key_name = key[0]
                key_data = key[1]
                key_button = Button(
                    text="",
                    width=math.floor(key_data["length"] * self.SIZE_MULTIPLIER),
                    height=math.floor(self.SIZE_MULTIPLIER / 2),
                    highlightthickness=1
                )
                if not key_name.isupper() and key_name.isalpha():
                    key_button.config(text=f"{key_data['shift']}")
                elif not key_name.isupper():
                    key_button.config(text=f"{key_data['normal']}{key_data['shift']}")
                else:
                    key_button.config(text=f"{key_data['normal']}")
                key_button.grid(in_=row_frame, row=row_num, column=column_num)
                column_num += 1
            row_frame.grid(in_=self.keyboard_frame)
            row_num += 1


