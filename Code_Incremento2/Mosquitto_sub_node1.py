import paho.mqtt.client as mqtt

def fxOn_connect(client, userdata, flagas, rc):
    print("Se conectó con mqtt "+ str(rc))
    client.subscribe("Tesis_ESP/Node1")

def fxOn_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = fxOn_connect
client.on_message=fxOn_message

client.connect("servermqtt.local")
client.loop_forever()