from argparse import ArgumentParser

class CliParser:
    def create_parser(self):
        parser = ArgumentParser()

        parser.add_argument("-i","--input",
                            help="Imput file or dir",
                            default="./input"
                            )
        parser.add_argument("-o", "--output",
                            help="Output dir",
                            default="./output"
                            )
        parser.add_argument("--input-encoding",
                            help="Source file encoding",
                            default="UTF8"
                            )
        parser.add_argument("--output-encoding",
                            help="Source file encoding",
                            default="UTF8"
                            )

        parser.add_argument("-f", "--formater",
                            help="Formater",
                            default="html"
                            )
        parser.add_argument("--silent",
                            help="Hide app messages",
                            action="store_false",
                            )
        parser.add_argument("-d", "--debug-level",
                            help="Debug level",
                            choices=[
                                'CRITICAL',
                                'FATAL',
                                'ERROR',
                                'WARNING',
                                'WARN',
                                'INFO',
                                'DEBUG',
                                'NOTSET',
                            ],
                            default="INFO"
                            )
        parser.add_argument("--dry-run",
                            help="Do no save the converted text to a file",
                            action="store_true"
                            )
        parser.add_argument("--print-output",
                            help="Print output file on the console",
                            action="store_true"
                            )
        return parser