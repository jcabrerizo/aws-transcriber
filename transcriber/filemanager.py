from sys import exit
import os
from os import path
import logging


class FileManager:

    def __init__(self, input, outputDir):
        self.input = input
        self.outputDir = outputDir

    def getFilesToProcess(self):
        targetFiles = []
        logging.debug(f'input: {self.input}')
        if path.isdir(self.input):
            logging.debug(f"Creating dir {self.input}")
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

    def saveJob(self, fileName, output, encoding):
        # Create dir if not exists
        if not path.isdir(self.outputDir):
            Path(self.outputDir).mkdir(parents=True, exist_ok=True)
            logging.debug(f'Created {self.outputDir}')
        outputFile = f"./{self.outputDir}/{fileName}.html"
        with open(outputFile, "w", encoding = encoding) as fh:
            fh.write(output)
        logging.debug(f'Created {outputFile}')
        return outputFile
