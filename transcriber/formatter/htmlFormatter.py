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
        ).get_template('template.html.jinga').render(
            title=self.model['title'],
            sentences=self.model['data']['sentences'])

        return html

    def _buildModel(self):
        self.model['title'] = f"Transcription {self.data['jobName']}"
        # self.data['results']['speaker_labels'].len
        # TODO: replace mock object
        self.model['data'] = {
            'sentences': [
                {
                    'speaker': 'speaker_one',
                    'words': [
                        {
                            'word': 'This',
                            'confidence': 'ok'
                        },
                        {
                            'word': 'is',
                            'confidence': 'medium'
                        },
                        {
                            'word': 'it',
                            'confidence': 'bad'
                        },
                    ]
                },
                {
                    'speaker': 'speaker_two',
                    'words': [
                        {
                            'word': 'Fire',
                            'confidence': 'bad'
                        },
                        {
                            'word': 'walk',
                            'confidence': 'ok'
                        },
                        {
                            'word': 'with',
                            'confidence': 'medium'
                        },
                        {
                            'word': 'me',
                            'confidence': 'medium'
                        },
                    ]
                }
            ]
        }
        logging.debug(f'Model: {self.model}')
