from configparser import RawConfigParser

BASE_DIR = "/etc/mqtt-doorbell/"
CONFIG_FILE = "/etc/mqtt-doorbell/doorbell.conf"
BROKER_SECTION = 'broker'
BELL_SECTION = 'bell'

config = RawConfigParser()
config.read(CONFIG_FILE)

BROKER_SERVER = config.get(BROKER_SECTION, "server", fallback="localhost")
BROKER_PORT = int(config.get(BROKER_SECTION, "port", fallback="1883"))
BROKER_USER = config.get(BROKER_SECTION, "user", fallback="broker_user")
BROKER_PASSWORD = config.get(BROKER_SECTION, "password", fallback="broker_password")
BROKER_TOPIC = config.get(BROKER_SECTION, "topic", fallback="doorbell/ring")
BELL_DEFAULT_RING = config.get(BELL_SECTION, "default_ring", fallback="classic-doorbell-meloboom")
BELL_MP3PLAYER_CMD = config.get(BELL_SECTION, 'mp3player_cmd', fallback="mpg123 -qf32768")


