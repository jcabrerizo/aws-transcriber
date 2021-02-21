from sys import exit
import os
from os import path
import logging


class FileManager:

    def __init__(self, input, output):
        self.input = input
        self.output = output

    def getFilesToProcess(self):
        targetFiles = []
        logging.debug(f'input: {self.input}')
        if path.isdir(self.input):
            logging.debug(f"reading dir {self.input}")
            for inputFile in os.listdir(self.input):
                logging.debug(f'{inputFile}')
                if inputFile.endswith(".json"):
                    logging.debug(f'Adding {inputFile}')
                    targetFiles.append(self.input + '/' + inputFile)
        elif path.isfile(self.input) and self.input.endswith(".json"):
            targetFiles.append(self.input)
        else:
            exit(f"'{self.input}' is a special file and can't be processed")

        logging.debug(f"target {targetFiles}")
        return targetFiles
