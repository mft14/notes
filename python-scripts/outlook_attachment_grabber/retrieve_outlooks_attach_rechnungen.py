from pathlib import Path  #core python module
import win32com.client  #pip install pywin32

searched_file_ext = ".pdf"
counter = 0

# Create output folder
output_dir = Path.cwd() / "C:\\Users\\KarimKiel\\Downloads\\Rechnungen"
output_dir.mkdir(parents=True, exist_ok=True)
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")# Connect to outlook

# Connect to folder
# inbox = outlook.GetDefaultFolder(6)
inbox = outlook.Folders["kiel@it-stade.de"].Folders["Posteingang"] #ADD: spezifische Mail, bei Posteingang Sprache beachten, im Englischen Inbox
# https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
# DeletedItems=3, Outbox=4, SentMail=5, Inbox=6, Drafts=16, FolderJunk=23

#write log
file = open(str(output_dir)+"\\log.txt", "w")

messages = inbox.Items# Get messages
for message in messages:
    subject = message.Subject
    body = message.body
    attachments = message.Attachments
    date = str(message.receivedTime) 
    date = str(date.replace(":","-"))
    
    for attachment in attachments:
        if(str(attachment).__contains__(searched_file_ext)):#search for file ext
            target_folder = output_dir / str(date[2:date.find('.')]+"__"+subject.replace(":",""))#date before name for better sorting, replacing uncommon chars to nothing
            target_folder.mkdir(parents=True, exist_ok=True)#make folder, even with exist
            attachment.SaveAsFile(target_folder / str(attachment))
            print("Attachment found: " + str(attachment))
            counter = counter + 1
            file.write(str(attachment)+"\n")#write log
            # print("Couldn't find "+searched_file_ext+" extension")

file.write("\nOperation done. Found " +str(counter)+ " "+searched_file_ext+" file(s)\n\n")
file.close #close log file
print("-------------------------")
print("\nOperation done. Found " +str(counter)+ " "+searched_file_ext+" file(s)\n\n")