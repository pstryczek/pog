import json
import websocket
from datetime import datetime
from db import db

from models.flashes import FlashesModel

try:
    import thread
except ImportError:
    import _thread as thread


def on_message(ws, message):
    msg = json.loads(message)

    dt = datetime.fromtimestamp(int(msg["time"]) // 1e9)
    s = dt.strftime('%Y-%m-%d %H:%M:%S')
    flashlight = json.dumps([{"time": s, "lat": msg["lat"], "lon": msg["lon"], "region": msg["region"], "delay": msg["delay"]}])
    flash_id = FlashesModel.objects.count()
    flash_id += 1
    time = s
    lat = float(msg["lat"])
    lon = float(msg["lon"])
    region = int(msg["region"])
    delay = float(msg["delay"])

    flashes = Flashes(flash_id=flash_id, time=time, lat=lat, lon=lon, region=region,delay=delay)
    flashes.save()



def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"west":-180,"east":180,"north":90,"south":-90}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://ws2.blitzortung.org:8050/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    ws.run_forever()
    ws.close()

# driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
# temp = []
# driver.get("http://91.220.17.198/Zakopane/1")
# content = driver.page_source
# soup = BeautifulSoup(content, features="html.parser")
# for a in soup.findAll('a', href=True, attrs={'class': 'col-xs-6 set text-left'}):
#     dzistemp = a.find('div', attrs={'class': 'col-xs-12 temp'})
#     print(temp.a.append(dzistemp.text))


# odpowiedz = urllib.request.urlopen("http://91.220.17.198/data/region/Zakopane")
#
# y = json.loads(odpowiedz.read())
# for x in y["data"]['stations']:
#     print(y["data"]["stations"][x]["name"])
#     print(y["data"]["stations"][x]["position"])
