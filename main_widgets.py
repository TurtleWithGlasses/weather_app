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
    def __init__(self,parent,current_data,forecast_data,location,color,forecast_images):
        super().__init__(parent,fg_color="transparent")
        self.pack(expand=True,fill="both")

        # layout
        self.rowconfigure(0, weight=6, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")
        self.columnconfigure(0,weight=1, uniform="a")
        self.columnconfigure(1,weight=2, uniform="a")

        # widgets
        SimplePanel(self,current_data,0,0,color)
        DatePanel(self,location,0,1,color)
        HorizontalForecastPanel(self,forecast_data,1,0,2,color['divider color'],forecast_images)

class TallWidget(ctk.CTkFrame):
    def __init__(self,parent,current_data,forecast_data,location,color,forecast_images):
        super().__init__(parent,fg_color="transparent")
        self.pack(expand=True,fill="both")

        # layout
        self.columnconfigure(0,weight=1,uniform="a")
        self.rowconfigure(0,weight=3,uniform="a")
        self.rowconfigure(1,weight=1,uniform="a")

        # widgets
        SimpleTallPanel(self,current_data,location,0,0,color)
        HorizontalForecastPanel(self,forecast_data,0,1,1,color['divider color'],forecast_images)

class MaxWidget(ctk.CTkFrame):
    def __init__(self,parent,current_data,forecast_data,location,color,forecast_images):
        super().__init__(parent,fg_color="transparent")
        self.pack(expand=True,fill="both")    

        # layout
        self.columnconfigure((0,1),weight=1,uniform="a")
        self.rowconfigure(0,weight=3,uniform="a")
        
        # widgets
        SimpleTallPanel(self,current_data,location,0,0,color)
        VerticalForecastPanel(self,forecast_data,1,0,color['divider color'],forecast_images)