from datetime import date
from os import path

class Journals:
    def __init__(self, journals_path, date_format, title_template):
        self.journals_path = journals_path
        self.date_format = date_format
        self.title_template = title_template

    def get_date(self):
        return date.today().strftime(self.date_format)

    def use_template(self, date: str):
        return self.title_template.format(date=date)

    @staticmethod
    def wrap_date_for_filename(date):
        return f"journal_{date}.md"

    def get_filepath(self, name):
        return path.join(self.journals_path, name)

    def get_todays_filename(self):
        return self.wrap_date_for_filename(self.get_date())

    def check_todays_journal(self):
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
