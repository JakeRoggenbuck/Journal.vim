from datetime import date
from os import path, listdir
from typing import Tuple, List


def use_template(date: str):
    return f"Journal entry {date}"


class Journals:
    outfile_path = "/tmp/journal-viewer-temp-file.md"

    def __init__(self, journals_path: str):
        self.journals_path = journals_path

    @staticmethod
    def convert_date(date_: date) -> str:
        """Works for arbitrary date objects

        To be used later in date search / date summary
        """
        return date_.strftime("%b-%d-%Y")

    @classmethod
    def get_date(cls):
        return cls.convert_date(date.today())

    @staticmethod
    def wrap_date_for_filename(date) -> str:
        return f"journal_{date}.md"

    def get_filepath(self, name: str):
        return path.join(self.journals_path, name)

    def get_todays_filename(self) -> str:
        return self.wrap_date_for_filename(self.get_date())

    def check_todays_journal(self) -> bool:
        return path.isfile(self.get_filepath(self.get_todays_filename()))

    def new(self):
        todays_file = self.get_todays_filename()
        with open(self.get_filepath(todays_file), "w") as file:
            date = str(self.get_date())
            file.write(use_template(date))

    def open(self):
        if not self.check_todays_journal():
            self.new()
        return self.get_filepath(self.get_todays_filename())

    def search_single_word(self, word: str):
        paths = listdir(self.journals_path)
        for j_path in paths:
            with open(path.join(self.journals_path, j_path)) as file:
                text = file.read()
                num = text.count(word)

                if num > 0:
                    yield (num, j_path)

    def open_journal_viewer(self, entries: List[Tuple[int, str]]):
        with open(self.outfile_path, "w") as file:
            file.write("# Journal Viewer\n\n")
            for n, entry in enumerate(entries):
                file.write(f"{n}. {entry[0]} {entry[1]}\n")
