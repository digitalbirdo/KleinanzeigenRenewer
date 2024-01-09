import imaplib
import email
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import concurrent.futures
from bs4 import BeautifulSoup

# account credentials
username = "<imap username>"
password = "<imap password>"
imap_server = "<imap server>"
mail_folder = "INBOX" # folder where the mails from Kleinanzeigen can be found

ignore_file="already_processed.txt"

# connect to imap mail server
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)

# Search for relevant messages
status, messages = imap.select(mail_folder, readonly=True)
term = u"Deine Anzeige läuft in einer Woche aus".encode("utf-8")
imap.literal = term
typ, msgnums = imap.search("utf-8", 'SUBJECT')
ids= str(msgnums[0]).replace("b","").replace("\'","").split(" ")#[-3:]
msgs=[]
for id in ids:
    res, msg = imap.fetch(str(id), "(RFC822)")
    msgs.append(msg)

# load links which have already been porcessed
file = open(ignore_file, 'a')
file.close()
with open(ignore_file) as f:
    lines = [line.rstrip('\n') for line in f]

# function which handles a specific mail
def handleMail(msg):
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            content_type = msg.get_content_type()
            body = msg.get_payload(decode=True).decode()
            if content_type == "text/html":

                 # Find all elements with the tag <a>
                soup = BeautifulSoup(body, 'html.parser')
                links = soup.find_all("a")

                for link in links:
                    if "Anzeige verlängern</font>" in str(link):

                        # check if the link was already processed
                        ignoreLink=False
                        for line in lines:
                            if link.get("href") in line:
                                ignoreLink=True

                        if not ignoreLink:
                            # open link in selenium webbrowser
                            print("Link:" + link.get("href"))
                            options = Options()
                            options.add_argument("--headless=new") # for Chrome >= 10
                            driver = webdriver.Chrome(options=options)
                            driver.get(link.get("href"))
                            driver.quit()

                            # return the link so it will be later added to the processed links file
                            return link.get("href")



# handle all messages at the same time in different threads
threads=None
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    threads = executor.map(handleMail, msgs)

# append all processed links to the ignore file
with open(ignore_file, "a") as myfile:
    for thread in threads:
        if thread is not None:
            print(thread)
            myfile.write(thread)
            myfile.write("\n")

print("Done")