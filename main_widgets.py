import customtkinter as ctk
from components import *

class SmallWidget(ctk.CTkFrame):
    def __init__(self,parent, current_data, location, color):
        super().__init__(parent,fg_color="transparent")
        self.pack(expand=True,fill="both")

        # layout
        self.rowconfigure(0,weight=6, uniform="a")
        self.rowconfigure(1,weight=1, uniform="a")
        self.columnconfigure(0,weight=1, uniform="a")

        # widgets
        SimplePanel(self,current_data,0,0,color)
        DatePanel(self,location,0,1,color)

class WideWidget(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color="blue")
        self.pack(expand=True,fill="both")

class TallWidget(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color="green")
        self.pack(expand=True,fill="both")

class MaxWidget(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color="orange")
        self.pack(expand=True,fill="both")