
from os import environ

BROKER_SERVER = environ.get('BROKER_SERVER', 'mqtt')
BROKER_PORT = int(environ.get('BROKER_PORT', 1833))
BROKER_USER = environ.get('BROKER_USER', 'BROKER_USER')
BROKER_PASSWORD = environ.get('BROKER_PASSWORD', 'BROKER_PASSWORD')

BELL_TOPIC = environ.get('BELL_TOPIC', '')
