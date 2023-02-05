from datetime import date
from os import path, listdir
from typing import Tuple, List

class Journals:
    outfile_path = "/tmp/journal-viewer-temp-file"

    def __init__(self, journals_path, date_format, title_template):
        self.journals_path = journals_path
        self.date_format = date_format
        self.title_template = title_template

    @staticmethod
    def convert_date(date_: date) -> str:
        """Works for arbitrary date objects

        To be used later in date search / date summary
        """
        return date_.strftime("%b-%d-%Y")

    def get_date(self):
        return date.today().strftime(self.date_format)

    def use_template(self, date: str):
        return self.title_template.format(date=date)

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
            file.write(self.use_template(date))

    def open(self):
        if not self.check_todays_journal():
            self.new()
        return self.get_filepath(self.get_todays_filename())

    def search_single_word(self, word: str):
        matching_paths = []
        paths = listdir(self.journals_path)
        for j_path in paths:
            full_path = path.join(self.journals_path, j_path)
            with open(full_path) as file:
                text = file.read()
                num = text.count(word)

                if num > 0:
                    matching_paths.append((num, full_path))

        return matching_paths

    def open_journal_viewer(self, entries: List[Tuple[int, str]]):
        with open(self.outfile_path, "w") as file:
            file.write("=== Journal Viewer ===\n\n")

            if len(entries) > 0:
                file.write("#\tcount\tpath\n")
                for n, entry in enumerate(entries):
                    count = str(entry[0]).ljust(5)
                    file.write(f"{n}.\t{count}\t{entry[1]}\n")
            else:
                file.write("Search term not found\n")
