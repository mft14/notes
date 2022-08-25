#Outlook Attachment grabber Script by Karim Kiel - 25.08.2022

from pathlib import Path  #core python module
import datetime
import win32com.client  #pip install pywin32

searched_file_ext = ".pdf" #change this if you need a different file extension to be grabbed
counter = 0

# Create output folder
output_dir = Path.cwd() / "C:\\Users\\KarimKiel\\Downloads\\Rechnungen" #Output folder
output_dir.mkdir(parents=True, exist_ok=True)
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")# Connect to outlook

# inbox = outlook.Folders["kiel@it-stade.de"].Folders["Posteingang"] #ADD: Check inbox name (different language matter)
inbox = outlook.GetDefaultFolder(6)
# https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
# DeletedItems=3, Outbox=4, SentMail=5, Inbox=6, Drafts=16, FolderJunk=23

now = str(datetime.datetime.now())[0:str(datetime.datetime.now()).find('.')]#gets today's date correctly formatted
file = open(str(output_dir)+"\\log.txt", "w")#starting a new logfile log 

messages = inbox.Items# Get messages
for message in messages:
    subject = message.Subject #get subject names
    attachments = message.Attachments #get attachment names
    date = str(message.receivedTime)# get email dates
    date = str(date.replace(":","-"))#change all : to - cuz folder names don't allow ":" 
    
    for attachment in attachments:
        if(str(attachment).__contains__(searched_file_ext)):#search for file ext
            target_folder = output_dir / str(date[2:date.find('.')]+"_"+subject.replace(":",""))#date before name for better sorting, replacing uncommon chars to nothing
            target_folder.mkdir(parents=True, exist_ok=True)#make folder, even with exist
            attachment.SaveAsFile(target_folder / str(attachment)) #Save attachment in targetfolder with attach name

            counter = counter + 1#counting for how many 
            file.write(str(attachment)+"\nMail ---> \"" + str(subject)+"\""+"\n\n")#write log
            print("Attachment found: " + str(attachment)+" ---> in Mail: \"" + str(subject)+"\"")#print in console
        else: 
            print("No "+searched_file_ext+" attachment in Mail: " + str(subject))

#write footer of log
file.write("-------------------------")
file.write("\nOperation done. Found " +str(counter)+ " "+searched_file_ext+" file(s)\n")
file.write("Last operaton run: " + now)
file.close #close log file