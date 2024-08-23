# KleinanzeigenRenewer

Automatically renews your Kleinanzeigen offerings by clicking on the renewal link inside your reminder mail.\
This is especially helpful when you are using the free version and have a lot of offerings online which can b a hassle to renew manually.\
Note: Usually you get the reminder mails 6 days before your offering will be deleted.

Make sure to edit the folowing credentials in the code for the access to your mail server:
```
username = "<imap username>"
password = "<imap password>"
imap_server = "<imap server>"
mail_folder = "INBOX" # folder where the mails from Kleinanzeigen can be found
```

When using subfolders, make sure to use the correct sring:
https://stackoverflow.com/questions/44230855/python-imaplib-selecting-folders

The script makes use of the following modules:
- selenium (for visiting the link)
- BeautifulSoup (for parsing the html of the mail and find the links)


## Was letzte Preis? -> Open Source! -> 0€
