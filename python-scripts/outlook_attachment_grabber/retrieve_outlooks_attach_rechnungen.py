from pathlib import Path  #core python module
import win32com.client  #pip install pywin32

searched_file_ext = ".pdf"

# Create output folder
output_dir = Path.cwd() / "C:\\Users\\KarimKiel\\Downloads\\Rechnungen"
output_dir.mkdir(parents=True, exist_ok=True)

# Connect to outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Connect to folder
# inbox = outlook.GetDefaultFolder(6)
inbox = outlook.Folders["kiel@it-stade.de"].Folders["Posteingang"] #ADD: spezifische Mail, bei Posteingang Sprache beachten, im Englischen Inbox

# https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
# DeletedItems=3, Outbox=4, SentMail=5, Inbox=6, Drafts=16, FolderJunk=23

# Get messages
messages = inbox.Items

for message in messages:
    subject = message.Subject
    body = message.body
    attachments = message.Attachments
    date = str(message.receivedTime) 
    date = str(date.replace(":","-"))
    
    print(str(date))
    input()

    # Create separate folder for each message
    target_folder = output_dir / str("TEST"+subject.replace(":",""))
    print("tg name: "+str(target_folder))
    target_folder.mkdir(parents=True, exist_ok=True)

    # Save attachments
    for attachment in attachments:
        if(str(attachment).__contains__(searched_file_ext)):
            attachment.SaveAsFile(target_folder / str(attachment))
        else:
            print("Couldn't find "+searched_file_ext+" extension")