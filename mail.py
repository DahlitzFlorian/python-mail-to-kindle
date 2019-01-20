import imaplib
import email
import datetime
import configparser
import os


class Mail:
    def __init__(self):
        print("Get mail configuration data...")
        config = configparser.ConfigParser()
        config.read("config.ini")

        self.username = config["EMAIL"]["email_username"]
        self.password = config["EMAIL"]["email_password"]
        self.imap_url = config["EMAIL"]["imap_url"]
        self.file_format = config["DEFAULT"]["file_format"]
        self.tmp_dir_name = Path(config["DEFAULT"]["tmp_dir_name"])

        self.today = datetime.datetime.now().strftime("%d-%b-%Y")

        self.login()
        self.inbox()

    def login(self):
        while True:
            try:
                self.imap = imaplib.IMAP4_SSL(self.imap_url, 993)
                r, d = self.imap.login(self.username, self.password)

                if r != "OK":
                    print("Login failed.\n")
                    raise ConnectionError

                print(" > Sign as ", d)
            except:
                print(" > Sign In ...")
                continue
            # self.imap.logout()
            break

    def logout(self):
        print("Logout...")
        return self.imap.logout()

    def inbox(self):
        print("Select folder: Inbox")
        return self.imap.select("Inbox")

    def save_attachments(self):
        print("Save attachments...")
        typ, data = self.imap.search(None, '(SINCE "' + self.today + '")', "ALL")
        mails = data[0].split()
        for mail in mails:
            t, d = self.imap.fetch(mail, "(RFC822)")
            msg = email.message_from_bytes(d[0][1])
            for part in msg.walk():
                if "application/epub" in part.get_content_type():
                    if part.get_filename().endswith(f".{self.file_format}"):
                        if not self.tmp_dir_name.exists():
                            self.tmp_dir_name.mkdir(exist_ok=True, parents=True)
                        fp = open(self.tmp_dir_name / part.get_filename(), "wb")
                        fp.write(part.get_payload(decode=1))
                        fp.close

        self.imap.close()
        print("Saved attachments successfully.")
