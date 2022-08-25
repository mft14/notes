#Outlook Attachment grabber Script by Karim Kiel - 25.08.2022

from pathlib import Path  #core python module
import datetime
import win32com.client  #pip install pywin32

searched_file_ext = ".png" #change this if you need a different file extension to be grabbed
counter = 0
html = ["<table>","</tr></table>","<td>","</td>","<thead>","</thead>"] #ht = html table

# Create output folder
output_dir = Path.cwd() / "C:\\Users\\KarimKiel\\Downloads\\Rechnungen" #Output folder
output_dir.mkdir(parents=True, exist_ok=True)
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")# Connect to outlook

# inbox = outlook.Folders["kiel@it-stade.de"].Folders["Posteingang"] #ADD: Check inbox name (different language matter)
inbox = outlook.GetDefaultFolder(6)
# https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
# DeletedItems=3, Outbox=4, SentMail=5, Inbox=6, Drafts=16, FolderJunk=23

now = str(datetime.datetime.now())[0:str(datetime.datetime.now()).find('.')]#gets today's date correctly formatted
file = open(str(output_dir)+"\\log.html", "w")#starting a new logfile log 
file.write("<style>body{font-family: Arial;}table{border-collapse:collapse;}td{border-bottom:1px solid black;padding:6 36 6 6;}thead{font-weight:bold;font-size:20;}</style>")
file.write("<table><thead><td>Attachments</td><td>Email</td></thead>") #start html table for log file


messages = inbox.Items# Get messages
for message in messages:
    subject = message.Subject #get subject names
    attachments = message.Attachments #get attachment names
    date = str(message.receivedTime)# get email dates
    date = str(date.replace(":","-"))#change all : to - cuz folder names don't allow ":" 
    date = str(date[2:date.find('.')])
    
    for attachment in attachments:
        if(str(attachment).__contains__(searched_file_ext)):#search for file ext
            target_folder = output_dir / str(date+"_"+subject.replace(":",""))#date before name for better sorting, replacing uncommon chars to nothing
            target_folder.mkdir(parents=True, exist_ok=True)#make folder, even with exist
            attachment.SaveAsFile(target_folder / str(attachment)) #Save attachment in targetfolder with attach name

            #This is just for the log
            counter = counter + 1#counting for how many 
            file.write("")
            file.write("")
            file.write("<tr>")
            file.write("<td>"+str(date)+"</td>")
            file.write("<td><a href=\"")
            file.write(str(output_dir)+"\\")
            file.write(str(date+"_"+subject.replace(":",""))+"\\")
            file.write(str(attachment)+"\" target=\"_blank\">")
            file.write(str(attachment)+"</a></td>")
            file.write("<td>"+str(subject)+"</td>")
            file.write("</tr>")
            print("Attachment found: " + str(attachment)+" ---> in Mail: \"" + str(subject)+"\"")#print in console
        else: 
            print("No "+searched_file_ext+" attachment in Mail: " + str(subject))

#write footer of log

file.write("</table><br><hr><p>Found " +str(counter)+ " "+searched_file_ext+" file(s)<br>Last log operation: <b>"+now+"</b></p>")
file.close #close log file