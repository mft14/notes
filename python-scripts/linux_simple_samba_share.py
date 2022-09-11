# This samba config is not excessively tested - only on Linux Mint 21. Use with care - recommend after a fresh installation
import os
import getpass

print("Simple Samba Setup, made by mft14 - mft14.github.com (22.08.22)")
print("---------------------------")
print("This script creates two config files, that then will be moved into the samba directory. ")
print("You can create quickly file sharing through your computers in the same network. There is no password encryption.")
print("If you leave the questions blank, it will be filled with standard infos, that should generally work.")
ask = input("\nType \"y\" to continue (y/n)  ")

if(ask == "y" or ask =="Y"):
    print("---------------------------") # Asking for three arguments
    server_name = input("Server Name? (default = \"My Server\"):\n")
    if(server_name == ""):
        server_name = "File Server"

    workgroup = input("Workgroup name? (default = myworkgroup):\n")
    if(workgroup == ""):
        workgroup = "myworkgroup"

    username = input("User name? (default = current username):\n")
    if(username == ""):
        username = getpass.getuser()

    sf_path = input("Enter path of your share folder (Default = /home/$USER/Public):\n")
    if(sf_path == ""):
        sf_path = "/home/"+username+"/Public"
        os.system('mkdir /home/'+username+'/Public')

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
    file.write('force user = '+username+'\n')
    file.close

    file = open("samba_install_instruction.txt", "w")
    file.write('Please follow these three steps to safely install your file server. Run these commands in this order until the line.\n')
    file.write('####################################\n')
    file.write('sudo apt install samba -y;\n')
    file.write('sleep 3 && sudo systemctl stop smbd ;\n')
    file.write('####################################\n')
    file.write('sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.bak;\n')
    file.write('sudo mv ~/smb.conf /etc/samba ;\n')
    file.write('sudo mv ~/shares.conf /etc/samba ;\n')
    file.write('sudo groupadd --system smbgroup ;\n')
    file.write('sudo useradd --system --no-create-home --group smbgroup -s /bin/false smbuser;\n')
    file.write('sudo chown -R smbuser:smbgroup '+sf_path+';\n')
    file.write('sudo chmod -R g+w '+sf_path+';\n')
    file.write('sudo adduser '+username+' smbgroup ;\n')
    file.write('####################################\n')
    file.write('sudo systemctl start smbd ;\n')
    file.write('sleep 3 && shutdown -r now ;\n')
    file.write('####################################\n')
    file.write('####################################\n')
    file.write('')
    file.write('After the reboot, you can bind the new shared folder.\n\n\nIn Windows:\n')
    file.write('net use Z: \\\\COMPUTERNAME\\SHAREDFOLDER /persistent:Yes\n\n')
    file.write('In Linux:\n')
    file.write('smb://COMPUTERNAME/SHAREDFOLDER')

    file.close

    # Move the scripts into home folder (since I dont have any idea how to do that exactly there while creating - help :D
    os.system('mv smb.conf ~/')
    os.system('mv shares.conf ~/')

    print("---------------------------")
    print("Successful!")
    print("smb.conf / shares.conf are created and being moved into your home directory.\n")
    print("Please follow the three instructions written in the next \"samba_install_instruction.txt\" file\n")
    print("Then reboot and it should be done!")
    print("---------------------------")
    print("Close with ENTER")
    input()
else:
    print("\nProgram closed")
