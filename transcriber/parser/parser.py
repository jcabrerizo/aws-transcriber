import logging
import json


class TranscriptParser:

    def __init__(self, path=None):
        logging.debug(f"Path: {path}")
        self.jsonPath = path

    def getJsonPath(self):
        return self.jsonPath

    def parse(self):
        # TODO: definir parámetros para encoding
        with open(self.jsonPath,encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
