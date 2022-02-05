import time

from scli.commands.base import BaseCommand
from scli.utils import option


class Command(BaseCommand):
    name = "check"
    description = "Checks the validity of the project"
    help = "Check the validity of the project"
    options = [
        option(
            long_name="force",
            short_name="f",
            description="Force check",
            flag=True,
        )
    ]

    @staticmethod
    def check():
        time.sleep(0.1)

    def handle(self):
        if self.option("force"):
            self.comment("Force checking ...")
        else:
            self.line("Checking ...")

        time.sleep(1)
        progress = self.progress_bar(10)
        for i in range(10):
            self.check()
            progress.advance()
        progress.finish()

        self.info("\nChecking succeeded!")
