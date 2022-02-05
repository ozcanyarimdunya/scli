from cleo import Command

__all__ = [
    "BaseCommand",
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
