import customtkinter as ctk
from settings import *
from main_widgets import *

import urllib.request
import json
from weather_data import *

class App(ctk.CTk):
    def __init__(self,current_data,forecast_data,city,country):

        # data
        self.current_data = current_data
        self.forecast_data = forecast_data
        self.location = {"city":city,"country":country}
        self.color = WEATHER_DATA[current_data["weather"]]

        super().__init__(fg_color=self.color["main"])
        self.geometry("550x250")
        self.minsize(550,250)
        self.title("Weather")
        self._set_appearance_mode("dark")

        # start widget
        self.widget = SmallWidget(self,self.current_data,self.location,self.color)

        # states
        self.height_break = 600
        self.width_break = 1000
        self.full_height_bool = ctk.BooleanVar(value=False)
        self.full_width_bool = ctk.BooleanVar(value=False)
        self.bind("<Configure>",self.check_size)
        self.full_width_bool.trace("w",self.change_size)
        self.full_height_bool.trace("w",self.change_size)



        self.mainloop()

    # check window size
    def check_size(self,event):
        if event.widget == self:
            # width
            if self.full_width_bool.get():
                if event.width < self.width_break:
                    self.full_width_bool.set(False)
            else:
                if event.width > self.width_break:
                    self.full_width_bool.set(True)
            # height
            if self.full_height_bool.get():
                if event.height < self.height_break:
                    self.full_height_bool.set(False)
            else:
                if event.height > self.height_break:
                    self.full_height_bool.set(True)

    def change_size(self,*args):
        self.widget.pack_forget()
        # max widget
        if self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = MaxWidget(self,
                                     current_data = self.current_data,
                                     forecast_data = self.forecast_data,
                                     location = self.location,
                                     color = self.color)
        
        # tall widget
        if self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = TallWidget(self,
                                     current_data = self.current_data,
                                     forecast_data = self.forecast_data,
                                     location = self.location,
                                     color = self.color)
        
        # wide widget
        if not self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = WideWidget(self,
                                     current_data = self.current_data,
                                     forecast_data = self.forecast_data,
                                     location = self.location,
                                     color = self.color)
        
        # min widget
        if not self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = SmallWidget(self,self.current_data,self.location,self.color)


if __name__ == "__main__":
    with urllib.request.urlopen("https://ipapi.co/json/") as url:
        data = json.loads(url.read().decode())
        city = data['city']
        country = data['country_name']
        latitude = data['latitude']
        longtitute = data['longitude']

    current_data = get_weather(latitude,longtitute,"metric","today")
    forecast_data = get_weather(latitude,longtitute,"metric","forecast")

    App(current_data=current_data,forecast_data=forecast_data,city=city,country=country)