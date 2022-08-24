import os

print("HTML IMG List Creator by MFT14\n")
yn = "" #Yes no chooser
path = input("Please type in your path: ")
isDirectory = os.path.isdir(path)

if(isDirectory is not True):
    print("Your path is not a valid Directory. Check again")

else: #add target blank into that placeholder string
    list_files = os.listdir(path) #list all files in an array
    file = open("link_list_img.html", "w") #make new file
    for i in range(0,len(list_files)): #list all files using array length
        file.write("<img src=\""+list_files[i]+"\">\n")
    file.close

    for i in range(0,len(list_files)): #list all files using array length
        print("<img src=\""+list_files[i]+"\">")

    print("")
    print("Successfully created!")
    input("")
