import logging
import webbrowser
import os
from parser.parser import TranscriptParser
from formatter.htmlFormatter import HtmlFormatter

# TODO: replace with CLI param
logging.basicConfig(level=logging.DEBUG)
printScreenMessages = True
path = "../resources/asrOutput.json"
openInBrowser = False

def screenMessage(msg):
    if printScreenMessages:
        print(msg)


def main():
    screenMessage("AWS transcrip")

    inputDirectory = r'../input'
    for inputFile in os.listdir(inputDirectory):
        if inputFile.endswith(".json"):
            parser = TranscriptParser(f'{inputDirectory}/{inputFile}')
            screenMessage(f"Path in parser: {parser.getJsonPath()}")
            data = parser.parse()
            screenMessage(f"AWS account: {data['accountId']}")
            screenMessage(f"JobName: {data['jobName']}")
            htmlFormatter = HtmlFormatter(data)
            # TODO: pass format options
            html = htmlFormatter.format()
            # TODO: add parameter for printing it
            #    print(html)
            # TODO: create module for file management
            outputFile = f"./target/{data['jobName']}.html"
            with open(outputFile, "w") as fh:
                fh.write(html)
            if openInBrowser:
                webbrowser.open('file://' + os.path.realpath(outputFile))
        else:
            continue



if __name__ == "__main__":
    main()
