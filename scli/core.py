from cleo import Command
from cleo.helpers import argument  # noqa
from cleo.helpers import option  # noqa

__all__ = [
    "argument",
    "BaseCommand",
    "option",
]


class BaseCommand(Command):
    def progress_bar(self, max=0):  # noqa
        progress = super().progress_bar(max)
        progress.set_format("verbose")
        progress.set_bar_character("<comment>█</comment>")
        progress.set_empty_bar_character("•")
        progress.set_progress_character("")
        return progress

    def handle(self):
        raise NotImplementedError()
