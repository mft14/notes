import os
from pathlib import Path  #core python module

print("HTML Link Creator will create quickly links to all your files in the current directory, where this .py has been executed!\n")

path = Path.cwd()
isDirectory = os.path.isdir(path)

a_target = ""
a_class=""
output = ""

counter = 0

if(isDirectory is not True):
    print("Your path is not a valid Direcotry. Check again")

else:
    ask = input("Do you need --> target=_blank? (default = no) (y/n) ")
    if(ask == "y" or ask == "Y"):
        a_target = " target=\"_blank\""

    ask = input("Do you need --> class=\"\"? (default = no) (y/n) ")
    if(ask == "y" or ask == "Y"):
        a_class = " class=\"\""

    list_files = os.listdir(path) #list all files in an array
    list_files = sorted(list_files) #sort alphabetically

    file = open("_link_list.html", "w") #make new file

    for i in range(0,len(list_files)): #list all files using array length

        if(list_files[i][0] == '.'):
            pass
        elif(list_files[i].__contains__('.')):

            a_href=" href=\""+list_files[i]+"\""
            link_name = list_files[i][0:list_files[i].find('.')].title()#substring from 0 to dot, title makes uppercase

            output = "<a"+a_target+a_class+a_href+">"+link_name+"</a>" #assemble the link

            file.write(str(output)+"\n")
            print(str(output))
            counter = counter + 1

    file.close

print("\nSuccessfully created " + str(counter) + " link(s)! ")
