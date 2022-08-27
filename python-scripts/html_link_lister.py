import os
from pathlib import Path  #core python module

# input("Put in your path:")

path = Path.cwd()
isDirectory = os.path.isdir(path)
targetblank = ""
counter = 0

print("path === " + str(path))
input()

if(isDirectory is not True):
    print("Your path is not a valid Direcotry. Check again")

else:
    ask = input("Do you need target=blank? (Y/N) ")
    if(ask == "y" or ask == "Y"):
        targetblank = " target=\"_blank\""

    list_files = os.listdir(path) #list all files in an array
    list_files = sorted(list_files)

    print("list files === " + str(list_files)+"\n\n")
    input()
    file = open("_link_list.html", "w") #make new file
    for i in range(0,len(list_files)): #list all files using array length

        link_name = list_files[i][0:list_files[i].find('.')].title()#substring from 0 to dot, title makes uppercase
        file.write("<a href=\""+list_files[i]+"\""+targetblank+">"+link_name+"</a>\n")

        print(list_files[i])
        counter = counter + 1

    file.close

print("Successfully created " + str(counter) + " link(s)! ")
