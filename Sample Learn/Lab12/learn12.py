import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('2-3N-4F-5G', '0905235629')
while not sta_if.isconnected():
    pass
print(sta_if.ifconfig())