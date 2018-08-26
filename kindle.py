import subprocess
import configparser
import os
from pathlib import Path, PurePath


class Kindle:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")

        self.tmp_dir_name = config["DEFAULT"]["tmp_dir_name"]
        self.file_format = config["DEFAULT"]["file_format"]
        self.flag = False

        self.sender = config["KINDLE"]["sender_address"]
        self.recipient = config["KINDLE"]["kindle_address"]
    

    def convert_files(self):
        if not os.path.exists(self.tmp_dir_name):
            self.flag = True
            return
        
        dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\" + self.tmp_dir_name
        path = Path(dir_path)
        files = path.iterdir()

        for file in files:
            if file.is_file() and file.name.endswith(self.file_format):
                file_mobi = file.stem + ".mobi"
                subprocess.run(["ebook-convert", file.name, file_mobi], cwd=self.tmp_dir_name,
                    shell=True)
    

    def send_files(self):
        if self.flag:
            return
        
        dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\" + self.tmp_dir_name
        path = Path(dir_path)
        files = path.iterdir()

        for file in files:
            if file.is_file() and file.name.endswith("mobi"):
                subprocess.run(["calibre-smtp", "-a", file.name, self.sender, self.recipient, " "],
                    cwd=self.tmp_dir_name, shell=True)
