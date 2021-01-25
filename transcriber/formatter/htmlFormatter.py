import logging
import json
import jinja2
from datetime import datetime


class HtmlFormatter:

    def __init__(self, source):
        self.data = source
        now = datetime.utcnow()
        self.model = {
            "startTime": str(now)
        }

    def format(self):
        self._buildModel()
        html = jinja2.Environment(
            loader=jinja2.FileSystemLoader('./../resources')
        ).get_template('template.jinja.html').render(
            title=self.model['title'],
            sentences=self.model['data']['sentences'],
            metadata=self._buildMetadata())

        return html

    def _buildModel(self):
        self.model['title'] = f"Transcription {self.data['jobName']}"
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
        return {
            'speakers': self.model['data']['speakers'],
            'items': self.model['data']['items']
        }

    def _getSymbolsInSegment(self, itemCounter, itemsInSegment):
        symbols = []
        itemsRead = 0
        itemsCounter = 0
        itemsInSegmenRaw = self.data['results']['items'][itemCounter:]
        logging.debug(
            f"getting {itemsInSegment} starting in {itemCounter} contaings {len(itemsInSegmenRaw)}")
        while itemsCounter < itemsInSegment:
            item = itemsInSegmenRaw[itemsRead]
            symbols.append(self._buildEntry(item))
            if item['type'] != "punctuation":
                itemsCounter += 1
            itemsRead += 1

        # Adding next to the segment if it's punctuation
        if len(itemsInSegmenRaw) > itemsRead and itemsInSegmenRaw[itemsRead]['type'] == "punctuation":
            symbols.append(self._buildEntry(itemsInSegmenRaw[itemsRead]))
            logging.debug("Punctuation inserted as last item in segment")
            itemsRead += 1
        return symbols, itemsRead

    def _mapConficenceClass(self, confidence):
        if float(confidence) < 0.5:
            return "bad"
        elif float(confidence) < 0.8:
            return "medium"
        else :
            return "ok"
    
    def _buildEntry(self, item):
        return {
                'entry': item['alternatives'][0]['content'],
                'confidence': self._mapConficenceClass(item['alternatives'][0]['confidence']),
                'type' : item['type']
                }
