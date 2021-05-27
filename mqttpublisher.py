import paho.mqtt.client as mqtt 

broker_address="192.168.86.42" 
#broker_address="iot.eclipse.org" #use external broker

# create a client instance - client id must be provided and must be unique
# there are other parameters (optional): Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
client = mqtt.Client("ID2") 

# connect to the broker - host must be provided
# there are other parameters (optional): connect(host, port=1883, keepalive=60, bind_address="")
client.connect(broker_address, port=1883)

# publish a message into the topic - topic and payload must be provided
# there are other parameters (optional): publish(topic, payload=None, qos=0, retain=False)
topic = "house/texttospeech"
payload = "hello world - from Python Client App"
client.publish(topic,payload)
print("message on topic ", topic, " = ", payload)