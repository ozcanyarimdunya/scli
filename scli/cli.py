from cleo.application import Application as BaseApplication

import scli
from scli.settings import INSTALLED_COMMANDS
from scli.utils import import_string


class Application(BaseApplication):
    def __init__(self):
        super().__init__("scli", scli.__version__)

        for cmd in INSTALLED_COMMANDS:
            path = "scli.commands.{}.Command".format(cmd)
            klass = import_string(path)
            self.add(klass())


def main():
    Application().run()
