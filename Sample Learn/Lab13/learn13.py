import network, urequests, ujson
from machine import Pin

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('2-3N-4F-2.4G', '0905235629')

while not sta_if.isconnected():
    pass

print(sta_if.ifconfig()[0])

res = urequests.get(
    "https://api.openweathermap.org/data/2.5/weather?" +
    "q=" + "Kaohsiung" + ",TW" +      # 指定城市與國別
    "&units=metric&lang=zh_tw&" +  # 使用攝氏單位
    "appid=" +  # 以下填入註冊後取得的 API key
    "59c73f52674ad94402bc8ab13a531d2d"
)

Jdict = ujson.loads(res.text)

G_LED = Pin(16, Pin.OUT)
R_LED = Pin(14, Pin.OUT)

weatherID = Jdict["weather"][0]["id"]
weatherDesc = Jdict["weather"][0]["description"]

if weatherID < 800:
    R_LED.value(1)
    G_LED.value(0)
else:
    R_LED.value(0)
    G_LED.value(1)

print("目前天氣：", str(weatherID))
print("代碼意義：", weatherDesc )