import mail
import kindle


def main():
    emails = mail.Mail()
    emails.save_attachments()
    emails.logout()

    kindle_device = kindle.Kindle()
    kindle_device.convert_files()
    kindle_device.send_files()


if __name__ == "__main__":
    main()
