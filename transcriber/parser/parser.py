import logging
import json


class TranscriptParser:

    def __init__(self, path=None):
        logging.debug(f"Path: {path}")
        self.jsonPath = path

    def getJsonPath(self):
        return self.jsonPath

    def parse(self):
        with open(self.jsonPath) as json_file:
            data = json.load(json_file)
        return data
