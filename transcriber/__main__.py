import logging
import webbrowser
import os
from parser.parser import TranscriptParser
from formatter.htmlFormatter import HtmlFormatter

# TODO: replace with CLI param
logging.basicConfig(level=logging.DEBUG)
printScreenMessages = True
path = "../resources/asrOutput.json"


def screenMessage(msg):
    if printScreenMessages:
        print(msg)


def main():
    screenMessage("AWS transcrip")
    parser = TranscriptParser(path)
    screenMessage(f"Path in parser: {parser.getJsonPath()}")
    data = parser.parse()
    screenMessage(f"AWS account: {data['accountId']}")
    screenMessage(f"JobName: {data['jobName']}")
    htmlFormatter = HtmlFormatter(data)
    # TODO: pass format options
    html = htmlFormatter.format()
    print(html)
    # TODO: create module for file management
    outputFile = f"./target/{data['jobName']}.html"
    with open(outputFile, "w") as fh:
        fh.write(html)

    webbrowser.open('file://' + os.path.realpath(outputFile))


if __name__ == "__main__":
    main()
