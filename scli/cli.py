from cleo.application import Application as BaseApplication

import scli
from scli.utils import import_string

COMMANDS = [
    "scli.commands.about.Command",
    "scli.commands.check.Command",
]


class Application(BaseApplication):
    def __init__(self):
        super().__init__("scli", scli.__version__)

        for cmd in COMMANDS:
            klass = import_string(cmd)
            self.add(klass())


def main():
    Application().run()
