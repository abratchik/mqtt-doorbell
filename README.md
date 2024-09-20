# Simple MQTT Door Bell 
A simple Linux-based doorbell, which plays the mp3 bell ringtone upon receiving 
a MQTT message.

The main idea is to create a system service, which can play an audio file
upon receiving the message from the MQTT message broker. This may be useful
for configuring sound notifications or alarms in the Home Assistant 
automations.

## Supported platforms
This solution has been tested on Ubuntu 22.04, but most likely will work on 
other Linux distros, with minor changes.

## Prerequisites

1. Mosquitto MQTT message broker installed and accessible from the deployment
   machine.
   
2. MP3 player utility, which can play mp3 files from the command line, installed
   on the host machine. I used mpg123 but other options should work as well.
   
3. Python verison >= 3.10 

## Installation
First please ensure all pre-requisites are in place. Testing your MP3 player
from the command line on the host where you plan to deploy this tool is the 
first step - you need to ensure that mp3 files are played as expected. 

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

Next, clone this repo to some folder on your disk:

```$ git clone https://github.com/abratchik/mqtt-doorbell ```

## Configuration



