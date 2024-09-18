import paho.mqtt.client as mqtt

import sys
import logging

from paho.mqtt.enums import CallbackAPIVersion

from . import settings

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def on_connect(client, userdata, flags, reason_code, properties):
    logger.info("Connected With Result Code (%s)" % reason_code.getName())


def on_disconnect(client, userdata, reason_code, properties):
    logger.info("Client Got Disconnected")


def on_message(client, userdata, message):
    logger.info("Message Recieved: " + message.payload.decode())


client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.username = settings.BROKER_USER
client.password = settings.BROKER_PASSWORD


res_err = client.connect(host=settings.BROKER_SERVER,
                         port=settings.BROKER_PORT)


if res_err:
    logger.error("Failed to connect to MQTT server, error %d", res_err)
else:
    logger.info("Connected to MQTT server %s" % settings.BROKER_SERVER)

    client.subscribe(settings.BELL_TOPIC)

    client.loop_forever()
