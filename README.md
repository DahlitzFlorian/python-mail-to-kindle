# Mail to Kindle #
## Description ##
This projects helps you saving your mail attachments (e.g. epub-files, PDFs) to a
temporary directory, convert the files to MOBI-format and send them directly
to your Kindle, so that you can read them later and do not have to do all
this by hand.

version 1.0

## Prerequisites ##
 - [Calibre](https://calibre-ebook.com/) (installs the needed CLI as well)
 - Changed the default values in the configuration file (current values are set to *insert_here*)

## Configuration ##
To customize the application for your needs, apply changes to the corresponding configuration file, which is in the root directory and named **config.ini**.

The following things can be customized:
 - Email Accounts Username (*email_username*)
 - Email Accounts Password (*email_password*)
 - Email Accounts IMAP-Server (*imap_url*)
 - File Format of the Attachments (*file_format*)
 - Directory name of the temporary directory (*tmp_dir_name*)
 - Kindle E-Mail-Address (*kindle_address*)
 - Accepted sender by Kindle (*sender_address*)