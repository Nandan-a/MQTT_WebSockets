# A program to write MQTT  web-subscriber
# Broker:Mosquitto.Localhost

import paho.mqtt.client as mqtt
import json

subscriber = mqtt.Client(client_id="cdacsensor1",protocol=mqtt.MQTTv5,transport="websockets")
TOPIC='cdac/temp'

#Setting the username password: USERNAME | PASSWORD
subscriber.username_pw_set("motor","ktm")



# set my will to the broker :topic |payload |QoS | RETAIN
WILL_TOPIC = 'device/dead'
subscriber.will_set(WILL_TOPIC,"Sensor DHT22 is offline.")
# a callback for mqtt server
def on_connection(client,userdata,flags,rc,properties):
    if rc == mqtt.MQTT_ERR_SUCCESS:
        print("I'm connected to MQTT Broker now.")
        # Subscribe to the topic here
        subscriber.subscribe(TOPIC)
    else:
        print("Error during connection")


# Define a callback method to receive MQTT Messages
def on_receive(client,userdata,msg):
    parsed_msg=json.loads(msg.payload)
    print(f'Topic: {msg.topic},Message: {parsed_msg["temp"]}')
    try:
        payload = parsed_msg
        if payload["temp"]>30:
            print("starting the fan now...")
    except:
        print("error in json parsing")
            
subscriber.on_connect = on_connection
subscriber.on_message = on_receive


# Requestion connection to broker here: HOST,port,keeepalive
subscriber.connect("localhost",8081)

subscriber.loop_forever()