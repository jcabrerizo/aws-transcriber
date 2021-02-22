import logging
import webbrowser
import os
from pathlib import Path

from parser import TranscriptParser
from formatter.htmlFormatter import HtmlFormatter
from cli_parser import CliParser
from filemanager import FileManager

args = CliParser().create_parser().parse_args()

logging.basicConfig(level=logging._nameToLevel[args.debug_level])
logging.debug(f"Efective execution arguments: {args}")

printScreenMessages = args.silent
openInBrowser = args.browser


def screenMessage(msg):
    if printScreenMessages:
        print(msg)


def main():
    screenMessage("AWS transcribe viewer")

    filemanager = FileManager(args.input, args.output)
    for inputFile in filemanager.getFilesToProcess():
        parser = TranscriptParser(inputFile, args.input_encoding)
        screenMessage(f"File to be parsed: {parser.getJsonPath()}")
        model = parser.parse()
        jobName = model['metadata']['jobName']
        screenMessage(f"AWS account: {model['metadata']['accountId']}")
        screenMessage(f"JobName: {jobName}")
        # TODO: create format factory and pass format options
        htmlFormatter = HtmlFormatter(model)
        output = htmlFormatter.format()
        if args.print_output:
            print(htmoutputl)
        outputFile = filemanager.saveJob(jobName, output, args.output_encoding)
        screenMessage(f'Output file: {outputFile}')
        if openInBrowser:
            webbrowser.open('file://' + os.path.realpath(outputFile))


if __name__ == "__main__":
    main()
