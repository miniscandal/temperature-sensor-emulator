'''
	Este es un script que utiliza la biblioteca paho-mqtt para conectarse a un
    servidor MQTT local y publicar y suscribirse a temas relacionados con sensores.
    
    El script recibe como argumentos un identificador de dispositivo único y un intervalo
    en segundos para repetir una publicación. El script define varias funciones para
    manejar diferentes acciones, como salir del sistema operativo, encender y
    apagar, actualizar y cancelar. También incluye una función para publicar mensajes
    en el tema de monitoreo de sensores.
    
    En el bucle principal, el script publica mensajes con valores aleatorios
    de humedad y temperatura si el cliente está conectado y no ha recibido una
    acción de salida.
'''

import paho.mqtt.client as mqtt
import random
import time
import argparse
import json
import os

MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC_SUBSCRIBE = "sensor"
MQTT_TOPIC_PUBLISH = "sensor_monitoring"

def on_connect(client, userdata, flags, rc):
    client.connected_flag = True;
    print("Connected with result code %s"%(rc))

def on_disconnect(client, usedata, rc):
    client.connected_flag = False
    print("Disconnect with result code %s"%(rc))

def on_message(client, userdata, msg):
    print("topic: %s, payload: %s"%(msg.topic, msg.payload))
    json_object = json.loads(msg.payload)
    switcher.get(json_object['action'])(client, json_object)

def publish_message(client, message):
    print(f'publish: { message }')
    client.publish(MQTT_TOPIC_PUBLISH, message)

def osExit(client, json_object):
    client.connected_flag = True
    client.status_report = 'exit'
    message = '{"id_device": "%s", "status_report": "%s"}'%(args.id, client.status_report)
    publish_message(client, message)
    print("OS exit")

def offOn(client, json_object):
    client.connected_flag = not client.connected_flag
    response = 'on' if client.connected_flag else 'off'
    client.status_report = response
    message = '{"id_device": "%s", "status_report": "%s"}'%(args.id, response)
    publish_message(client, message)
    print("Status %s"%(response))

def update(client, json_object):
    client.connected_flag = True
    client.status_report = 'update'
    message = '{"id_device": "%s", "status_report": "%s"}'%(args.id, client.status_report)
    publish_message(client, message)
    print("Status %s"%(client.status_report))

def cancel(client, json_object):
    client.connected_flag = True
    client.status_report = 'on'
    message = '{"id_device": "%s", "status_report": "%s"}'%(args.id, client.status_report)
    publish_message(client, message)
    print("Status %s"%(client.status_report))

def command(client, json_object):
    message = '{"id_device": "%s", "status_report": "%s"}'%(args.id, "command")
    publish_message(client, message)
    client.unsubscribe("%s/%s"%(MQTT_TOPIC_SUBSCRIBE, args.id))
    args.id = json_object['command']['set-id-device']
    client.subscribe("%s/%s"%(MQTT_TOPIC_SUBSCRIBE, args.id))
    client.status_report = 'on'

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", required=True, help="unique device identifier")
parser.add_argument("-s", "--seconds", default="1", help="interval in seconds to repeat a post")
args = parser.parse_args()

client = mqtt.Client()
client.connected_flag = False
client.status_report = 'on'
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
client.subscribe("%s/%s"%(MQTT_TOPIC_SUBSCRIBE, args.id))
client.loop_start()

switcher = {
    'exit': osExit,
    'offOn': offOn,
    'update': update,
    'command': command,
    'cancel': cancel,
}

while True:
    if client.connected_flag:
        humidity = random.randint(0, 100)
        temperature = random.randint(0, 90)
        message = '{"id_device": "%s", "status_report": "%s", "humidity": %i, "temperature": %i }'%(args.id, client.status_report, humidity, temperature)
        publish_message(client, message)
        time.sleep(int(args.seconds))
    if client.status_report == 'exit':
        os._exit(0)