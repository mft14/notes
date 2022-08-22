# Linux Configs and Settings
Linux often needs more text adjustments than Windows. But that does not mean, it's unpractical. Most of these settings can be saved as small config file and 
can be used later on, usually by copying/overwriting existing files. And even this step can be automated by simple bash scripts! That's why I made this cheatsheet.


## Navigation
- **Settings**
- **Config Locations**
- **Configs**
  - [Simple SSH](#simple-ssh)
  - [Simple Shared Folder with Samba](#simple-shared-folder-with-samba)

# Settings

# Config Locations

# Configs
## Simple SSH
#### ON SERVER
|Command|Meaning|
|---|---|
|`sudo apt install openssh-server`|Install SSH|
|`sudo systemctl status sshd`|Check server status|
|`hostname -l`|list IP Adress of server|
|`whoami`|Shows user name|

#### ON CLIENT
Login with: `ssh USERNAME@IP`<br>
- where **USERNAME** is the one you found out with `whoami`<br>
- where **IP** is the IP Adress of the server (found out by using `hostname -l` OR `ip a`)

##### Save SERVER adresses
If you have multiple servers, this is useful. Give them names of your choice.
- Create file in home folder like this: `sudo nano .ssh/config`
- Insert this:
```
Host NAME_OF_YOUR_CHOICE
    HostName SERVER_IP_ADRESS
    IdentityFile ~/.ssh/YOUR_FOLDER_NAME
    User USERNAME_OF_SERVER
```
|Placeholder|Example|
|---|---|
|NAME_OF_YOUR_CHOICE|MyServer|
|SERVER_IP_ADRESS|192.168.1.1|
|YOUR_FOLDER_NAME|server1 OR myserver|
|USERNAME_OF_SERVER|user1|

> Note: This is a simple access without any further security policies. Just use this for non-sensitive files. Encryption might follow

## Simple Shared Folder with Samba
### ON SERVER
Create two files and save them for future use.
##### Create smb.conf and fill it with this:
```
[global]
server string = SERVER_NAME
workgroup = WORKGROUP_NAME
security = user
map to guest = Bad User
name resolve order = bcast host
include = /etc/samba/shares.conf
```
##### Create shares.conf and fill it with this:
**Note:** The shares.conf sets up the folders you want to share. I usually use the pre-created __Public__ folder. You can use any other location and even add more at once. For another location, copy the whole code, change the path and name it differently. 
```
[Public]
path = /home/$USER/Public
force user = smbuser
force group = smbgroup
create mask = 0664
force create mode = 0664
directory mask = 0775
force directory mode = 0775
public = yes
writable = yes
```

Save them in your **home folder ~/** for the following script or adjust the path.
##### Run these three scripts in a row
```
sudo systemctl stop smbd
```
Wait for the server being stopped. You can additionally check with `sudo systemctl status smbd`
```
sudo apt install samba -y; 
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.bak ;
sudo cp ~/smb.conf /etc/samba ;
sudo cp ~/shares.conf /etc/samba ;
sudo groupadd --system smbgroup ;
sudo useradd --system --no-create-home --group smbgroup -s /bin/false smbuser ; 
sudo chown -R smbuser:smbgroup /home/$USER/Public ;
sudo chmod -R g+w /home/$USER/Public ;
sudo adduser $USER smbgroup ;
systemctl start smbd ;
```
Wait for samba to be restarted - then rebooting the system:
```
reboot
```
After a reboot, the folder can be reached now using **samba://SERVERNAME/SHARED_FOLDER** (here: Public) or it shows up automatically in your file explorer of choice. (under "Network" or "Other locations")

