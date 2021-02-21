import logging
import json
from datetime import datetime


class TranscriptParser:

    def __init__(self, path=None):
        logging.debug(f"Path: {path}")
        self.jsonPath = path
        now = datetime.utcnow()
        self.model = {
            "startTime": str(now)
        }

    def getJsonPath(self):
        return self.jsonPath

    def parse(self):
        # TODO: definir parámetros para encoding
        with open(self.jsonPath, encoding="utf-8") as json_file:
            self.data = json.load(json_file)
        self._buildModel()
        self._buildMetadata()
        return self.model

    def _buildModel(self):
        self.model['title'] = f"{self.data['jobName']}"
        self.model['data'] = {}
        self.model['data']['speakers'] = self.data['results']['speaker_labels']['speakers']

        segmentCounter = 0
        self.model['data']['sentences'] = []
        for segment in self.data['results']['speaker_labels']['segments']:
            itemsInSegment = len(segment['items'])
            symbols, itemsRead = self._getSymbolsInSegment(
                segmentCounter, itemsInSegment)
            newSentence = {
                'speaker': segment['speaker_label'],
                'symbols': symbols
            }
            self.model['data']['sentences'].append(newSentence)
            segmentCounter += itemsRead

        self.model['data']['items'] = segmentCounter
#        logging.debug(f'Model: {self.model}')

    def _buildMetadata(self):
        self.model['metadata'] = {
            'speakers': self.model['data']['speakers'],
            'items': self.model['data']['items'],
            'accountId': self.data['accountId'],
            'jobName': self.data['jobName']
        }

    def _getSymbolsInSegment(self, itemCounter, itemsInSegment):
        symbols = []
        itemsRead = 0
        itemsCounter = 0
        itemsInSegmenRaw = self.data['results']['items'][itemCounter:]
#        logging.debug(
#             f"getting {itemsInSegment} starting in {itemCounter} contaings {len(itemsInSegmenRaw)}")
        while itemsCounter < itemsInSegment:
            item = itemsInSegmenRaw[itemsRead]
            symbols.append(self._buildEntry(item))
            if item['type'] != "punctuation":
                itemsCounter += 1
            itemsRead += 1

        # Adding next to the segment if it's punctuation
        if len(itemsInSegmenRaw) > itemsRead and itemsInSegmenRaw[itemsRead]['type'] == "punctuation":
            symbols.append(self._buildEntry(itemsInSegmenRaw[itemsRead]))
#            logging.debug("Punctuation inserted as last item in segment")
            itemsRead += 1
        return symbols, itemsRead

    def _mapConficenceClass(self, confidence):
        if float(confidence) < 0.5:
            return "bad"
        elif float(confidence) < 0.8:
            return "medium"
        else:
            return "ok"

    def _buildEntry(self, item):
        return {
            'entry': item['alternatives'][0]['content'],
            'confidence': self._mapConficenceClass(item['alternatives'][0]['confidence']),
            'type': item['type']
        }
