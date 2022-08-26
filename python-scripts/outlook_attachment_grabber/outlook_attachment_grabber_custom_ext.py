#Outlook Attachment grabber Script by Kiel (Metal Fortress) 24.08.2022 --- mft14.github.com

# How to use
# - 1: Put in as many file extensions as you need in the "attach_filter" array. Pattern looks like this ".pfd" , ".jpg" -- seperate with comma !
# - 2: Configure a path, where your attachments should be saved (change output_dir)
# - Additionally rename the log file
#
# The log.html file will give you an overview of what has been automatically grabbed. Under the HTML table, you can also see a small result section. 
# If your emails have special characters, it will skip creating that folder. To notify you, check the error.txt, that will be created. 
# If an error happens, go down to the line with the comment "#ADD MORE REPLACE FILTER" and add more lines and char replacing to it

from pathlib import Path  #core python module
import datetime
import win32com.client  #pip install pywin32

attach_filter = [".pdf",".png"] #change or add here as many file ext as you need
output_dir = Path.cwd() / "MyOutlookAttachments" #Output folder - or use full path = C:\\Users\\NAME\\Downloads\\MyOutlookAttachments
log = "Overview_log" #log file NAME
counter = [0] * len(attach_filter)#Counter for counting each file ext
month_names = ["","-Jan","-Feb","-Mar","-Apr","-Mai","-Jun","-Jul","-Aug","-Sep","-Oct","-Nov","-Dec"]
errorlog = False

# Create output folder
output_dir.mkdir(parents=True, exist_ok=True)
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")# Connect to outlook

inbox = outlook.GetDefaultFolder(6)
# inbox = outlook.Folders["YOURMAIL@MAIL.COM"].Folders["Inbox"] #IMPORTNAT: Check inbox name (different languages matter)
# https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
# DeletedItems=3, Outbox=4, SentMail=5, Inbox=6, Drafts=16, FolderJunk=23

now = str(datetime.datetime.now())[0:str(datetime.datetime.now()).find('.')]#gets today's date correctly formatted - this is for the log html file
file = open(str(output_dir)+"\\"+log+".html", "w")#starting a new logfile log 
file.write("<style>body{font-family: Arial;}a{text-decoration: none;}a:hover{color:orange;}table{border-collapse:collapse;}td{border-bottom:1px solid black;padding:6 36 6 6;}thead{font-weight:bold;font-size:20;}</style>")
file.write("<table><thead><td>Receiving Date</td><td>Attachments</td><td>Email Subject Name</td></thead>") #start html table for log file

messages = inbox.Items# Get messages
for message in reversed(messages):
    attachments = message.Attachments #get attachment names
    subject = message.Subject #get subject names

    #ADD MORE REPLACE FILTER if you encounter special characters in your email headline
    subject = subject.replace(":","") 
    subject = subject.replace("\"","-") 
    subject = subject.replace("\\"," ") 
    subject = subject.replace("/"," ") 
    subject = subject.replace("%"," ") 
    subject = subject.replace("$"," ") 

    date = str(message.receivedTime)# get email dates
    date = str(date.replace(":","-"))#change all : to - cuz folder names don't allow ":" 

    date = str(date[2:19]) #it seems sometimes the dates have . or zeros so I use this for trimming - Additionally commen this line out and reactivate the next two ones
    # date = str(date[2:date.find('.')])
    # date = str(date[2:date.find('+')])
    
    for attachment in reversed(attachments):# look through attachments first, IF there isnt, then skip that mail 
        for i in range(0,len(attach_filter)):# look through the first ext, then download all, then next extension
            if(str(attachment).__contains__(attach_filter[i])):#search for file ext

                month_number = date[3:5].lstrip('0') #extract month names, 1 = Jan ; 12 = Dec etc., removing 0 in front of date numbers to use it for the array month_names
                month_folder = date[3:5]+month_names[int(month_number)] # assembling month folder name
                year_folder = "20"+date[0:2] # Year folder name

                #UN/COMMENT THESE LINES if you want to have everything in one folder preferably 
                target_folder = output_dir /year_folder/month_folder/ str("Day "+date[6:8]+" - "+str(date[len(date)-8:len(date)-3]).replace('-','h')+" --- "+subject)#date before name for better sorting, replacing uncommon chars to nothing
                # target_folder = output_dir / str(date+"_"+subject)#use this if everything should be in thrown one folder

                try:# Try creating folders but when bad letters, throw error message
                    target_folder.mkdir(parents=True, exist_ok=True)#make folder, even with exist
                    attachment.SaveAsFile(target_folder / str(attachment)) #Save attachment in targetfolder with attach name

                    #This is for the log - creating a table
                    counter[i] = counter[i] + 1 #counting each file extention using an array
                    file.write("<tr>")
                    file.write("<td>"+str(message.receivedTime)[2:16].replace(" "," -- ")+"</td>") #write date in table

                    # Use this for file names only, not with link.
                    # file.write("<td>"+str(attachment)+"</td>") #

                    # Use this for file names with links.
                    file.write("<td><a href=\"") #start ahref
                    file.write(str(target_folder)+"\\" + str(attachment)+"\" target=\"_blank\">"  ) #put path in href
                    file.write(str(attachment)+"</a></td>") #use attach name as link text
                    file.write("<td>"+str(subject)+"</td>") #put email subject name in table
                    file.write("</tr>")
                    print("Attachment found: " + str(attachment)+" ---> in Mail: \"" + str(subject)+"\"")#print status

                except NotADirectoryError: #if subject has invalid chars, create error log
                    err_message = "Couldn't create folder for this mail. Invalid special characters"
                    print(err_message + str(subject))
                    err_file = open(str(output_dir)+"\\""error.txt", "w")#starting err log
                    err_file.write(err_message + "\n--> " + str(subject)+"\n")
                    errorlog = True
            else: 
                print("No "+attach_filter[i]+" attachment in Mail: " + str(subject))#print status

#write html footer
file.write("</table><br><hr>") # End table
for i in range(0,len(attach_filter)): # Count and print how many attachs have been found
    file.write("Found <u>" +str(counter[i])+ " attachments</u> with <b>"+attach_filter[i]+"</b> included<br>")

file.write("<p>In total: <b><u>" +str(sum(counter))+ " attachments</u></b><br>Last log operation: <b>"+now+"</b></p>")# total files
file.close #close log file

if(errorlog == True):#close errorlog only when there is one
    err_file.close