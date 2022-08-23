import os

input("Put in your path:")
print()
path = 'C:\\xampp\\htdocs\\mft14.github.io\\tools\\apps'
isDirectory = os.path.isdir(path)
targetblank = ""

if(isDirectory is not True):
    print("Your path is not a valid Direcotry. Check again")

else:
    ask = input("Do you need target=blank? (Y/N) ")
    if(ask == "y" or ask == "Y"):
        targetblank = " target=\"_blank\""

    list_files = os.listdir(path) #list all files in an array
    file = open("link_list.html", "w") #make new file
    for i in range(0,len(list_files)): #list all files using array length

        link_name = list_files[i][0:list_files[i].find('.')].title()#substring from 0 to dot, title makes uppercase
        file.write("<a href=\""+list_files[i]+"\""+targetblank+">"+link_name+"</a>\n")

    file.close
