#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
class EmojiLoader():
    def __init__(self):
        self.map = {}
        path = "/".join(str(os.path.abspath(__file__)).split("/")[:-1])+"/emoji.json"
        with open(path) as f:
            self.map = json.load(f)
    
    def run(self):
        IS_TITLE = False
        for line in sys.stdin:
            line = line.strip()
            if IS_TITLE:
                for k in self.map:
                    if k in line:
                        line = line.replace(k, self.map[k]["emoji"], 1)
                        break
            if line == "":
                IS_TITLE = not IS_TITLE
            print(line)

emojiLoader = EmojiLoader()
emojiLoader.run()


