# Mail to Kindle #
## Description ##
This projects helps you saving your mail attachments (e.g. epub-files, PDFs) to a
temporary directory, convert the files to MOBI-format and send them directly
to your Kindle, so that you can read them later and do not have to do all
this by hand.

version 1.0.1

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

## Using Docker ##
This application is also available via Docker! Simply clone this repository, change the `config.ini`,
build the image and run the container via

```PowerShell
$ docker image build -t mail .
$ docker container run -itd --rm --name mail mail
```

Now you can use it via the `exec` command

```PowerShell
$ docker container exec -it mail python main.py
```

This can be automated using cronjobs on any server using Docker.