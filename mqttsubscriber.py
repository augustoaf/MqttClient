import paho.mqtt.client as mqtt 
import time
import datetime

# callback method to receive the message when published on the topic this client has subscribed
def on_message(client, userdata, message):
    print("message received= ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

# callback method to act when the connection is closed by the broker or by the client
def on_disconnect(client, userdata, rc):
    print("client disconnected status: ", rc)

def on_connect(client, userdata, flags, rc):
    print("client connected status: ", rc)
    client.subscribe("house/teste")

# callback method for log
def on_log(client, userdata, level, buf):
    print('log on ', str(datetime.datetime.now()) , ': ', buf)

def main():

    client = ""

    try:

        broker_address="192.168.86.42" 
        #broker_address="iot.eclipse.org" #use external broker

        # create a client instance - client_id may be provided and must be unique, if not provided the paho client will set a random id
        # there are other parameters (optional): Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
        # clean_session (True by default) is a parameter which indicates if the Mqtt Broker must remember the client about the subscriptions in case of a reconnection and also to store messages during the connection lost (to receive the stored messages when connection restablished, the publish and subsbribe must use QOS equals to 1 or above - default is QOS 0 which does not guarantee message delivery/storage)
        client = mqtt.Client()
        
        # connect to the broker - host must be provided
        # there are other parameters (optional): connect(host, port=1883, keepalive=60, bind_address="")
        client.connect(broker_address, port=1883, keepalive=10)

        # subscribe to a topic - topic must be provided
        # there are other parameters (optional): subscribe(topic, qos=0)
        #client.subscribe("house/teste") # instruction moved to on_connect callback method in order to subscribe again in case of disconnection (if disconnected and clean_session=True, the subscription will be empty when connected again)

        #bind callback functions
        client.on_message=on_message
        client.on_log=on_log
        client.on_connect=on_connect
        client.on_disconnect=on_disconnect

        #start the loop to "hear" the callbacks and also try to reconnect automatically (usually the reconnect happens between 3 to 6 seconds)
        client.loop_start() 

        while True:
            time.sleep(10)
            print(".")

    except KeyboardInterrupt:
        client.loop_stop() 
        client.disconnect()
        print ( "App stopped" )

if __name__ == '__main__':
    print ( "Press Ctrl-C to exit" )
    main()