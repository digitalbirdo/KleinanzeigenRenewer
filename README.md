# KleinanzeigenRenewer
Automatically renews your Kleinanzeigen offerings by clicking on the renewal link insode your reminder mail.

make sure to edit the folowing credentials in the code for the access to your mail server:
```
username = "<imap username>"
password = "<imap password>"
imap_server = "<imap server>"
mail_folder = "INBOX" # folder where the mails from Kleinanzeigen can be found
```

Usually you get the reminder mails 6 days before your offering will be deleted.

The script makes use of the following modules:
- selenium (for visiting the link)
- BeautifulSoup (for parsing the html of the mail and find the links)
