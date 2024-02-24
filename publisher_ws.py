import paho.mqtt.client as mqtt
import json
publisher = mqtt.Client(client_id = "cdacsensor1", protocol=mqtt.MQTTv311, transport="websockets")

#Topic for publishing
TOPIC = 'cdac/temp'


# The callback for when the client receives a CONNACK response from the server.
def on_connection(client, userdata, flags, rc):
    if rc == mqtt.MQTT_ERR_SUCCESS:
        print('Connected with Broker')
        value = {"temp": 13.5}

    #Parameters: TOPIC, Payload, QOS and Retain flag can be set
        publisher.publish(TOPIC, payload = json.dumps(value), qos=1, retain=True)
        print("Data published.....")
    else:
        print("Some Error occurd during Connection")

#Assign our method 
publisher.on_connect = on_connection 

# Connecting to the Broker; HOSTNAME, PORT, KeepAlive
publisher.connect("localhost", 8081)

#Adding the loop forever
publisher.loop_forever()
