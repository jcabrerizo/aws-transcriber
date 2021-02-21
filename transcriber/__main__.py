import logging
import webbrowser
import os
from pathlib import Path
from parser import TranscriptParser
from formatter.htmlFormatter import HtmlFormatter
from cli_parser import CliParser

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

    input = args.input
    # TODO: allow only one file as input or a dir for a batch
    # TODO: move file logic to a file management module
    for inputFile in os.listdir(input):
        if inputFile.endswith(".json"):
            parser = TranscriptParser(f'{input}/{inputFile}')
            screenMessage(f"Path in parser: {parser.getJsonPath()}")
            model = parser.parse()
            jobName = model['metadata']['jobName']
            screenMessage(f"AWS account: {model['metadata']['accountId']}")
            screenMessage(f"JobName: {jobName}")
            htmlFormatter = HtmlFormatter(model)
            # TODO: pass format options
            output = htmlFormatter.format()
            if args.print_output:
                print(htmoutputl)
            # TODO: create module for file management            
            Path(args.output).mkdir(parents=True, exist_ok=True)
            outputFile = f"./{args.output}/{jobName}.html"
            screenMessage(f'Output file: {outputFile}')
            with open(outputFile, "w") as fh:
                fh.write(output)
            if openInBrowser:
                webbrowser.open('file://' + os.path.realpath(outputFile))
        else:
            continue



if __name__ == "__main__":
    main()
