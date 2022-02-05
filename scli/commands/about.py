import scli
from scli.core import BaseCommand


class Command(BaseCommand):
    name = "about"
    description = "Shows information about scli"

    def handle(self):
        self.table(
            header=["scli", "✨ ✨ ✨"],
            rows=[
                ["version", scli.__version__],
                ["author", scli.__author__],
            ],
        ).render(self.io)
