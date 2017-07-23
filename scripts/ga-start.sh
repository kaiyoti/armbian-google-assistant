#!/bin/bash

# Depending on the audio interface, some usb audio devices may automatically turn on mic
# This is workaround to mute mic during playback
amixer -c 2 sset Mic Playback unmute
amixer -c 2 sset Mic Playback mute
aplay /home/kaiyoti/media/kaiyoti-startup.wav &
. /home/kaiyoti/env/bin/activate
googlesamples-assistant-hotword
