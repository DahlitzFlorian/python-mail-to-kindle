import configparser
import shutil
import subprocess

from pathlib import Path, PurePath


class Kindle:
    def __init__(self):
        print("Get kindle configuration data...")
        config = configparser.ConfigParser()
        config.read("config.ini")

        self.tmp_dir_name = Path(config["DEFAULT"]["tmp_dir_name"])
        self.file_format = config["DEFAULT"]["file_format"]
        self.flag = False

        self.sender = config["KINDLE"]["sender_address"]
        self.recipient = config["KINDLE"]["kindle_address"]

    def convert_files(self):
        if not self.tmp_dir_name.exists():
            self.flag = True
            return

        print("Get files to convert...")
        path = Path().cwd() / self.tmp_dir_name
        files = path.iterdir()

        print("Convert files...")
        print("-" * 40)
        for file in files:
            if file.is_file() and file.name.endswith(self.file_format):
                file_mobi = file.stem + ".mobi"
                subprocess.run(
                    ["ebook-convert", file.name, file_mobi],
                    cwd=self.tmp_dir_name,
                )

        print("-" * 40)
        print("Convertion was successful.")

    def send_files(self):
        if self.flag:
            return

        print("Get files to send to kindle...")
        path = Path().cwd() / self.tmp_dir_name
        files = path.iterdir()

        print("Send files...")
        for file in files:
            if file.is_file() and file.name.endswith("mobi"):
                subprocess.run(
                    ["calibre-smtp", "-a", file.name, self.sender, self.recipient, " "],
                    cwd=self.tmp_dir_name,
                )

        print("Files were send.")
        print("Delete tmp directory...")

        shutil.rmtree(self.tmp_dir_name, ignore_errors=True)

        print("Deletion was successful.")
