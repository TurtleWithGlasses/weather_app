import customtkinter as ctk

class SmallWidget(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color="red")
        self.pack(expand=True,fill="both")

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