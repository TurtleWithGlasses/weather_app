import customtkinter as ctk
from settings import *
# from ctypes import windll, byref, sizeof, c_int


class App(ctk.CTk):
    def __init__(self):

        self.color = WEATHER_DATA["Clear"]
        super().__init__(fg_color=self.color["main"])
        self.geometry("550x250")
        self.minsize(550,250)
        self.title("Weather")
        self._set_appearance_mode("dark")

        self.mainloop()


if __name__ == "__main__":
    App()