import os
from pathlib import Path  #core python module

html_name = "_link_list.html"

def generate_links(user_path):

    a_target = ""
    a_class=""
    output = ""
    counter = 0
    br = ""
    path = user_path #pass the new path
    ask = input("Do you need --> target=_blank? (default = no) (y/n) ")
    if(ask == "y" or ask == "Y"):
        a_target = " target=\"_blank\""

    ask = input("Do you need --> class=\"\"? (default = no) (y/n) ")
    if(ask == "y" or ask == "Y"):
        a_class = " class=\"\""

    ask = input("Do you need --> <br> (default = no) (y/n) ")
    if(ask == "y" or ask == "Y"):
        br = "<br>"

    list_files = os.listdir(path) #list all files in an array
    list_files = sorted(list_files) #sort alphabetically

    file = open(html_name, "w") #make new file

    for i in range(0,len(list_files)): #list all files using array length

        if(list_files[i][0] == '.'):
            pass
        elif(list_files[i].__contains__('.')):

            a_href=" href=\""+list_files[i]+"\""
            link_name = list_files[i][0:list_files[i].find('.')].title()#substring from 0 to dot, title makes uppercase
            output = "<a"+a_target+a_class+a_href+">"+link_name+"</a>"+br #assemble the link

            file.write(str(output)+"\n")
            print(str(output))
            counter = counter + 1

    file.close
    print("\nSuccessfully created " + str(counter) + " link(s)! Created --> "+html_name)

######## Program starts here

print("HTML Link Creator will create quickly links to all your files in the current directory, where this .py has been executed!\n")
print("----------------------")
ask = input ("Do you want to use your current directory or type your directory (path) manually?\n1 = current directory <-- (default)\n2 = new path = ")

if(ask == "2"):
    path = input("\nPut in your new path = ")
    while(os.path.isdir(path) is not True):#if typed directory is bad
        path = input("\nPlease type again or type\nc = cancel \ncd = current directory  \n----------------------\nNew path = ")
        if(path.lower()== "c"):#shutdown app
            print("\n----------------------\nProgram canceled.")
            break
        elif(path.lower()== "cd"):
            path = Path.cwd()
    
    generate_links(path)#path self inserted
else:
    path = Path.cwd()
    generate_links(path)#cwd Path and go












