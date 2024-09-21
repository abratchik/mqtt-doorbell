# Simple MQTT Door Bell 
A simple Linux-based doorbell, which plays the mp3 ringtone upon receiving 
a special MQTT message.

The main idea is to create a system service, which can play an audio file
upon receiving the message from the MQTT message broker. This may be useful
for configuring sound notifications or alarms in the 
[Home Assistant](https://www.home-assistant.io/) automations.

This module also supports random ringtones based on a pattern. This means the same
message may result in random ringtones being played based on the pattern received
in the MQTT message.

## Supported platforms
This solution has been tested on Ubuntu 22.04, but most likely will work on 
other Linux distros, with minor changes.

## Prerequisites

1. Mosquitto MQTT message broker installed and accessible from the deployment
   machine. You will need to create credentials (user/password) on the MQTT 
   broker server for this solution.
   
2. MP3 player utility, which can play mp3 files from the command line, installed
   on the host machine. I used mpg123 but other options should work as well.
   
3. Python verison >= 3.10 + pip.

## Installation
First please ensure all pre-requisites are in place. Testing your MP3 player
from the command line on the host where you plan to deploy this tool is the 
first step - you need to ensure that mp3 files are played as expected. 

Please note that the following commands will require administrative grants, 
so please don't forget to start them with **sudo** if required. 

For example, here is the command for the **mpg123** utility:

```$ mpg123 -qf32768 -adefault:CARD=Speaker /path/to/ringtone.mp3```

In this command, the number after the -qf option represents the volume, which 
can range from -32767 to 32768.  

Second, we need to create a user profile, which will run the mqtt-doorbell
service:

``` 
$ useradd -M doorbell
$ usermod -L doorbell
$ groupadd doorbell
$ usermod -a -G doorbell,audio doorbell 
```

Install the solution with the following command (must be under **sudo**!):

```
$ sudo pip install mqtt-doorbell
```

Next step is to configure the mqtt-doorbell service

## Configuration 
First we need to create the configuration file **doorbell.conf** in the 
**/etc/mqtt-doorbell** folder. The file should be as follows:

```
[broker]
server	 = localhost
port	 = 1883
user	 = mqtt_user 
password = mqtt_password
topic	 = doorbell/ring

[bell]
default_ring  = classic-doorbell
mp3player_cmd = mpg123 -qf32768 -adefault:CARD=Speaker
```

Please ensure to update the MQTT broker username and password accordingly. 

Then, we need to create the **mqtt-doorbell.service** service configuration 
file in the **/lib/systemd/system** folder, as follows:

```
[Unit]
Description=MQTT Doorbell Service

[Service]
WorkingDirectory=/etc/mqtt-doorbell/
ExecStart=/usr/bin/python3 -m mqtt-doorbell.valet
Type=simple
User=doorbell
Group=doorbell
Restart=always

[Install]
WantedBy=multi-user.target
```

Next, we need to create a media folder **/etc/mqtt-doorbell/media** and
place there all the mp3 files we want to use as ringtones. You may download 
the ringtones from [here](https://github.com/abratchik/mqtt-doorbell/tree/main/src/media)
or use your own mp3 files. 

Finally we can enable and start the service:

```
$ systemctl enable mqtt-doorbell.service
$ systemctl start mqtt-doorbell.service
```

## Usage

In order to trigger the ringtone you will need to send the following MQTT 
message to the **doorbell/ring** topic:

```json
{"ringtone": "filename_pattern"}
```

where the **filename_pattern** should match the name of an MP3 file or files
in the **media** folder. A random ringtone from the search result will be 
played in case of multiple match.