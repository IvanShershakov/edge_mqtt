import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    client.subscribe("test")

def on_message(client, userdata, message):
    print("Get message: ", message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883)
client.loop_forever()
