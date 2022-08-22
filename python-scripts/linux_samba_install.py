import os

print("Simple Samba Setup, made by Metal Fortress (22.08.22) - mft14.github.com")
print("---------------------------")
print("PLEASE READ BEFORE EXECUTING:")
print("- Run this on Linux (tested with: )")
print("- If you run this script, it will create two config files for samba and run an install script. It will ask for sudo permissions to run these. Check the source code as needed")
print("- This python script will move 2 config files into etc/samba/, add smbuser & smbgroup and gives permissions and your shared folder write access")
print("- This is for those, who wants a simple file share in their network. Nothing won't be encrypted with a password.\n")
print("I RECOMMEND to run this script first/only on a virtual machine or on a fresh linux install.")
go = input("\nType \"y\" to continue (y/n)  ")

if(go == "y" or go =="Y"):
    print("---------------------------") # Asking for three arguments
    server_name = input("Server Name? (default = \"My Server\"):\n")
    if(server_name == ""):
        server_name = "MyServer"

    workgroup = input("Workgroup name?:\n")
    if(workgroup == ""):
        workgroup = "Workgroup"

    sf_path = input("Enter path of your share folder (for example: /home/$USER/Public - If left empty, it will use the example):\n")
    if(sf_path == ""):
        sf_path = "home/$USER/Public"
    #######################################
    # More folders are planned in the future

    file = open("smb.conf", "w")
    file.write('[global]\n')
    file.write('server string = '+server_name+'\n')
    file.write('workgroup = '+workgroup+'\n')
    file.write('security = user\n')
    file.write('map to guest = Bad User\n')
    file.write('name resolve order = bcast host\n')
    file.write('include = /etc/samba/shares.conf\n')
    file.close

    file = open("shares.conf", "w")
    file.write('[Public]'+'\n')
    file.write('path = '+sf_path+'\n')
    file.write('force user = smbuser'+'\n')
    file.write('force group = smbgroup'+'\n')
    file.write('create mask = 0664'+'\n')
    file.write('force create mode = 0664'+'\n')
    file.write('directory mask = 0775'+'\n')
    file.write('force directory mode = 0775'+'\n')
    file.write('public = yes'+'\n')
    file.write('writable = yes'+'\n')
    file.close

    file = open("installsamba.sh", "w")
    file.write('sudo apt install samba -y;\n')
    file.write('sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.bak;\n')
    file.write('sudo mv ~/smb.conf /etc/samba ;\n')
    file.write('sudo mv ~/shares.conf /etc/samba ;\n')
    file.write('sudo groupadd --system smbgroup ;\n')
    file.write('sudo useradd --system --no-create-home --group smbgroup -s /bin/false smbuser;\n')
    file.write('sudo chown -R smbuser:smbgroup '+sf_path+';\n')
    file.write('sudo chmod -R g+w '+sf_path+';\n')
    file.write('sudo adduser $USER smbgroup ;\n')
    file.write('systemctl start smbd ;\n')
    file.write('')
    file.close

    # Move the scripts into home folder (since I dont have any idea how to do that exactly there while creating - help :D
    os.system('mv smb.conf ~/')
    os.system('mv shares.conf ~/')

    os.system('sudo systemctl stop smbd')

    print("---------------------------")
    print("Successful!")
    print("smb.conf / shares.conf are created and being moved into your home directory.")
    print("Next you need to stop the server manually with = sudo systemctl stop smbd")
    print("After that, just launch the new .sh shell script with sudo (sudo sh installsamba.sh)\n")
    print("Then reboot and it should be done!")
    print("---------------------------")
    print("Close with ENTER")
    input()
else:
    print("\nProgram closed")
