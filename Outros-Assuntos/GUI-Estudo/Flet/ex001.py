import json
import pprint
import time
import flet as ft
import requests


def get_time():
    try:
        request = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=30bc4efcb11c829301b50208ea6aca20")
        weather = json.loads(request.text)
        pprint.pprint(weather)

        weather_description = dict
        weather_description = {"title": weather['weather'][0]['main'],
                               "description": weather['weather'][0]['description'],
                               "temp_min": weather['main']["temp_min"], "temp_min": weather['main']["temp_max"]}

        return weather_description
    except:
        return None


class Gui:
    def __init__(self, page: ft.page):
        self.title = "Weither App"
        self.weathter = get_time()
        self.page = page

    def build_gui(self):
        self.page.add(self.title)
        self.page.add(ft.Text)

        self.page.add(ft.Text(self.weathter["title"]))
        self.page.update()

    def update_time(self):
        self.weathter = get_time()


def main(page: ft.page):
    gui = Gui(ft.page)
    gui.build_gui()


ft.app(target=main)
