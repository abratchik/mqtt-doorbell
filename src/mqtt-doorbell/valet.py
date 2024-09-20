import json

import paho.mqtt.client as mqtt

import sys
import subprocess
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

logger.debug("Logger started")


def on_connect(client, userdata, flags, reason_code, properties):
    logger.info("Connected With Result Code (%s)" % reason_code.getName())


def on_disconnect(client, userdata, reason_code, properties):
    logger.info("Client Got Disconnected")


def on_message(client, userdata, message):
    logger.info("Message Recieved: " + message.payload.decode())
    try:
        payload = json.loads(message.payload.decode())
        ringtone = payload.get("ringtone", settings.BELL_DEFAULT_RING)

        play_command = "%s %smedia/%s.mp3" % (settings.BELL_MP3PLAYER_CMD,
                                              settings.BASE_DIR,
                                              ringtone)
        logger.debug("subprocess.run: %s" % play_command)
        subprocess.run(play_command, shell=True)
    except Exception as e:
        logger.error("Error playing sound: %s" % e)
        logger.exception(e)


logger.info("Preparing MQTT client")

client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.username = settings.BROKER_USER
client.password = settings.BROKER_PASSWORD

logger.info("Connecting to %s:%d" % (settings.BROKER_SERVER, settings.BROKER_PORT))

try:
    res_err = client.connect(host=settings.BROKER_SERVER,
                             port=settings.BROKER_PORT)

    if res_err:
        logger.error("Failed to connect, error %d", res_err)
    else:
        client.subscribe(settings.BROKER_TOPIC)

        client.loop_forever()
except Exception as e:
    logger.error("Exception in the mqtt-doorbell service: %s" % e)
