import os

print("HTML Link Lister by MFT14\n")

yn = "" #Yes no chooser
path = input("Please type in your path: ")
path.replace("\\","/")
isDirectory = os.path.isdir(path)

if(isDirectory is not True):
    print("Your path is not a valid Directory. Check again")

else: #add target blank into that placeholder string
    yn = input("Do you need target=_blank? (Y/N) ")
    if(yn.lower() == "y" or yn == "yes"):
        targetblank = " target=\"_blank\""
    else: 
        targetblank = ""

    list_files = os.listdir(path) #list all files in an array
    file = open("link_list.html", "w") #make new file
    for i in range(0,len(list_files)): #list all files using array length
        link_name = list_files[i][0:list_files[i].find('.')].title()#substring from 0 to dot, title makes uppercase
        file.write("<a href=\""+list_files[i]+"\""+targetblank+">"+link_name+"</a>\n")
    file.close

    print("")
    print("Successfully created!")
    input("")
