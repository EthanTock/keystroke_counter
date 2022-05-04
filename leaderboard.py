from tkinter import *

BG_COLOR = "grey3"
TEXT_COLOR = "white"
KEYBOARD_FONT = ("Terminal", 8, "normal")


class Leaderboard:

    def __init__(self, key_layout: list):
        self.leaderboard_frame = Frame(
            padx=5,
            pady=5,
            bg=BG_COLOR
        )

        self.all_keys = {}
        for row in key_layout:
            self.all_keys.update(row)
        self.sorted_keys = dict(sorted(self.all_keys.items(), key=lambda item: item[1]["percent"], reverse=True))
        self.leaderboard_text = []
        pos = 0
        for name, data in self.sorted_keys.items():
            if (name != "SHIFT_2" and name != "CTRL_2") and data["percent"] != 0:
                pos += 1
                self.leaderboard_text.append(f"{pos}. '{data['normal']}', {data['count']} instances, " \
                                         f"{data['percent'] * 100:.2f}% relative to '{list(self.sorted_keys.keys())[0]}'\n")
        for ypos in range(len(self.leaderboard_text)):
            leaderboard_label = Label(text=self.leaderboard_text[ypos], fg=TEXT_COLOR, font=KEYBOARD_FONT, bg=BG_COLOR)
            leaderboard_label.grid(in_=self.leaderboard_frame, sticky="W", row=ypos, column=0)
