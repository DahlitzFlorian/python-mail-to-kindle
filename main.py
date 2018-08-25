import configparser
import mail


def main():
    emails = mail.Mail()
    emails.save_attachments()
    emails.logout()


if __name__ == "__main__":
    main()
