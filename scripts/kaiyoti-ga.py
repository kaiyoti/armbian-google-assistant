#!/usr/bin/env python

# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function

import argparse
import os.path
import os
import json

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

def greenledon():
    value = open("/sys/class/leds/green_led/brightness","w")
    value.write(str(1))
    value.close()

def greenledoff():
    value = open("/sys/class/leds/green_led/brightness","w")
    value.write(str(0))
    value.close()

def redledon():
    value = open("/sys/class/leds/red_led/brightness","w")
    value.write(str(1))
    value.close()

def redledoff():
    value = open("/sys/class/leds/red_led/brightness","w")
    value.write(str(0))
    value.close()

def process_event(event):
    print(event)

    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        greenledon()
        os.system("/usr/bin/aplay /home/kaiyoti/media/kaiyoti-response.wav")

    if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        redledon()

    if event.type == EventType.ON_RESPONDING_FINISHED:
        redledoff()

    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        greenledoff()

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()

    greenledoff()
    redledoff()

    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event)


if __name__ == '__main__':
    main()
