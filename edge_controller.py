import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    print("Connected to a broker 172.31.100.2:9999!")
    client.subscribe("test")

def on_message(client, userdata, message):
    print("Proxy data to 172.31.100:9999: ", message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883)
client.loop_forever()
