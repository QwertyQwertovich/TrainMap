import requests
import json
def conv(h,m):
    return h*60+m
class train:
    def __init__(self, start, number, stops):
        self.start = start
        self.number = number
        self.stops = stops
class stop:
    def __init__(self, dep, esr):
        self.dep = dep
        self.esr = esr
def get_rasp():
    x = requests.get("https://api.rasp.yandex.net/v3.0/search?apikey=29a0fe51-dbc1-4d92-bcab-bb2c68daa9c9&from=038205&to=039301&format=json&lang=ru_RU&date=2021-05-09&transport_types=suburban&system=esr&show_systems=esr&transport=false")
    xx = json.loads(x.text)
    xx = xx['segments']
    links = []
    trains = []
    for i in xx:
        links.append(i["thread"]["thread_method_link"]+"&apikey=29a0fe51-dbc1-4d92-bcab-bb2c68daa9c9&show_systems=esr")
    for u in links:
        x = requests.get(u)
        xx = json.loads(x.text)
        number = xx["number"]
        stops = []
        for i in xx["stops"]:
            if i["departure"]:

                stops.append(stop(i[]))
    print(links)
get_rasp()